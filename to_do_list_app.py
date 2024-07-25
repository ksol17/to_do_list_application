# User Interface (UI):

def display_menu():
     # Display the main menu options.
    print("\nWelcome to the To-Do List App!")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task(tasks):
    # Add a new task to the list.
    try:
        title = input("Enter a task title: ")
        if not title.strip():
            raise ValueError("Task title cannot be empty.")
        tasks.append({"title": title, "status": "Incomplete"})
        print("Task added!")
    except ValueError as e:
        print(f"Error: {e}")


def view_tasks(tasks):
    # Display all tasks with their titles and statuses.
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['title']} [{task['status']}]")
        

def mark_task_complete(tasks):
    # Mark a specified task as complete.
    if not tasks:
        print("No tasks available to mark as complete.")
        return
    
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["status"]= "Complete"
            print("Task marked as complete!")
                
        else:
            raise IndexError("Invalid task number.")
    except ValueError:
            print("Invalid input. Please enter a number.")
    except IndexError as e:
        print(f"Error: {e}")

def delete_task(tasks):
    # Delete a specified task from the list.
    if not tasks:
        print("No tasks available to delete.")
        return
    
    view_tasks(tasks)
    try: 
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            print("Task deleted!")
        else:
            raise IndexError("Invalid task number. Please enter valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except IndexError as e:
        print(f"Error: {e}")
    finally:
        print("Task deletion process completed.")

def main():
    # Main function to run the To-Do List Application.
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
                
      
if __name__ == "__main__":
    main()



