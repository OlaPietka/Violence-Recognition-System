"""
Main module responsible for coordinating work between modules.
- Benedykt Kościński
"""

import multiprocessing
import threading
import time
from datetime import datetime

import cv2
from config import (CAM_ADDRESS, DIDN_ENABLED, DIDN_FRAME_COUNT, FGN_ENABLED,
                    FGN_FRAME_COUNT, VRN_ENABLED, VRN_FRAME_COUNT)
from didn import didn_predict, didn_reshape, didn_transform
from fgn import fgn_predict, fgn_reshape, fgn_transform
from log import log_all, log_start, log_stop
from video_cap import available_frames, collect_frames
from vrn import vrn_predict, vrn_reshape, vrn_transform


"""
Universal function that performs necessary transformations and orders prediction.
"""
def predict(frames, reshape, transform, prediction):
    reshaped_frames = reshape(frames)
    transformed_frames = transform(reshaped_frames)
    prediction = prediction(transformed_frames)
    return prediction


def main():
    # Initialising the camera connection and continuously collecting new frames in a separate thread.
    cap = cv2.VideoCapture(CAM_ADDRESS)
    pool = multiprocessing.Pool()
    threading.Thread(target=collect_frames, args=(cap,)).start()
    log_start(CAM_ADDRESS, FGN_ENABLED, VRN_ENABLED, DIDN_ENABLED)

    # Main loop responsible for transformation and prediction ordering.
    while True:
        if len(available_frames) >= 64:
            ts = datetime.now()

            # Depending on whether the module is enabled, a new thread with data for analysis will be added.
            threads = dict()
            if FGN_ENABLED:
                threads["FGN"] = pool.apply_async(func=predict, args=(
                    available_frames[-FGN_FRAME_COUNT:], fgn_reshape, fgn_transform, fgn_predict,))
            if VRN_ENABLED:
                threads["VRN"] = pool.apply_async(func=predict, args=(
                    available_frames[-VRN_FRAME_COUNT:], vrn_reshape, vrn_transform, vrn_predict,))
            if DIDN_ENABLED:
                threads["DIDN"] = pool.apply_async(func=predict, args=(
                    available_frames[-DIDN_FRAME_COUNT:], didn_reshape, didn_transform, didn_predict,))

            # We wait for each thread to return a prediction result and add the result to the results table,
            # based on which a final verdict will be given.
            predictions = []
            for name, t in threads.items():
                t.wait()
                predictions.append((name, t.get()))

            log_all(ts, CAM_ADDRESS, *predictions)

        else:
            print(f'Frames collected: {len(available_frames)}')
            time.sleep(0.5)


if __name__ == "__main__":
    try:
        main()
    finally:
        print("Exiting...")
        log_stop()
