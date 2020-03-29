import os
import json
import jsonschema

image_schema = {
    "type": "object",
    "properties": {
        "file_name": {
            "type": "string"
            },
        "id": {
            "type": "integer"
            }
    },
    "required": ["file_name", "id"]
}

segmentation_schema = {
    "type": "array",
    "items": {
        "type": "array",
        "items": {
            "type": "number",
            },
        "additionalItems": False
        },
    "additionalItems": False
}

annotation_schema = {
    "type": "object",
    "properties": {
        "image_id": {
            "type": "integer"
            },
        "category_id": {
            "type": "integer"
            },
        "segmentation": segmentation_schema
    },
    "required": ["image_id", "category_id", "segmentation"]
}

category_schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
            },
        "id": {
            "type": "integer"
            }
    },
    "required": ["name", "id"]
}

coco_schema = {
    "type": "object",
    "properties": {
        "images": {
            "type": "array",
            "items": image_schema,
            "additionalItems": False
            },
        "annotations": {
            "type": "array",
            "items": annotation_schema,
            "additionalItems": False
            },
        "categories": {
            "type": "array",
            "items": category_schema,
            "additionalItems": False
            }
    },
    "required": ["images", "annotations", "categories"]
}


def read_and_validate_coco_annotation(
        coco_annotation_path: str) -> (dict, bool):
    """
    Reads coco formatted annotation file and validates its fields.
    """
    try:
        with open(coco_annotation_path) as json_file:
            coco_dict = json.load(json_file)
        jsonschema.validate(coco_dict, coco_schema)
        response = True
    except jsonschema.exceptions.ValidationError as e:
        print("well-formed but invalid JSON:", e)
        response = False
    except json.decoder.JSONDecodeError as e:
        print("poorly-formed text, not JSON:", e)
        response = False

    return coco_dict, response


def create_dir(_dir):
    """
    Creates given directory if it is not present.
    """
    if not os.path.exists(_dir):
        os.makedirs(_dir)


def list_jsons_recursively(directory, silent=True):
    """
    Accepts a folder directory containing json files.
    Returns a list of json file paths present in given directory.
    """
    target_extension_list = ["json"]

    # walk directories recursively and find json files
    abs_filepath_list = []
    relative_filepath_list = []

    # r=root, d=directories, f=files
    for r, _, f in os.walk(directory):
        for file in f:
            if file.split(".")[-1] in target_extension_list:
                abs_filepath = os.path.join(r, file)
                abs_filepath_list.append(abs_filepath)
                relative_filepath = abs_filepath.split(directory)[-1]
                relative_filepath_list.append(relative_filepath)

    number_of_files = len(relative_filepath_list)
    folder_name = directory.split(os.sep)[-1]

    if not silent:
        print("There are {} json files in folder {}.".format(number_of_files, folder_name))

    return relative_filepath_list, abs_filepath_list
