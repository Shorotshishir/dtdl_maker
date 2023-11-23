import json
from dataclasses import fields
from typing import get_type_hints, Optional, get_origin, Union


def serialize_to_dtdl(instance, version: int, display_name: str, description: str):
    class_data = {
        "@id": f"dtmi:digitaltwins:Basic:{instance.__class__.__name__};{version}",
        "@type": "Interface",
        "@context": ["dtmi:dtdl:context;2"],
        "displayName": f"display_name_v{version}",
        "description": description,
        "contents": []
    }

    type_hints = get_type_hints(instance.__class__)
    for field in fields(instance):
        if get_origin(type_hints[field.name]) is Union:
            field_type = 'Telemetry'
        else:
            field_type = 'Property'
        schema = type_to_dtdl_schema(
            type_hints[field.name].__args__[0] if field_type == 'Telemetry' else type_hints[field.name])
        field_data = {
            "@type": field_type,
            "name": field.name,
            "schema": schema
        }
        if field_type == 'Property' and field.name.endswith('ID'):
            field_data['writable'] = True

        class_data["contents"].append(field_data)

    return json.dumps(class_data, indent=4)


def type_to_dtdl_schema(py_type):
    type_mapping = {
        str: "string",
        int: "integer",
        float: "double",
        bool: "boolean",
        type(None): "string",  # Default schema for NoneType in Optional fields
        type(list): "relationship"
    }
    return type_mapping.get(py_type, "string")
