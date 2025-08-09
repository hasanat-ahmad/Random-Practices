def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks(todo_list):
    if not todo_list:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task index. Try again.")

def todo_list_app():
    todo_list = []

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            new_task = input("Enter the new task: ")
            add_task(todo_list, new_task)
        elif choice == "2":
            view_tasks(todo_list)
        elif choice == "3":
            task_index = int(input("Enter the task index to remove: "))
            remove_task(todo_list, task_index)
        elif choice == "4":
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    todo_list_app()
