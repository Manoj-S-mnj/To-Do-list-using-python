print("Learn_code_with_me")
print("\nTo-Do List\n")

TodoList = {
    "Eat": 1,
    "Bath": 0,
    "Study": 1
}

def add_task():
    task = input("Enter the task : ")
    if task in TodoList:
        print("Task is already in the list.")
    else:
        TodoList[task] = 0
        print("Task added successfully.")

def view_all_tasks():
    print("\nAll Tasks:")
    for task, status in TodoList.items():
        status_str = "Completed" if status == 1 else "Pending"
        print(f"- {task} : {status_str}")

def view_completed_tasks():
    print("\nCompleted Tasks:")
    found = False
    for task, status in TodoList.items():
        if status == 1:
            print(f"- {task}")
            found = True
    if not found:
        print("No completed tasks.")

def view_pending_tasks():
    print("\nPending Tasks:")
    found = False
    for task, status in TodoList.items():
        if status == 0:
            print(f"- {task}")
            found = True
    if not found:
        print("No pending tasks.")

def mark_as_complete():
    completed_task = input("Enter the task you completed: ")
    if completed_task in TodoList:
        TodoList[completed_task] = 1
        print("Task marked as completed.")
    else:
        print("Task not found in list.")

def delete_task():
    taskName = input("Enter the task name to delete: ")
    if taskName in TodoList:
        del TodoList[taskName]
        print("Task deleted successfully.")
    else:
        print("Task not found in list.")

while True:
    print("\nSelect from the options below:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    option = input("Enter an option (1–5): ")

    if option == "1":
        add_task()
    elif option == "2":
        print("\n1. View All Tasks")
        print("2. View Completed Tasks")
        print("3. View Pending Tasks")
        optionView = input("Choose an option (1–3): ")

        if optionView == "1":
            view_all_tasks()
        elif optionView == "2":
            view_completed_tasks()
        elif optionView == "3":
            view_pending_tasks()
        else:
            print("Invalid view option.")
    elif option == "3":
        mark_as_complete()
    elif option == "4":
        delete_task()
    elif option == "5":
        print("Exiting from the To-Do List.\nThank you!")
        break
    else:
        print("Invalid option. Please select a number between 1 and 5.")
