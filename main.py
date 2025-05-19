from datetime import datetime
import time

print("Welcome to the To-Do List App!")
time.sleep(1)

tasks = []

def save_tasks():
    try:
        with open("tasks.txt", "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(f"{task['text']} | {task['done']} | {task['datetime']}\n")
    except Exception as e:
        print(f"Error saving tasks: {e}")
        time.sleep(1)

def load_tasks():
    global tasks
    tasks = []
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    tasks.append({
                        "text": parts[0],
                        "done": parts[1] == "True",
                        "datetime": parts[2]
                    })
    except Exception as e:
        print(f"Error loading tasks: {e}")
        time.sleep(1)

def show_tasks():
    if not tasks:
        print("Your task list is empty.")
    else:
        print("\n--- TASKS ---")
        for i, task in enumerate(tasks, 1):
            status = "✔" if task["done"] else "✘"
            print(f"{i}. [{status}] {task['text']} ({task['datetime']})")
        print("---------------")
    time.sleep(1.5)

load_tasks() # Load tasks from file at the start

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Task List")
    print("2. Add New Task")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Search Tasks")
    print("7. Save Tasks to File")
    print("8. Exit")
    print("-------------------------")

    choice = input("Choose an option (1-8): ").strip()

    if choice == "1":
        show_tasks()

    elif choice == "2":
        task_text = input("Enter task description: ").strip()
        if not task_text:
            print("Task cannot be empty.")
            time.sleep(1)
            continue
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        tasks.append({"text": task_text, "done": False, "datetime": timestamp})
        print("Task added.")
        time.sleep(1.5)

    elif choice == "3":
        show_tasks()
        try:
            index = int(input("Enter the task number to edit: ")) - 1
            if 0 <= index < len(tasks):
                new_text = input("Enter new task description: ").strip()
                if not new_text:
                    print("Task description cannot be empty.")
                else:
                    tasks[index]["text"] = new_text
                    print("Task updated.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1.5)

    elif choice == "4":
        show_tasks()
        try:
            index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Task '{removed['text']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1.5)

    elif choice == "5":
        show_tasks()
        try:
            index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["done"] = True
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1.5)

    elif choice == "6":
        keyword = input("Enter keyword to search: ").lower().strip()
        print("\n--- SEARCH RESULTS ---")
        found = False
        for i, task in enumerate(tasks, 1):
            if keyword in task["text"].lower():
                status = "✔" if task["done"] else "✘"
                print(f"{i}. [{status}] {task['text']} ({task['datetime']})")
                found = True
        if not found:
            print("No matching tasks found.")
        time.sleep(2)

    elif choice == "7":
        save_tasks()
        print("Tasks saved to 'tasks.txt'.")
        time.sleep(1)

    elif choice == "8":
        save_tasks()
        print("Exiting the app. Goodbye!")
        time.sleep(1)
        break

    else:
        print("Invalid option. Please enter a number between 1 and 8.")
        time.sleep(1.5)

# Final messages
print("Thank you for using the To-Do List App!")
time.sleep(1)
print("Your tasks have been saved.")
time.sleep(0.9)
print("Goodbye!")
time.sleep(0.8)
print("Exiting the program.")
time.sleep(0.7)
print("v1.0 - TNC Group Project")
time.sleep(0.6)
print("Developed by Emre Şahbaz")
time.sleep(0.5)
print("All rights reserved.")
time.sleep(0.4)
print("...")
time.sleep(0.3)
print("..")
time.sleep(0.2)
print(".")
time.sleep(0.1)
print("☺")
