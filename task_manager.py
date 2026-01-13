from datetime import datetime
from collections import deque
import heapq

tasks = []
tasks_category = {}
task_schedule = deque()
priorities = []
undo_stack = []
redo_stack = []
operation = None


class Task: #creating the class for the task object
    def __init__(self, name, category, deadline, priority, status):
        self.name = name
        self.category = category
        self.deadline = deadline
        self.status = status
        self.priority = priority

    def __str__(self): # declaring how the program should print the task object
        return f'Task: {self.name}, Category: {self.category}, Deadline: {self.deadline}, Priority: {self.priority}, Status: {self.status}'


def console_printer(): # function to print the program in the console
    print('Enter your choice: ')
    print('1. Add Task')
    print('2. View Task')
    print('3. View Tasks by Category')
    print('4. View Priority Tasks')
    print('5. View Sorted Tasks')
    print('6. View Task Schedule')
    print('7. Execute or Delete task')
    print('8. Undo Last Action')
    print('9. Redo Last Action')
    print('10. Exit')
    while True:
        try:
            user_input = int(input('Enter your choice(1-9): '))
            break
        except ValueError:
            print('Invalid Input!')
    program_logic(user_input)


def add_task(): # function to add a new task to the program 
    while True:
        try:
            task_name = str(input('What is the name of the task: ')) #making sure the input for task name is a string
            break
        except ValueError:
            print('Invalid input!') # handling valueError 
    category = input('Enter the category(Work/School || Personal || Health & Fitness || Finance & Household || Social & Miscellaneous): ')
    category = category.upper()
    while True:
        deadline = input('Enter the deadline for completing the task(YYYY-MM-DD HH:MM): ')
        try:
            deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M") # verifying if the date the user entered as deadline matches the specified description using the strptime method in the datetime module
            break
        except ValueError:
            print("Invalid format! Please use YYYY-MM-DD HH:MM  (e.g. 2025-08-20 14:30)") #handling valueError
    
    while True:
        try:
            priority = int(input('Enter task priority(a lower number equals higher priority): '))
            break
        except ValueError:
            print('Invalid input! Please enter an integer between 1-100')
    priorities.append(priority)
    status = input('Enter the status(NOT STARTED || IN PROGRESS || COMPLETED): ')
    task= Task(task_name, category, deadline, priority, status) # creating the task object
    tasks.append(task) # adding the task object to tasks list

    if category not in tasks_category: #checking if the newly created task's category alraedy exists
        tasks_category[category] = [] # if it dosen't, create a new one in the dictionary---
        #the dictionary arranges tasks according to their category. each key in the dictionary is a category while the value for that key is a list of the tasks in that category.
    tasks_category[category].append(task) # adding the task to its category
    task_schedule.append(task) # task schedule is a deque which i use to sort tasks acccording to their deadline later in the program. here i'm just adding all the tasks to the deque as they are created so that i can sort them later
    print(' ')
    print('Task successfully added')
    undo_stack.append(('add', task))
    redo_stack.clear()
    operation = 'add'


def view_task(): #function to view all tasks
    if len(tasks) == 0:
        print('\nNo tasks available')
    else:
        print('\nAvailable Tasks:')
        for i, task in enumerate(tasks, 1):# printing the tasks
            print(f'{i}. Task:{task.name}, Category:{task.category}, Deadline:{task.deadline}, Priority:{task.priority}, Status:{task.status}')

def view_tasks_by_category(): # function to view tasks by their category.
    if not tasks_category: # if tasks category is empty, print this.
        print('No categorized tasks yet.')
    else: # if not, for each category in tasks_category, print all the tasks in it.
        for category in tasks_category:
            print(f"\nCategory: {category}")
            for i, task in enumerate(tasks_category[category], 1):
                print(f'{i}. Task:{task.name}, Deadline:{task.deadline}, Priority:{task.priority}, Status:{task.status}')
            print('')


def view_priority_tasks(): #function to view tasks according to priority.
    list_of_tuples = [(task.priority, task) for task in tasks] # create a tuple consisting of the task priority and the task object itself from each task in tasks and append all the tuples to a list called list_of_tuples.
    # i did this so that i can have the entire task object and the task priority (which im going to use in arranging the heap) inside one tuple
    heapq.heapify(list_of_tuples) # then sort all these tuples into a heap using the heapify property.
    rank = 1 
    print('\nTasks according to their priority:')
    while list_of_tuples: # while list_of_tuples is not empty...
        _, task = heapq.heappop(list_of_tuples) # here, _ is serving as a throwaway variable. i use it to discard task.priority as i already have the entire task object to print any property about that task
        print(f'{rank}. Task:{task.name}, Priority:{task.priority}, Deadline:{task.deadline}, Category:{task.category}, Status:{task.status}')
        rank += 1


def insertion_sort_by_dates(array): #here i'm implementing insertion sort algorithm to sort the tasks by their deadline.
    i = 1
    for i in range(1, len(array)):
        key=array[i]
        j = i-1
        while j>=0 and array[j].deadline > key.deadline:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key
    return array


def view_sorted_tasks(x): # function to view tasks sorted by deadline
    sorted_tasks = insertion_sort_by_dates(x) # using the insertion sort function to sort the tasks
    print("\nTasks Sorted by Deadline:\n")
    for i, task in enumerate(sorted_tasks, 1):
        print(f"{i}. Task:{task.name}, Deadline:{task.deadline}, Category:{task.category}, Priority:{task.priority}, Status:{task.status}")
        

def view_task_schedule(): # function to view tasks schedule
    if not task_schedule:
        print("\nNo tasks have been scheduled yet.")
    else:
        insertion_sort_by_dates(task_schedule)
        print("\nTask Schedule:\n")
        print(' ')
        for i, task in enumerate(task_schedule, 1):
            print(f"You are to complete {task.name} before {task.deadline}")


def execute_task():  # function to delete a task
    global operation
    if not task_schedule:
        print('\n No tasks available to execute!')
    else:
        view_task()
        print(' ')
        task = input('Which of these tasks do you want to execute?: ')
        print(' ')
        normalized_task = task.strip().lower()
        found = False
        for t in tasks:
            if t.name.lower() == normalized_task:
                tasks.remove(t)
                if t in task_schedule:
                    index = task_schedule.index(t)
                    task_schedule.remove(t)
                    tasks_category[t.category].remove(t)
                print(f'{t.name} has been successfully executed and removed.')
                found = True

                # --- Undo/Redo tracking ---
                undo_stack.append(("remove", (t, index)))
                redo_stack.clear()
                operation = 'remove'
                break
        if not found:
            print('Task not found!')


def undo_action():
    global operation
    if not undo_stack:
        print('Nothing to undo!')
        return

    action, data = undo_stack.pop()

    if action == "add":  # undo adding a task → remove it
        task = data
        if task in tasks:
            tasks.remove(task)
        if task in task_schedule:
            task_schedule.remove(task)
        if task in tasks_category.get(task.category, []):
            tasks_category[task.category].remove(task)
        print(f'Undo: Removed task {task.name}')
        redo_stack.append(("add", task))
        operation = "undo add"

    elif action == "remove":  # undo removing a task → restore it
        task, index = data
        tasks.append(task)
        task_schedule.insert(index, task)
        tasks_category[task.category].append(task)
        print(f'Undo: Restored task {task.name}')
        redo_stack.append(("remove", (task, index)))
        operation = "undo remove"


def redo_action():
    global operation
    if not redo_stack:
        print('Nothing to redo!')
        return

    action, data = redo_stack.pop()

    if action == "add":  # redo adding a task → re-add it
        task = data
        tasks.append(task)
        task_schedule.append(task)
        tasks_category[task.category].append(task)
        print(f'Redo: Re-added task {task.name}')
        undo_stack.append(("add", task))
        operation = "redo add"

    elif action == "remove":  # redo removing a task → remove again
        task, index = data
        if task in tasks:
            tasks.remove(task)
        if task in task_schedule:
            task_schedule.remove(task)
        if task in tasks_category.get(task.category, []):
            tasks_category[task.category].remove(task)
        print(f'Redo: Removed task {task.name} again')
        undo_stack.append(("remove", (task, index)))
        operation = "redo remove"

        
def program_logic(user_input):
    if user_input == 1:
        add_task()
        print(' ')
        console_printer()
    elif user_input == 2:
        view_task()
        print(' ')
        console_printer()
    elif user_input == 3:
        view_tasks_by_category()
        print(' ')
        console_printer()
    elif user_input == 4:
        view_priority_tasks()
        print(' ')
        console_printer()
    elif user_input == 5:
        tasks_copy = tasks[:]
        view_sorted_tasks(tasks_copy)
        print(' ')
        console_printer()
    elif user_input == 6:
        view_task_schedule()
        print(' ')
        console_printer()
    elif user_input == 7:
        execute_task()
        print(' ')
        console_printer()
    elif user_input == 8:
        undo_action()
        print(' ')
        console_printer()
    elif user_input == 9:
        redo_action()
        print(' ')
        console_printer()
    elif user_input == 10:
        print('Goodbye!')
    else:
        print('Invalid Response!')
        print(' ')
        console_printer()
    
console_printer()
