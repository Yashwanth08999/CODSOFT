import tkinter as tk
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", 'a+') as taskfile:
            taskfile.write(f"{task}\n")
        task_list.append(task)
        listbox.insert(END, task)

def deleteTask():
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")

        listbox.delete(ANCHOR)

def updateTask():
    selected_task = listbox.curselection()
    if selected_task:
        new_task = task_entry.get()
        if new_task:
            index = selected_task[0]
            task_list[index] = new_task
            with open("tasklist.txt", "w") as taskfile:
                for task in task_list:
                    taskfile.write(task + "\n")
            listbox.delete(index)
            listbox.insert(index, new_task)
            task_entry.delete(0, END)

def openTaskFile():
    try:
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            task = task.strip()
            if task:
                task_list.append(task)
                listbox.insert(END, task)
    except FileNotFoundError:
        with open('tasklist.txt', 'w') as file:
            file.close()

# icon
Image_icon = PhotoImage(file="Image/task.png")
root.iconphoto(False, Image_icon)

# top bar
TopImage = PhotoImage(file="Image/topbar.png")
Label(root, image=TopImage).pack()

dockImage = PhotoImage(file="Image/dock.png")
Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)

noteImage = PhotoImage(file="Image/task.png")
Label(root, image=noteImage, bg="#32405b").place(x=330, y=25)

heading = Label(root, text="ALL TASK", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# main frame
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

add_button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
add_button.place(x=300, y=0)

# listbox and scrollbar
frame1 = Frame(root, bd=3, width=400, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=("arial", 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

# delete button
Delete_icon = PhotoImage(file="Image/delete.png")
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

# update button (now a regular button)

update_button = Button(root, text="UPDATE", font="arial 12 bold", width=8, bg="#ffbb5a", fg="#fff", bd=0, command=updateTask)
update_button.place(x=290, y=580)

root.mainloop()
