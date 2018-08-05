from tkinter import *
from tkinter.messagebox import showinfo
import time

class ConversionGUI:
    #initials master
    def __init__(self, master):
        #names the window
        self.master = master
        master.title("House Inventory - Login")

        #title text at the top window
        self.titleText = Label(master, text="House Inventory - Login", font=("Times", "24", "bold italic"))
        self.titleText.grid(column = 0, columnspan = 3, row = 2, pady = 15)

        # lable of highest number
        self.feetLabel = Label(master, text="Username")
        self.feetLabel.grid(column=0, row=4)
        # entry of the highest number
        self.username = StringVar()
        self.entryValue = Entry(master, textvariable=self.username, width=15)
        self.entryValue.grid(row=5, column=0, padx=10)

        #lable of lowest number
        self.feetLabel = Label(master, text="Password")
        self.feetLabel.grid(column = 1, row = 4)
        #entry of the lowest number
        self.password = StringVar()
        self.entryValue = Entry(master, textvariable=self.password, width = 15)
        self.entryValue.grid(row=5, column = 1, padx = 10)

        #button that checks if
        self.submitButton = Button(master, text="Login", command=self.submit)
        self.submitButton.grid(row=6, column = 0, columnspan = 3)

        #button which closes the GUI
        self.close_button = Button(master, text="Exit", command=master.quit)
        self.close_button.grid(row=7, column=1, sticky = "e")

        #info button
        self.button_showinfo = Button(master, text="?", command=self.loginInfoWindow)
        self.button_showinfo.grid(column = 1, row=2, sticky = "e", pady = (0, 35))

    #calcualate function, gathers all the information given from choices made in the GUI and uses them with other
    #functions to them assign them back to the class and give results
    def submit(self):
        #assigns the class variables to variables for the calculation
        enterusername = self.username.get()
        enterpassword = self.password.get()
        u = open("Usernames.txt", "r")
        ulist = [line.rstrip('\n') for line in u]
        p = open("passwords.txt", "r")
        plist = [line.rstrip('\n') for line in p]
        print(ulist)
        print(plist)

        x = 0
        for i in ulist:
            if enterusername == i:
                print("Good User")
                if enterpassword == plist[x]:
                    print("Good Pass")
                else:
                    print("Bad Pass")

            else:
                print("Bad User")
            x = x + 1
        return

    def loginInfoWindow(hi):
        showinfo("LoginHelp", "Enter a valid Username and Password into appropriate entry boxes")


#starts up the GUI
root = Tk()
gui = ConversionGUI(root)
root.mainloop()