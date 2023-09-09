def show_menu():
    print("Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Exit")

tasks = []

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added!")

    elif choice == "2":
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else " "
            print(f"{index}. [{status}] {task['task']}")

    elif choice == "3":
        if tasks:
            view_choice = int(input("Enter the number of the task to mark as completed: ")) - 1
            if 0 <= view_choice < len(tasks):
                tasks[view_choice]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")
        else:
            print("No tasks to mark as completed.")

    elif choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please choose again.")
