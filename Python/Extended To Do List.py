import datetime
def add_task_with_priority(todo_list, task, priority):
    todo_list.append({"task": task, "priority": priority})
    print(f"Task {task} with priority {priority} added successfully!")

def add_task_with_due_date(todo_list, task, due_date):
    todo_list.append({"task": task, "due_date": due_date})
    print(f"Task {task} with due date {due_date} added successfully!")

def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task['task']}' removed successfully!")
    else:
        print("Invalid task index. Try again.")

def mark_task_as_done(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        done_task = todo_list[task_index - 1]["task"]
        todo_list[task_index - 1]["status"] = "Done"
        print(f"Task '{done_task}' marked as done!")
    else:
        print("Invalid task index. Try again.")

def save_to_file(todo_list, filename="todo_list.txt"):
    with open(filename, "w") as file:
        for task_info in todo_list:
            task = task_info["task"]
            status = task_info.get("status", "Not Done")
            file.write(f"{status}: {task}\n")
    print(f"To-do list saved to {filename}.")

def view_tasks(todo_list):
    if not todo_list:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for i, task_info in enumerate(todo_list, start=1):
            task = task_info["task"]
            status = task_info.get("status", "Not Done")
            print(f"{i}. Status: {status}, Task: {task}")

def overdue_tasks(todo_list):
    today = datetime.date.today()
    overdue_tasks = [task_info for task_info in todo_list if task_info.get("due_date") and task_info["due_date"] < today]
    if overdue_tasks:
        print("\nOverdue Tasks:")
        for i, task_info in enumerate(overdue_tasks, start=1):
            task = task_info["task"]
            due_date = task_info["due_date"]
            print(f"{i}. Due Date: {due_date}, Task: {task}")
    else:
        print("\nNo overdue tasks.")

def todo_list_app():
    todo_list = []

    while True:
        print("\nTo-Do List Menu:")
        print("1) Add Task")
        print("2) View Tasks")
        print("3) Remove Task")
        print("4) Mark Task as Done")
        print("5) Save to File")
        print("6) Overdue Tasks")
        print("7) Exit")
        
        choice = input("What do you want to do? ")

        if choice == "1":
            new_task = input("Enter the new task: ")
            priority = input("Enter priority (high, medium, low): ")
            due_date_str = input("Enter due date (YYYY-MM-DD, press Enter for none): ")
            
            if due_date_str:
                due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
                add_task_with_due_date(todo_list, new_task, due_date)
            else:
                add_task_with_priority(todo_list, new_task, priority)

        elif choice == "2":
            view_tasks(todo_list)

        elif choice == "3":
            task_index = int(input("Enter the task index to remove: "))
            remove_task(todo_list, task_index)

        elif choice == "4":
            task_index = int(input("Enter the task index to mark as done: "))
            mark_task_as_done(todo_list, task_index)

        elif choice == "5":
            save_to_file(todo_list)

        elif choice == "6":
            overdue_tasks(todo_list)

        elif choice == "7":
            print("Exiting the To-Do List. Goodbye!")
            save_to_file(todo_list)
            break

        else:
            print("Invalid choice. Try again.")

todo_list_app()
