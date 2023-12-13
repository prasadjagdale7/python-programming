import json
from datetime import datetime

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("Your To-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']} - {task['due_date']}")

def add_task(tasks, title, due_date):
    new_task = {"title": title, "due_date": due_date}
    tasks.append(new_task)
    print("Task added successfully!")

def update_task(tasks, index, title, due_date):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["title"] = title
        tasks[index - 1]["due_date"] = due_date
        print("Task updated successfully!")
    else:
        print("Invalid task index.")

def delete_task(tasks, index):
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        print(f"Task '{deleted_task['title']}' deleted successfully!")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Display tasks")
        print("2. Add a task")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, title, due_date)
        elif choice == '3':
            display_tasks(tasks)
            index = int(input("Enter the index of the task to update: "))
            title = input("Enter new task title: ")
            due_date = input("Enter new due date (YYYY-MM-DD): ")
            update_task(tasks, index, title, due_date)
        elif choice == '4':
            display_tasks(tasks)
            index = int(input("Enter the index of the task to delete: "))
            delete_task(tasks, index)
        elif choice == '5':
            save_tasks(tasks)
            print("Exiting the To-Do List application. Your tasks are saved.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4/5).")

if __name__ == "__main__":
    main()
