import os

TODO_FILE = "todo_list.txt"

def add_task(task):
    with open(TODO_FILE, "a") as file:
        file.write(task + "\n")

def view_tasks():
    if not os.path.exists(TODO_FILE):
        print("No tasks found.")
        return

    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()

    if tasks:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task.strip()}")
    else:
        print("No tasks found.")

def delete_task(task_number):
    if not os.path.exists(TODO_FILE):
        print("No tasks found.")
        return

    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()

    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        with open(TODO_FILE, "w") as file:
            file.writelines(tasks)
        print(f"Task {task_number} deleted.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
