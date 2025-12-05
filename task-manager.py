from datetime import datetime, timezone
import argparse
import json
import os

#Time
time_now = datetime.now()
neat = time_now.strftime("%Y-%m-%d %H:%M:%S")

#Parser List
parser = argparse.ArgumentParser(description="task management commands")
subparser = parser.add_subparsers(dest="command", required=True)

#Add Parser
add_parser = subparser.add_parser("add", help="adds task name")
add_parser.add_argument("name", help="name of task")

#Update Parser
upd_parser = subparser.add_parser("update", help="update task name")
upd_parser.add_argument("new_id", type=int, help="specific task to be changed")
upd_parser.add_argument("new", type=str, help="new name of task")

#Arguments
args = parser.parse_args()

#Function for "add" parser
def new_task(name):
    file = "tasks.json"

    #File Check
    if os.path.isfile(file) and os.path.getsize(file) > 0:
        with open(file, "r") as f:
            data = json.load(f)
    else:
        data = {"tasks": []}
    
    tasks = {
        "id": len(data["tasks"]),
        "description": name,
        "status": "todo",
        "createdAt": neat,
        "updatedAt": ""
    }
    data["tasks"].append(tasks)
    
    #Load data into JSON File
    with open(file, "w") as f:
        json.dump(data, f, indent=4)
        print("Task created successfully.")

#Function for "update" parser
def new_name(id, new):
    file = "tasks.json"

    #File Check
    if os.path.isfile(file) and os.path.getsize(file) > 0:
        with open(file, "r") as f:
            data = json.load(f)
    else:
        print("Create a task first.")
        return None
        
    data["tasks"][id]["description"] = new
    data["tasks"][id]["updatedAt"] = neat

    with open(file, "w") as f:
        json.dump(data, f, indent=4)
        print('Task successfully updated.')

#Command List
if args.command == "add":
    new_task(args.name)
elif args.command == "update":
    new_name(args.new_id, args.new)
else:
    print("Failed to execute.")
