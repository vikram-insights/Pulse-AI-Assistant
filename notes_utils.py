import json

def load_notes():
    try:
        with open("notes.json","r") as file:
            notes = json.load(file)
            return notes
    except FileNotFoundError:
            return []



def save_notes(notes):
    with open("notes.json","w") as file:
         json.dump(notes, file)



def add_notes(title, content):
    notes = load_notes()
    new_note = {
        "title" : title,
        "content" : content
        }
    notes.append(new_note)
    save_notes(notes)


def view_notes():
    notes = load_notes()
    return notes





def delete_notes(number):
    notes = load_notes()
    if not notes:
        return False, "No notes found"
        
    if not (1 <= number <= len(notes)):
        return False, "Invalid Index!"
        
    notes.pop(number - 1)
    save_notes(notes)
    return True, "Note deleted successfully ✅"



def update_notes(number, new_title, new_content):
    notes = load_notes()
    if not notes:
        return False, "No notes found"
            
    if not (1 <= number <= len(notes)):
        return False, "Invalid Index!"
            
    current_note = notes[number - 1]

    if new_title == "" and new_content == "":
        return False, "No changes made."
    
    if new_title != "":
        current_note["title"] = new_title
    if new_content != "":
        current_note["content"] = new_content
        
    save_notes(notes)
    return True, "Notes updated successfully ✅"



def search_notes(title):
    if not title.strip():
        return False, "Please... Enter a title."
        
    notes = load_notes()
    results = []
    for note in notes:
        if title.lower() in note["title"].lower():
            results.append(note)
            
    if results:
        return True, results
    return False, "No notes found"



        


    
