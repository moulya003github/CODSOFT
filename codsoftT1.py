# task1.py

import json
import os

TASKS_FILE = 'tasks_simple.json'

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description, tasks):
    """Add a new task with a description."""
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)

def list_tasks(tasks):
    """List all tasks with their status."""
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        status = 'Done' if task['completed'] else 'Not Done'
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {status}")

def update_task(task_id, description=None, completed=None, tasks=[]):
    """Update the details of a specific task."""
    for task in tasks:
        if task['id'] == task_id:
            if description is not None:
                task['description'] = description
            if completed is not None:
                task['completed'] = completed
            save_tasks(tasks)
            return True
    return False

def delete_task(task_id, tasks):
    """Delete a specific task."""
    tasks[:] = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)

def main():
    """Main function to drive the to-do list application."""
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Menu")
        print("1. List tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            description = input("Enter task description: ")
            add_task(description, tasks)
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            description = input("Enter new description (leave blank to keep current): ")
            completed = input("Mark as completed? (yes/no, leave blank to keep current): ")
            completed = completed.lower() == 'yes' if completed else None
            if update_task(task_id, description if description else None, completed, tasks):
                print(f"Task ID {task_id} updated.")
            else:
                print("Task not found.")
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id, tasks)
            print(f"Task ID {task_id} deleted.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.")

if __name__ == '__main__':
    main()
