#this file is simply used when coding to test snippets from inside the code outside the code
#and to test snippets of other code and how to integrate that into my code
#throughout commits this file (will of had/will have) random code in it they may not ever
#appear in the actuall code although these lines will be all that remains once completed

import tkinter as tk


def center_window(centering):
    # get screen width and height
    screen_width = centering.winfo_screenwidth()
    screen_height = centering.winfo_screenheight()
    width = centering.winfo_width
    height = centering.winfo_height

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    centering.geometry('%dx%d+%d+%d' % (width, height, x, y))


root = tk.Tk()
center_window()
root.mainloop()