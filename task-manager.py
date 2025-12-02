import argparse
import json
import os

#Loads JSON file
def load_json():
    with open("tasks.json", "w") as f:
        data = json.load(f)

#Creates new JSON file
def new_json():
    with open("tasks.json", "w") as f:
        f.write('')



