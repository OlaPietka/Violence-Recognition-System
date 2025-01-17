"""
Script responsible for preprocessing and transformations required before sending data to model.
- Ola Piętka
"""
import cv2
import numpy as np


def normalize(data):
    mean = np.mean(data)
    std = np.std(data)
    return (data - mean) / std


def get_optical_flow(video):
    # initialize the list of optical flows
    gray_video = []
    for i in range(len(video)):
        img = cv2.cvtColor(video[i], cv2.COLOR_RGB2GRAY)
        gray_video.append(np.reshape(img, (64, 64, 1)))

    flows = []
    for i in range(0, len(video) - 1):
        # calculate optical flow between each pair of frames
        flow = cv2.calcOpticalFlowFarneback(gray_video[i], gray_video[i + 1], None, 0.5, 3, 15, 3, 5, 1.2,
                                            cv2.OPTFLOW_FARNEBACK_GAUSSIAN)
        # subtract the mean in order to eliminate the movement of camera
        flow[..., 0] -= np.mean(flow[..., 0])
        flow[..., 1] -= np.mean(flow[..., 1])
        # normalize each component in optical flow
        flow[..., 0] = cv2.normalize(flow[..., 0], None, 0, 255, cv2.NORM_MINMAX)
        flow[..., 1] = cv2.normalize(flow[..., 1], None, 0, 255, cv2.NORM_MINMAX)
        # Add into list
        flows.append(flow)
    # Padding the last frame as empty array
    flows.append(np.zeros((64, 64, 2)))

    return np.array(flows, dtype=np.float32)


def normalize_respectively(data):
    data[..., :3] = normalize(data[..., :3])
    data[..., 3:] = normalize(data[..., 3:])

    return data


def set_optical_flow(frames, flows):
    result = np.zeros((len(flows), 64, 64, 5))
    result[..., :3] = frames
    result[..., 3:] = flows

    return result
