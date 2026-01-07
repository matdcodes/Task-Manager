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

#Delete Parser
del_parser = subparser.add_parser("delete", help="delete a task")
del_parser.add_argument("num", type=int, help="id of task")

#In-Progress Parser
prog_parser = subparser.add_parser("mark-in-progress", help="sets status of task to in-progress")
prog_parser.add_argument("val", type=int, help="id of task")

#Done Parser
done_parser = subparser.add_parser("mark-done", help="sets status of task to done")
done_parser.add_argument("val", type=int, help="id of task")

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
        "updatedAt": neat
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

#Function for "delete" parser
def del_task(num):
    file = "tasks.json"

    #File Check
    if os.path.isfile(file) and os.path.getsize(file) > 0:
        with open(file, "r") as f:
            data = json.load(f)
    else:
        print("Create a task first.")
        return None
    
    data["tasks"].pop(num)
    
    #Reassign id Values
    new_val = 0
    for i in range(len(data["tasks"])):
        if data["tasks"][i]["id"] != new_val:
            data["tasks"][i]["id"] = new_val + 1
            new_val += 1

    with open(file, "w") as f:
        json.dump(data, f, indent=4)
        print('Task successfully updated.')

#Function for "mark-in-progress" parser
def in_prog(val):
    file = "tasks.json"

    #File Check
    if os.path.isfile(file) and os.path.getsize(file) > 0:
        with open(file, "r") as f:
            data = json.load(f)
    else:
        print("Create a task first.")
        return None
    
    data["tasks"][val]["status"] = "in-progress"
    data["tasks"][val]["updatedAt"] = neat

    with open(file, "w") as f:
        json.dump(data, f, indent=4)
        print('Task successfully updated.')

#Function for "mark-done" parser
def mk_done(val):
    file = "tasks.json"

    #File Check
    if os.path.isfile(file) and os.path.getsize(file) > 0:
        with open(file, "r") as f:
            data = json.load(f)
    else:
        print("Create a task first.")
        return None
    
    data["tasks"][val]["status"] = "done"
    data["tasks"][val]["updatedAt"] = neat

    with open(file, "w") as f:
        json.dump(data, f, indent=4)
        print('Task successfully updated.')

#Command List
if args.command == "add":
    new_task(args.name)
elif args.command == "update":
    new_name(args.new_id, args.new)
elif args.command == "delete":
    del_task(args.num)
elif args.command == "mark-in-progress":
    in_prog(args.val)
elif args.command == "mark-done":
    mk_done(args.val)
else:
    print("Failed to execute.")
