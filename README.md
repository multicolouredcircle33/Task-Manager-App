# 📝 Task Manager Application (TMA)

A **Python-based Task Manager Application** built using **optimized data
structures** to efficiently manage tasks with features like scheduling,
prioritization, undo/redo, and categorization.

This project was developed as part of the **Software Engineering
Bootcamp (Data Structures & Algorithms Module)**.

------------------------------------------------------------------------

## 🚀 Features

1.  **Task List**
    -   Store tasks as objects with attributes: name, category,
        deadline, priority, and status.\
    -   Tasks are managed in dynamic structures (lists and
        dictionaries).
2.  **Task Priority Queue**
    -   Uses a **Heap** (min-heap) to efficiently manage and retrieve
        tasks based on priority (urgent tasks first).
3.  **Undo/Redo Feature**
    -   Implemented using **Stacks** to allow users to undo or redo
        actions such as adding or removing tasks.
4.  **Task Scheduling**
    -   Uses a **Queue (deque)** to manage tasks by deadlines, ensuring
        tasks are executed in the correct order.
5.  **Search Tasks**
    -   Tasks are organized in a **Hash Table** (dictionary) by
        categories/tags for quick searching and categorization.
6.  **Task Hierarchy** *(Planned Extension)*
    -   Could use a **Binary Search Tree (BST)** to represent tasks in a
        hierarchy (e.g., by deadline).
7.  **Recursive Functions** *(Planned Extension)*
    -   Supports future implementation for tasks with subtasks by
        breaking them down recursively.
8.  **Sorting Tasks**
    -   Implements **Insertion Sort** to sort tasks by deadline.\
    -   Can be extended with Merge Sort/Quick Sort for scalability.

------------------------------------------------------------------------

## 📌 Menu Options

When you run the program, you'll get an interactive console menu:

    Enter your choice:
    1. Add Task
    2. View Task
    3. View Tasks by Category
    4. View Priority Tasks
    5. View Sorted Tasks
    6. View Task Schedule
    7. Execute or Delete Task
    8. Undo Last Action
    9. Redo Last Action
    10. Exit

------------------------------------------------------------------------

## 🛠 Technologies & Concepts Used

-   **Python** (Core language)
-   **Data Structures**:
    -   List
    -   Dictionary (Hash Table)
    -   Deque (Queue)
    -   Heap
    -   Stack
-   **Algorithms**:
    -   Insertion Sort (for deadlines)
    -   Heap operations (priority queue)
    -   Undo/Redo logic with stack operations

------------------------------------------------------------------------

## 📂 Project Structure

    task_manager.py   # Main program file

------------------------------------------------------------------------

## ▶️ How to Run

1.  Clone the repository:

    ``` bash
    git clone https://github.com/<your-username>/task-manager-app.git
    cd task-manager-app
    ```

2.  Run the Python program:

    ``` bash
    python task_manager.py
    ```

------------------------------------------------------------------------

## 📸 Sample Output

    Enter your choice:
    1. Add Task
    2. View Task
    ...
    Task successfully added

    Undo: Removed task sweeping
    Redo: Re-added task sweeping

------------------------------------------------------------------------

## 🔮 Future Enhancements

-   GUI interface (Tkinter or PyQt)\
-   Database integration (SQLite/PostgreSQL) for persistent storage\
-   Advanced sorting (Merge Sort, Quick Sort)\
-   Task hierarchy using BST\
-   Subtasks with recursive management

------------------------------------------------------------------------

## 👨‍💻 Author

**Shobanke AbdulAzeez Oladimeji**\
Software Engineering Bootcamp -- Data Structures & Algorithms
