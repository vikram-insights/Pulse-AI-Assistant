#! 2. VIEW TASKS
                elif todo_choice == 2:
                    tasks = notes_utils.view_notes()
                    if not tasks:
                        print("\n📭 No tasks found.")
                    else:
                        for index, task in enumerate(tasks, start=1):
                            print("-" * 30)
                            print(index)
                            print(f"Task   : {task['task']}")
            
                            #! Dynamic status assignment
                            status = "Completed ✅" if task["completed"] else "Pending⌛"
                            print(f"Status : {status}")
                        print("-" * 30)
