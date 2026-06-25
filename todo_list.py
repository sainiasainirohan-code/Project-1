tasks = []

try:
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()

except:
    pass


while True:
    print("""
1. Add Task
2. Delete Task
3. Save Tasks
4. Exit
""")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print(tasks)

        task = input("Enter exact task name to delete: ")

        if task in tasks:
            tasks.remove(task)
            print("Task deleted!")

        else:
            print("Task not found!")

    elif choice == "3":
        with open("tasks.txt", "w") as file:
            file.write("\n".join(tasks))

        print("Tasks saved!")

    elif choice == "4":
        break

    else:
        print("Invalid choice")