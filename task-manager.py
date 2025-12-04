from datetime import datetime, timezone
import argparse
import json
import os

parser = argparse.ArgumentParser(description="task management commands")
subparser = parser.add_subparsers(dest="command", required=True)

#Add Parser
add_parser = subparser.add_parser("add", help="adds task name")
add_parser.add_argument("name", help="name of task")
args = parser.parse_args()

def new_task(name):
    file = "tasks.json"

    #File Check
    if os.path.isfile(file) and os.path.getsize(file) > 0:
        with open(file, "r") as f:
            data = json.load(f)
    else:
        data = {"tasks": []}
    
    tasks = {
        "id": len(data["tasks"]) + 1,
        "description": name,
        "status": "todo",
        "createdAt": "",
        "updatedAt": ""
    }
    data["tasks"].append(tasks)
    
    #Load data into JSON File
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

    print("Task created successfully.")

if __name__ == '__main__':
    new_task(args.name)