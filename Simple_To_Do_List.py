#import necessary libraries
import tkinter
import tkinter.messagebox
import pickle

#start root app
root = tkinter.Tk()
root.title("To-Do-List by @BradRedondo")

def add_task():
    #gets task from entry
    task = entry_task.get()

    #shows warning if task is empty
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title = "Warning", message = "You must enter a task. ")


def delete_task():
    #deletes selected task, shows warning if not selected.
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

def load_tasks():
    #loads tasks from "tasks.dat", shows warning if not found.
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

def save_tasks():
    #saves tasks in tasks.dat
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

def key_pressed(event):
    #if user presses Enter, add the task
    if event.char == '\r':
        add_task()
    
    #if user presses Backspace, delete the task
    if event.char == '\x08':
        delete_task()
#Bind it so key_pressed is called when, you guessed it, a key is pressed.
root.bind("<Key>",key_pressed)

# Create GUI

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height = 30, width = 150)
listbox_tasks.pack(side = tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side = tkinter.RIGHT, fill = tkinter.Y)


listbox_tasks.config(yscrollcommand = scrollbar_tasks.set)
scrollbar_tasks.config(command = listbox_tasks.yview)

entry_task = tkinter.Entry(root, width = 150)
entry_task.pack()

button_add_task = tkinter.Button(root, text = "Add task",height = 2, width = 130, command = add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text = "Delete task",height = 2, width = 130, command = delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(root, text = "Load tasks",height = 2, width = 130, command = load_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text = "Save tasks",height = 2, width = 130, command = save_tasks)
button_save_tasks.pack()

root.mainloop()