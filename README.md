# Task Manager

A simple CLI for managing tasks stored in a JSON file.

## Features
* Creating tasks - `add (description)` 
* Update tasks - `update (description)` 
* Delete tasks - `delete (task id)`
* Mark as In-Progress - `mark-in-progress (task id)`
* Mark as Done - `mark-done (task id)`
* List tasks - `list (filter)`
  * filter: todo, in-progress, done
  * for all, only `list`

## Sample Usage

``` bash
python task-manager.py add "clean room"

python task-manager.py list

python task-manager.py update 0 "clean room and study"

python task-manager.py mark-in-progress 0

python task-manager.py mark-done 0
```
## Inspiration
https://roadmap.sh/projects/task-tracker
