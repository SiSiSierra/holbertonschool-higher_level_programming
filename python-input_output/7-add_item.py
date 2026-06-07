#!/usr/bin/python3
"""Main run file"""
import json, sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

def main():
    """ Add runtime args to json file

    Returns: nothing
    """
    if len(sys.argv) == 1:
        args = []
    else:
        args = sys.argv[1:]
    old_args = load_from_json_file("add_item.json")
    old_args.extend(args)
    save_to_json_file(old_args, "add_item.json")
    return

if __name__ == "__main__":
    main()
