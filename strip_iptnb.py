#!/usr/bin/env python
import json
import sys

# notebook = sys.stdin.read()
# json_in = json.loads(notebook)

files = sys.argv[1:]

def strip_output_from_cell(cell):
    """
    Takes a notebook cell and removes the "prompt_number" field
    and the "outputs" field.
    """
    if 'outputs' in cell:
        cell['outputs'] = []
    if 'prompt_number' in cell:
        del cell['prompt_number']

def clean_notebook(file):
    notebook = json.loads(open(file, 'r').read())
    cells = notebook['worksheets'][0]['cells'] if 'worksheets' in json_in else json_in['cells']
    for cell in cells:
        strip_output_from_cell(cell)
    json.dump(notebook, open(file, 'w'), sort_keys=True, indent=1, separators=(',', ': '))
