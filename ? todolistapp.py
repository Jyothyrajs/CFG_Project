from curses.textpad import Textbox
import tkinter as tk
from tkinter import ttk

import utils

todoWindow = tk.Tk()

todoWindow.title("To do List App")
screen_spec = "600x400+50+50"
todoWindow.geometry(screen_spec)

message = tk.Label(todoWindow,text ="My Tasks")
message.pack()

task  = tk.Text(todoWindow,height = 5)
task.pack()

# user_task = task.get('0.0')
def add_task():
    tasks = []
    new_task = task.get('1.0','end')
    utils.add_task(new_task)
    



add_list_button = ttk.Button(todoWindow,text = "Add task")
add_list_button.config(command = add_task)

add_list_button.pack(ipadx=5,ipady=5,expand =True)


todoWindow.mainloop()
