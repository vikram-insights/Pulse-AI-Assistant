import json


#! LOAD TO DO LIST FUNCTION
def load_todos():
    try:
        with open("todos.json","r") as file:
            todos = json.load(file)
            return todos
    except FileNotFoundError as e:
        return []


#! SAVE FUNCTION
def save_todos(todos):
    with open("todos.json","w") as file:
        json.dump(todos, file)

#! ADD TASK FUNCTION
def add_task(task):
    todos = load_todos()
    new_task = {
        "task" : task,
        "completed" : False
    }

    todos.append(new_task)
    save_todos(todos)


#! VIEW TO DO LIST FUNCTION
def view_todos():
    todos_list = load_todos()
    return todos_list



#! UPDATE TASK FUNCTION
def update_todos(number, new_task):
    todos = load_todos()
    if not todos:
        return False, "No task found"
                
    if not (1 <= number <= len(todos)):
        return False, "Invalid Index!"
                
    current_task = todos[number - 1]

    if new_task == "":
        return False, "No changes made."
        
    if new_task != "":
        current_task["task"] = new_task
            
    save_todos(todos)
    return True, "Task updated successfully ✅"
    
    
    


#! DELETE TASK FUNCTION
def delete_todos(number):
    todos = load_todos()
    if not todos:
        return False, "No no task found"
        
    if not (1 <= number <= len(todos)):
        return False, "Invalid task number!"
        
    todos.pop(number - 1)
    save_todos(todos)
    return True, "Task deleted successfully ✅"


#! SEARCH TASK FUNCTION
def search_todos(task):
    if not task.strip():
        return False, "Please... Enter a task or keyword."
        
    todos = load_todos()
    results = []
    for todo in todos:
        if isinstance(todo, dict) and "task" in todo:
            if task.lower() in todo["task"].lower():
                results.append(todo)
        
            
    if results:
        return True, results
    return False, "No tasks found"




#! MARK COMPLETED
def mark_completed(number, response):
    todos = load_todos()
    if not todos:
        return False, "No tasks found!"


    if not (1 <= number <= len(todos)):
            return False, "Invalid Index!"
    
    if not response.strip():
        return False, "Please... Enter yes!"

    current_task = todos[number - 1]

    if response.strip().lower() != "yes":
        return False, "Invalid input response ❌"
    
    
    current_task["completed"] = True
    save_todos(todos)
    return True, "Marked completed!"









        
