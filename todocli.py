

from todolist import ToDoList

def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Update Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        
        elif choice == '3':
            todo_list.list_tasks()
        
        elif choice == '4':
            old_task = input("Enter the task to update: ")
            new_task = input("Enter the new task: ")
            todo_list.update_task(old_task, new_task)
        
        elif choice == '5':
            print("Exiting the application.")
            break
        
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
