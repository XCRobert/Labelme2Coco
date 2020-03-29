[![PyPI version](https://badge.fury.io/py/labelme2coco.svg)](https://badge.fury.io/py/craft-text-detector)
![CI](https://github.com/fcakyon/labelme2coco/workflows/CI/badge.svg)

## labelme2coco python package for Linux/MacOS/Windows
 **Package maintainer: Fatih Cagatay Akyon**

## Convert LabelMe annotations to COCO format in one step
[Labelme](https://github.com/wkentaro/labelme) is a widely used is a graphical image annotation tool that supports classification, segmentation, isntance segmentation and object detection formats.
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

# conert labelme annotations to coco
labelme2coco.convert(labelme_folder, save_json_path)
```

