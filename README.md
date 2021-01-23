[![Downloads](https://pepy.tech/badge/labelme2coco/month)](https://pepy.tech/project/labelme2coco)
[![PyPI version](https://badge.fury.io/py/labelme2coco.svg)](https://badge.fury.io/py/labelme2coco)
![CI](https://github.com/fcakyon/labelme2coco/workflows/CI/badge.svg)

# labelme2coco Python Package for Linux/MacOS/Windows
Make your own dataset for object detection/instance segmentation using [labelme](https://github.com/wkentaro/labelme) and transform the format to coco json format 

## Convert LabelMe annotations to COCO format in one step
[labelme](https://github.com/wkentaro/labelme) is a widely used is a graphical image annotation tool that supports classification, segmentation, instance segmentation and object detection formats.
However, widely used frameworks/models such as Yolact/Solo, Detectron, MMDetection etc. requires COCO formatted annotations.

You can use this package to convert labelme annotations to COCO format.

## Getting started
### Installation
```
pip install labelme2coco
```

### Usage
```python
# import package
import labelme2coco

# set directory that contains labelme annotations and image files
labelme_folder = "tests/data/labelme_annot"

# set path for coco json to be saved
save_json_path = "tests/data/test_coco.json"

# convert labelme annotations to coco
labelme2coco.convert(labelme_folder, save_json_path)
```

