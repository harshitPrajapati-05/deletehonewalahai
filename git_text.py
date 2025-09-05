todos = [
     { id: 1, "title": "Fix bug in user login", "completed": False },
     { id: 2, "title": "Implement password reset", "completed": False },
     { id: 3, "title": "Add 2FA authentication", "completed": False },  
]

def get_todo_by_id(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return None

def add_todo(title):
    new_id = max(todo["id"] for todo in todos) + 1 if todos else 1
    new_todo = { "id": new_id, "title": title, "completed": False }
    todos.append(new_todo)
    return new_todo

def complete_todo(todo_id):
    todo = get_todo_by_id(todo_id)
    if todo:
        todo["completed"] = True
        return todo
    return None


def list_todos():
    return todos

if __name__ == "__main__": 
    print("Current Todos:")
    for todo in list_todos():
        status = "Done" if todo["completed"] else "Pending"
        print(f"{todo['id']}: {todo['title']} - {status}")