def show_menu():
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View To-Do List")
    print("4. Quit")

def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list[task] = False
    print("Task added successfully!")

def mark_complete(todo_list):
    task = input("Enter the task to mark as complete: ")
    if task in todo_list:
        todo_list[task] = True
        print(f"Task '{task}' marked as complete!")
    else:
        print(f"Task '{task}' not found in the to-do list.")

def view_todo_list(todo_list):
    print("\nTo-Do List:")
    for task, completed in todo_list.items():
        status = "Complete" if completed else "Incomplete"
        print(f"- {task}: {status}")
    print()

def main():
    todo_list = {}

    while True:
        show_menu()

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            mark_complete(todo_list)
        elif choice == '3':
            view_todo_list(todo_list)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
1
if __name__ == "__main__":
    main()