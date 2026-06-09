#!/usr/bin/python3
"""Module

Functions:
    serialise_to_xml(dictionary, xml)
    deserialise_from_xml(filename)
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for item in dictionary:
        ele = ET.Element(item)
        ele.text = dictionary[item]
        root.append(ele)
    tree = ET.ElementTree(root)
    ET.indent(tree)
    with open(filename, 'wb') as f:
        tree.write(f)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    root_dict = {}
    for child in root:
        root_dict[child.tag] = child.text
    return root_dict
