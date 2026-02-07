import os
import time

todo_list = []


def menu():
    title_menu = f"MENU"
    print("=" * 50)
    print(f"{title_menu:^50}")
    print(f"1. Add Tasks")
    print(f"2. View Tasks")
    print(f"3. Mark Tasks")
    print(f"4. Delete Tasks")
    print(f"5. Exit")
    print("=" * 50)


def add(todo_list):
    while True:
        title = input(f"Enter your task ('q' to return to menu): ")
        if title.strip().lower() == "q":
            break
        completed = input(f"Is that completed ? (Y/n) : ")
        if completed.strip().lower() == "y":
            completed = True
        else:
            completed = False
        task = {"task": title, "completed": completed}
        todo_list.append(task)


def view(todo_list):
    view_title = f"===TODO-LIST==="
    print(f"{view_title:^50}")
    id = 1
    for task in todo_list:
        print(f"{id}. {task['task']} - {task['completed']}")
        id += 1
    print("=" * 50)


def mark(todo_list):
    while True:
        while True:
            index = input(
                f"Enter the task number (1 - {len(todo_list)}) ('q' to return to menu) : "
            )
            try:
                index = int(index) - 1
                break
            except ValueError:
                if index.strip().lower() == "q":
                    break
                else:
                    print(f"Invalid Input, Try again!")
        if index == "q":
            break
        else:
            if todo_list[index]["completed"] == True:
                todo_list[index]["completed"] = False
            elif todo_list[index]["completed"] == False:
                todo_list[index]["completed"] = True


def delete(todo_list):
    while True:
        while True:
            index = input(
                f"Enter the task number to delete  (1 - {len(todo_list)}) ('q' to return to menu) : "
            )
            try:
                index = int(index) - 1
                break
            except ValueError:
                if index.strip().lower() == "q":
                    break
                else:
                    print(f"Invalid Input, Try again!")
        if index == "q":
            break
        else:
            todo_list.pop(index)


while True:
    menu()
    while True:
        mode = input(f"Enter the mode (1 - 5) : ")
        try:
            mode = int(mode)
            if mode < 1 or mode > 5:
                print(f"Please choose from 1 to 5")
            else:
                break
        except ValueError:
            print("Invalid Choice, try again!")
    if mode == 1:
        time.sleep(0.1)
        os.system("cls")
        add(todo_list)
    elif mode == 2:
        view(todo_list)
    elif mode == 3:
        view(todo_list)
        mark(todo_list)
    elif mode == 4:
        view(todo_list)
        delete(todo_list)
    elif mode == 5:
        break

