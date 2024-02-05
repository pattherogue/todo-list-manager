# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append({"task": task, "completed": False})
    print("Task '{}' added successfully!".format(task))

# Function to remove a task from the list
def remove_task(task):
    for t in tasks:
        if t["task"] == task:
            tasks.remove(t)
            print("Task '{}' removed successfully!".format(task))
            return
    print("Task '{}' not found in the list.".format(task))

# Function to mark a task as completed
def mark_completed(task):
    for t in tasks:
        if t["task"] == task:
            t["completed"] = True
            print("Task '{}' marked as completed!".format(task))
            return
    print("Task '{}' not found in the list.".format(task))

# Function to display the current to-do list
def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, t in enumerate(tasks, start=1):
            status = "Completed" if t["completed"] else "Not Completed"
            print("{}. {} - {}".format(i, t['task'], status))

# Main loop to manage the to-do list
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Mark a task as completed")
    print("4. Display tasks")
    print("5. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == "1":
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "3":
        task = input("Enter the task to mark as completed: ")
        mark_completed(task)
    elif choice == "4":
        display_tasks()
    elif choice == "5":
        print("Exiting the to-do list manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
