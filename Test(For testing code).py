#this file is simply used when coding to test snippets from inside the code outside the code
#and to test snippets of other code and how to integrate that into my code
#throughout commits this file (will of had/will have) random code in it they may not ever
#appear in the actuall code although these lines will be all that remains once completed

import tkinter as tk


def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if entry.get() == 'Enter your user name...':
       entry.delete(0, "end") # delete all the text in the entry
       entry.insert(0, '') #Insert blank for user input


root = tk.Tk()

label = tk.Label(root, text="User: ")
label.pack(side="left")

entry = tk.Entry(root, bd=1)
entry.insert(0, 'Enter your user name...')
entry.bind('<FocusIn>', on_entry_click)
entry.pack(side="left")

root.mainloop()