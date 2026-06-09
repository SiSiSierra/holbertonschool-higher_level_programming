#!/usr/bin/python3
"""Module

Functions:
    serialise_and_save_to_file(data, filename)
    load_and_deserialize(filename)
"""
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, "w") as f:
        f.write(json.dumps(data))
    pass

def load_and_deserialize(filename):
    with open(filename, "r") as f:
        return json.loads(f.read())
    pass
