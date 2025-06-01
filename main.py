def to_do_list():
    tasks = []

    while True: 
        print("1 - Add a task")
        print("2 - remove a task")
        print("3 - show all tasks")
        print("4 - Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"Task '{task}' added.")
        elif choice == "2":
            task = input("Enter the task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print(f"Task '{task}' removed.")
            else:
                print(f"Task '{task}' not found.")
        elif choice == "3":
            print("Tasks:")
            for task in tasks:
                print(f"- {task}")
        elif choice == "4":
            print("Exiting the to-do list.")
            break
        else:
            print("Invalid choice. Please try again.")

to_do_list()