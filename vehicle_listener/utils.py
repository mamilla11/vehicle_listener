import json
import jsonschema


VEHICLE_SCHEMA = {
    "type": "object",
    "properties": {
        "component": {
            "type": "string"
        },
        "country": {
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "model": {
            "type": "string"
        },
    },
    "required": [
        "component",
        "country",
        "description",
        "model"
    ]
}


def parse(data: str) -> dict:
    try:
        json_doc = json.loads(data)
    except ValueError:
        return {}

    if not isinstance(json_doc, dict):
        return {}
    return json_doc


def validate(json_doc: dict) -> bool:
    try:
        jsonschema.validate(instance=json_doc, schema=VEHICLE_SCHEMA)
    except jsonschema.exceptions.ValidationError:
        return False

    if not json_doc['country']:
        json_doc['country'] = 'USA'
    return True
