#!/usr/bin/python3
"""Module

Functions:
    convert_csv_to_json(filename)
"""
import csv
import json


def convert_csv_to_json(filename):
    """Convert CSV data to JSON

    Params:
        filename: Path of CSV file

    Returns: True if the operation succeeds
    """
    try:
        with open(filename, 'r') as f:
            data = list(csv.DictReader(f))
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except OSError or csv.Error:
        return False
