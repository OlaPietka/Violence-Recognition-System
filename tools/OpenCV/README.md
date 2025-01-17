# Optical flow with OpenCV
Dataset tranformation using Optical Flow

![](https://i.imgur.com/B5mFQol.png)
## Requirements
You can find all requirements in `requirements-opencv.txt` file

## Required Data
To convert your dataset to Optical Flow, you will need to create directory strucutre as below:

```bash
├── dataset
│   ├── Fight
│   │   ├── 0
│   │   │   ├── frame0.png
│   │   │   ├── frame1.png
│   │   │   ... 
│   │   └── 1
│   │   │   ├── frame0.png
│   │   │   ├── frame1.png
│   │       ... 
│   └── NonFight
│   │   ├── 0
│   │   │   ├── frame0.png
│   │   │   ├── frame1.png
│   │   │   ... 
│   │   └── 1
│   │   │   ├── frame0.png
│   │   │   ├── frame1.png
│   │       ... 
```

## Using
```
python dataset_conv.py --path path//to//dataset// --path_save path//to//save//dir//
```