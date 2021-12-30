import json
import os

import jsonschema

image_schema = {
    "type": "object",
    "properties": {"file_name": {"type": "string"}, "id": {"type": "integer"}},
    "required": ["file_name", "id"],
}

segmentation_schema = {
    "type": "array",
    "items": {
        "type": "array",
        "items": {
            "type": "number",
        },
        "additionalItems": False,
    },
    "additionalItems": False,
}

annotation_schema = {
    "type": "object",
    "properties": {
        "image_id": {"type": "integer"},
        "category_id": {"type": "integer"},
        "segmentation": segmentation_schema,
    },
    "required": ["image_id", "category_id", "segmentation"],
}

category_schema = {
    "type": "object",
    "properties": {"name": {"type": "string"}, "id": {"type": "integer"}},
    "required": ["name", "id"],
}

coco_schema = {
    "type": "object",
    "properties": {
        "images": {"type": "array", "items": image_schema, "additionalItems": False},
        "annotations": {
            "type": "array",
            "items": annotation_schema,
            "additionalItems": False,
        },
        "categories": {
            "type": "array",
            "items": category_schema,
            "additionalItems": False,
        },
    },
    "required": ["images", "annotations", "categories"],
}


def read_and_validate_coco_annotation(coco_annotation_path: str) -> (dict, bool):
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
