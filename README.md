# To-Do List Application

## Description
A simple console-based To-Do List application developed using Python. This application allows users to manage their daily tasks through a menu-driven interface. Tasks are stored in a text file so that they remain available even after the program is closed.

## Features
- View all tasks
- Add new tasks
- Remove existing tasks
- Save tasks to a file
- Persistent task storage using `tasks.txt`
- Easy-to-use menu-driven interface

## Technologies Used
- Python 3
- Text File Handling

## Project Structure

```
To-Do-List-Application/
│
├── todo.py
├── tasks.txt
└── README.md
```

## How to Run

### Step 1: Clone the Repository

```bash
git clone <repository-url>
```

### Step 2: Navigate to the Project Folder

```bash
cd To-Do-List-Application
```

### Step 3: Run the Program

```bash
py todo.py
```

or

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
Displays all saved tasks.

### Add Task
Allows the user to add a new task to the list.

### Remove Task
Allows the user to remove a task by selecting its number.

### Exit
Saves all tasks and exits the application.

## File Storage

Tasks are stored in:

```text
tasks.txt
```

This ensures that tasks remain available even after closing and reopening the application.

## Author

Aravind

## License

This project is created for educational and learning purposes.
