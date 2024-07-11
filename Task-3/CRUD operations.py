# Function to display menu and get user choice
def display_menu():
    print("Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

# Global list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter task to add: ")
    tasks.append(task)
    print("Task added successfully.")

# Function to view all tasks
def view_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks found.")

# Function to update a task
def update_task():
    view_tasks()
    if tasks:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Enter new task description: ")
            tasks[index] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to update.")

# Function to delete a task
def delete_task():
    view_tasks()
    if tasks:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to delete.")

# Main function to run the task manager
def main():
    while True:
        choice = display_menu()
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the main function
if __name__ == "__main__":
    main()
