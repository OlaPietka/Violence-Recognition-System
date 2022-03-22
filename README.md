# Violence Recognition System
With use of recurrent neural networks, optical flow, image segmentation and machine learning methods, the trained model is capable of detecting violence on sequence of frames with accuracy of around 88% (with 3 percentage points of error).

**Every module is described separately in module directory.**

## Results
We manage to achieve:
* 88% of accuracy with our solution
* prediction every 1.5 second (with 30 FPS and 4 threads on CPU)
* 3 percentage points of error

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
