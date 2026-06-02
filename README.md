# To-Do List Application

## Description

A simple console-based To-Do List application developed using Python. This application allows users to manage their daily tasks through a menu-driven interface. Tasks are stored in a text file, ensuring they remain available even after the program is closed.

## Features

* View all tasks
* Add new tasks
* Remove existing tasks
* Save tasks automatically
* Persistent task storage using `tasks.txt`
* User-friendly menu-driven interface

## Technologies Used

* Python 3
* File Handling

## Project Structure

```text
To-Do-List-Application/
│
├── todo.py
├── tasks.txt
└── README.md
```

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Aravind731-bit/To-Do-List-Application.git
```

### 2. Navigate to the Project Directory

```bash
cd To-Do-List-Application
```

### 3. Run the Application

```bash
py todo.py
```

Or:

```bash
python todo.py
```

## Sample Output

```text
===== TO-DO LIST MENU =====
1. View Tasks
2. Add Task
3. Remove Task
4. Exit

Enter your choice (1-4):
```

## Functionality

### View Tasks

Displays all existing tasks stored in the application.

### Add Task

Allows users to add a new task to the task list.

### Remove Task

Allows users to delete a task by selecting its corresponding number.

### Exit

Saves all tasks and exits the application safely.

## Data Storage

All tasks are stored in:

```text
tasks.txt
```

This ensures that tasks persist between program sessions.

## Author

Aravind

## License

This project is created for educational and learning purposes.
