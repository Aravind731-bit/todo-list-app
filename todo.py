FILE_NAME = "tasks.txt"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\n===== YOUR TASKS =====")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()


def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")


def remove_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_num = int(input("Enter task number to remove: "))

        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed}' removed successfully!\n")
        else:
            print("Invalid task number!\n")

    except ValueError:
        print("Please enter a valid number!\n")


def main():
    tasks = load_tasks()

    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            remove_task(tasks)

        elif choice == "4":
            print("Thank you for using To-Do List App!")
            break

        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
