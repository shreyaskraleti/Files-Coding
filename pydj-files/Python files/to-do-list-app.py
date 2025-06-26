tasks = []

def show_menu():
    print("\n==== To Do List Menu ====")
    print("1.View Tasks")
    print("2.Add Tasks")
    print("3.Remove Tasks")
    print("4.Exit")
    
def view_tasks():
    if not tasks:
        print("No tasks added yet")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
            
def add_task():
    task = input("Enter a task:")
    tasks.append(task)
    print(f"Task '{task}' added ")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number:")
        
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    
            