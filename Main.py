from tkinter import *
from tkinter.messagebox import showinfo

class ConversionGUI:
    #initializes master
    def __init__(self, master):
        #names the window
        self.master = master
        master.title("House Inventory - Login")

        #title text at the top window
        self.titleText = Label(master, text="House Inventory - Login", font=("Times", "24", "bold italic"))
        self.titleText.grid(column = 0, columnspan = 3, row = 2, pady = 15)

        #lable point for username
        self.feetLabel = Label(master, text="Username")
        self.feetLabel.grid(column=0, row=4)
        #point where the username is entered
        self.username = StringVar()
        self.entryValue = Entry(master, textvariable=self.username, width=15)
        self.entryValue.grid(row=5, column=0, padx=10)

        #lable of password
        self.feetLabel = Label(master, text="Password")
        self.feetLabel.grid(column=1, row=4)
        #point where the pasword is entered
        self.password = StringVar()
        self.entryValue = Entry(master, textvariable=self.password, width=15)
        self.entryValue.grid(row=5, column=1, padx=10)

        #this runs the submit command making the program check if the username and password is correct
        self.submitButton = Button(master, text="Login", command=self.submit)
        self.submitButton.grid(row=6, column=0, columnspan=3)

        #button which closes the GUI
        self.close_button = Button(master, text="Exit", command=master.quit)
        self.close_button.grid(row=7, column=1, sticky="e")

        #result of login
        self.feetLabel = Label(master, text=" ")
        self.feetLabel.grid(column=0, row=7)

        #info button displays pages information
        self.button_showinfo = Button(master, text="?", command=self.loginInfoWindow)
        self.button_showinfo.grid(column=1, row=2, sticky="e", pady=(0, 35))

    #the login function, this gets the password and username database files and tests to see if the user input values
    #match any of the logins
    def submit(self):
        #assigns the class variables to specfic variables for the calculation
        enterusername = self.username.get()
        enterpassword = self.password.get()
        #opens the files and attaches them to a list each
        u = open("usernames.txt", "r")
        ulist = [line.rstrip('\n') for line in u]
        p = open("passwords.txt", "r")
        plist = [line.rstrip('\n') for line in p]

        #tests to see if the login is found in the database
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

    #function which runs the information window
    def loginInfoWindow(hi):
        showinfo("LoginHelp", "Enter a valid Username and Password into appropriate entry boxes")


#starts up the GUI
root = Tk()
gui = ConversionGUI(root)
root.mainloop()