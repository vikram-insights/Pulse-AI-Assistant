import json
from datetime import datetime


#! Load all tasks from JSON
def load_todos():
    try:
        with open("todos.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


#! Save tasks to JSON
def save_todos(todos):
    with open("todos.json", "w") as file:
        json.dump(todos, file, indent=4)


#! Add a new task
def add_task(task, priority):

    todos = load_todos()

    todos.append(
        {
            "task": task,
            "created_at": datetime.now().isoformat(),
            "completed": False,
            "priority": priority,
            "completed_at": None,
        }
    )

    save_todos(todos)


#! Return all tasks
def view_todos():
    return load_todos()


#! Update task or priority
def update_todos(number, new_task, new_priority):

    todos = load_todos()

    if not todos:
        return False, "No tasks found."

    if number < 1 or number > len(todos):
        return False, "Invalid task number."

    task = todos[number - 1]

    #! Remove extra spaces
    new_task = new_task.strip()

    if new_priority:
        new_priority = new_priority.strip()

    #! Nothing entered
    if not new_task and not new_priority:
        return False, "No changes made."

    #! Update task name
    if new_task:
        task["task"] = new_task

    #! Update priority
    if new_priority:
        task["priority"] = new_priority

    save_todos(todos)

    return True, "Task updated successfully ✅"


#! Delete a task
def delete_todos(number):

    todos = load_todos()

    if not todos:
        return False, "No tasks found."

    if number < 1 or number > len(todos):
        return False, "Invalid task number."

    todos.pop(number - 1)

    save_todos(todos)

    return True, "Task deleted successfully ✅"


#! Search task by keyword
def search_todos(keyword):

    keyword = keyword.strip()

    if not keyword:
        return False, "Please enter a keyword."

    todos = load_todos()

    results = []

    for task in todos:
        if keyword.lower() in task["task"].lower():
            results.append(task)

    if results:
        return True, results

    return False, "No matching task found."


def mark_completed(number, response):

    todos = load_todos()

    if not todos:
        return False, "No tasks found."

    if number < 1 or number > len(todos):
        return False, "Invalid task number."

    if response.strip().lower() != "yes":
        return False, "Please enter 'yes'."

    task = todos[number - 1]

    #! Task already completed
    if task["completed"]:
        return False, "Task is already completed."

    #! Mark task as completed
    task["completed"] = True
    task["completed_at"] = datetime.now().isoformat()

    save_todos(todos)

    return True, "Task marked as completed ✅"
