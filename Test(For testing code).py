# this file is simply used when coding to test snippets from inside the code outside the code
# and to test snippets of other code and how to integrate that into my code
# throughout commits this file (will of had/will have) random code in it they may not ever
# appear in the actual code although these lines will be all that remains once completed

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()