import os

TASKS_FILE = 'tasks.txt'

def load_tasks():
    """Load tasks from the file into a list."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        tasks = file.read().splitlines()
    return tasks

def save_tasks(tasks):
    """Save the list of tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task(task):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task added: "{task}"')

def view_tasks():
    """Display all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def delete_task(task_number):
    """Delete a task by its number."""
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f'Task deleted: "{removed_task}"')
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            try:
                task_number = int(input("Enter the task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
