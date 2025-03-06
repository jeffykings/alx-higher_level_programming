#!/usr/bin/python3

"""a script that adds all arguments to a Python list, and then save
them to a file"""

from pathlib import Path
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = Path("add_item.json")

if filename.exists():
    lst = load_from_json_file(filename)

    for value in sys.argv[1:]:
        lst.append(value)
else:
    lst = sys.argv[1:]

save_to_json_file(lst, filename)
