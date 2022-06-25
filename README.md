# Violence Recognition System
With use of recurrent neural networks, optical flow, image segmentation and machine learning methods, the trained model is capable of detecting violence on sequence of frames with accuracy of around 88% (with 3 percentage points of error).

**Every module is described separately in module directory.**

## Results
We manage to achieve:
* 88% of accuracy with our solution
* prediction every 1.5 second (with 30 FPS and 4 threads on CPU)
* 3 percentage points of error

## Used image transormations
### [Optical flow with OpenCV](./tools/OpenCV)
![](https://i.imgur.com/B5mFQol.png)

### [Optical flow with RAFT](./tools/RAFT)
![](https://i.imgur.com/IMlqSU9.png)

### [Segmenation with Keras](./tools/Segmentation)
![](https://i.imgur.com/ngDAvEL.png)

## Moduls sample results
### [Module.VRN](./src/Module.VRN)
Violence Recognition Network that uses VGG16 network as base and LSTM as one of the top layers
![](https://i.imgur.com/L2GsPSA.png)

### [Module.FGN](./src/Module.FGN)
Flow Gated Network module based on [Violence Detection project](https://github.com/mchengny/RWF2000-Video-Database-for-Violence-Detection)
![](https://i.imgur.com/GimUqDX.png)

### [Module.DSDN](./src/Module.DSDN)
Dangerous Sound Detection Network module for gunshot detection using VGG16 and transformation to spectrograms
![](https://i.imgur.com/7L6713J.png)

### [Module.DIDN](./src/Module.DIDN)
Dangerous Item Detection Network based trained with [YOLOv3](https://pjreddie.com/darknet/yolo/) and translated to Tensorflow library with usage of [tool used for translation](https://github.com/hunglc007/tensorflow-yolov4-tflite)

## System architecture
### Sequence view
![](https://user-images.githubusercontent.com/36880623/175791360-81831d18-8b34-4e05-b6ee-4438e8a8b39e.png)

### Main system loop process
![image](https://user-images.githubusercontent.com/36880623/175791377-7b0e4d3a-7bd6-4727-8ab4-d6814b9b150e.png)

### Deployment diagram
![image](https://user-images.githubusercontent.com/36880623/175791401-bba7d20e-a545-4a67-8227-5f7d83c701d0.png)

## Dataset
We used [RWF-2000](https://github.com/mchengny/RWF2000-Video-Database-for-Violence-Detection) dataset for training our models.

<p align="left">
  <img width="600" height="500" src="https://i.imgur.com/hCx7gbU.png">
</p>

## Directories structure
* [doc](./doc) – documentation
   * [VRS_-_Praca_Dyplomowa.pdf](./doc/VRS_-_Praca_Dyplomowa.pdf)– system documentation (Polish)
 * [src](./src) – source code
   * [Module.DIDN](./src/Module.DIDN) – Dangerous Item Detection Network, YOLOv3
   * [Module.DSDN](./src/Module.DSDN) – Dangerous Sound Detection Network
   * [Module.FGN](./src/Module.FGN) – Flow Gate Network
   * [Module.Main](./src/Module.Main) – Main module
   * [Module.VRN](./src/Module.VRN) – Violence Recognition Network
   * [Module.Boilerplate](./src/Module.Boilerplate) – Abandoned API boilerplate
 * [tools](./tools) – different tools used in implementation/learning process
 * [docker-compose.yml](./docker-compose.yml) – configure file
 
## System configuration
[docker-compose.yml](./docker-compose.yml) - start file with configuration  options
- `CAM_ADDRESS` - Video stream adress
- `FGN_ENABLED` - Enable/disable FGN module 
- `VRN_ENABLED` - Enable/disable VRN module 
- `DIDN_ENABLED` - Enable/disable DIDN module

## Booting the system
`docker-compose up --build` - Starting up the containers

`localhost:5341`- URL adress for Seq
