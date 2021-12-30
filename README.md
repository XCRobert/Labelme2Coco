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
pip install -U labelme2coco
```

### Basic Usage

```python
labelme2coco path/to/labelme/dir
```

```python
labelme2coco path/to/labelme/dir --train_split_rate 0.85
```

### Advanced Usage

```python
# import package
import labelme2coco

# set directory that contains labelme annotations and image files
labelme_folder = "tests/data/labelme_annot"

# set export dir
export_dir = "tests/data/"

# set train split rate
train_split_rate = 0.85

# convert labelme annotations to coco
labelme2coco.convert(labelme_folder, export_dir, train_split_rate)
```

```python
# import functions
from labelme2coco import get_coco_from_labelme_folder, save_json

# set labelme training data directory
labelme_train_folder = "tests/data/labelme_annot"

# set labelme validation data directory
labelme_val_folder = "tests/data/labelme_annot"

# set path for coco json to be saved
export_dir = "tests/data/"

# create train coco object
train_coco = get_coco_from_labelme_folder(labelme_train_folder)

# export train coco json
save_json(train_coco.json, export_dir+"train.json")

# create val coco object
val_coco = get_coco_from_labelme_folder(labelme_val_folder, coco_category_list=train_coco.json_categories)

# export val coco json
save_json(val_coco.json, export_dir+"val.json")
```