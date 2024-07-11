import os

# Global variable for the task file
task_file = "tasks.txt"

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

# Function to load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(task_file):
        with open(task_file, 'r') as file:
            for line in file:
                tasks.append(line.strip())
    return tasks

# Function to save tasks to file
def save_tasks(tasks):
    with open(task_file, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Function to add a task
def add_task(tasks):
    task = input("Enter task to add: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

# Function to view all tasks
def view_tasks(tasks):
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks found.")

# Function to update a task
def update_task(tasks):
    view_tasks(tasks)
    if tasks:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Enter new task description: ")
            tasks[index] = new_task
            save_tasks(tasks)
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to update.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            save_tasks(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to delete.")

# Main function to run the task manager
def main():
    tasks = load_tasks()
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the main function
if __name__ == "__main__":
    main()
