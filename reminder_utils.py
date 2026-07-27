import json
from datetime import datetime 

def load_reminders():
    try:
        with open("reminders.json","r") as file:
            reminders = json.load(file)
            return reminders
    except FileNotFoundError:
        return []


def save_reminders(reminders):
    with open("reminders.json","w") as file:
        json.dump(reminders, file)


def add_reminder(title, date, time):
    reminders = load_reminders()
    new_reminder = {
        "title" : title,
        "date" : date,
        "time" : time
    }
    reminders.append(new_reminder)
    save_reminders(reminders)


def delete_reminder(number):
    reminders = load_reminders()
    if reminders:
        if 1 <= number <= len(reminders):
            reminders.pop(number-1)
            save_reminders(reminders)
        else:
            return "Invalid Index!"
    else:
        return "No reminders found"



def view_reminders():
    reminders = load_reminders()
    return reminders




def update_reminder(number, new_task, new_date, new_time):
    reminders = load_reminders()
    if not reminders:
        return "No reminders found"
        
    if not (1 <= number <= len(reminders)):
        return "Invalid Index!"
        
    current_reminder = reminders[number - 1]
    
    
    if new_date != "":
        try:
            datetime.strptime(new_date, "%d-%m-%Y")
        except ValueError:
            return "Invalid date format! Use DD-MM-YYYY."

    
    if new_time != "":
        try:
            datetime.strptime(new_time, "%H:%M")
        except ValueError:
            return "Invalid time format! Use HH:MM."
            
    
    if new_task == "" and new_date == "" and new_time == "":
        return "No changes made."

    if new_task != "":
        current_reminder["title"] = new_task
    if new_date != "":
        current_reminder["date"] = new_date
    if new_time != "":
        current_reminder["time"] = new_time
        
    save_reminders(reminders)
    return "Reminder updated successfully"   
    









        



    