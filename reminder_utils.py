import json

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









        



    