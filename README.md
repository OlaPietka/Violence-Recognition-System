# Violence Recognition System
Violence Recognition System is thesis project that I've been apart of. We are using variant of neural networks and computer vision techniques to detect violence on sequence of frames.

**Every module is described in separate readme in module directory.**

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
