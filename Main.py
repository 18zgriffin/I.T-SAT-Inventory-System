from tkinter import *
from tkinter.messagebox import showinfo

class InventorySystem(Frame):
    # initializes master
    def __init__(self, master):
        Frame.__init__(self, master)
        # names the window
        self.master = master
        master.title("House Inventory - Login")

        # title text at the top window
        self.titleText = Label(master, text="House Inventory - Login", font=("Times", "24", "bold italic"))
        self.titleText.grid(column=1,columnspan=2, row=2, pady=15)

        # info button displays pages information
        self.button_showinfo = Button(master, text="?", command=self.loginInfoWindow)
        self.button_showinfo.grid(column=3, row=1, sticky="e")

        # lable point for username
        self.feetLabel = Label(master, text="Username")
        self.feetLabel.grid(column=1, row=3, padx=(0, 10))
        # point where the username is entered
        self.username = StringVar()
        self.entryValue = Entry(master, textvariable=self.username, width=15)
        self.entryValue.grid(row=4, column=1, sticky="w")

        # lable of password
        self.feetLabel = Label(master, text="Password")
        self.feetLabel.grid(column=2, row=3, padx=(10, 0))
        # point where the pasword is entered
        self.password = StringVar()
        self.entryValue = Entry(master, textvariable=self.password, width=15)
        self.entryValue.grid(row=4, column=2, sticky="e")

        # this runs the submit command making the program check if the username and password is correct
        self.loginButton = Button(master, text="Login", command=self.login)
        self.loginButton.grid(row=5, column=1, columnspan=2, pady=(2.5, 0))

        # button which closes the GUI
        self.close_button = Button(master, text="Exit", command=master.quit)
        self.close_button.grid(row=6, column=3, sticky="e")

        # result of login
        self.attemptResult = StringVar()
        self.feetLabel = Label(master, textvariable=self.attemptResult)
        self.feetLabel.grid(column=1, row=6, columnspan=2)

        self.fillSpace = Label(master, text="           ")
        self.fillSpace.grid(column=0, row=6)

    # the login function, this gets the password and username database files and tests to see if the user input values
    # match any of the logins
    def login(self):
        # assigns the class variables to specific variables for the calculation
        enterusername = self.username.get()
        enterpassword = self.password.get()
        # opens the files and attaches them to a list each
        u = open("usernames.txt", "r")
        ulist = [line.rstrip('\n') for line in u]
        p = open("passwords.txt", "r")
        plist = [line.rstrip('\n') for line in p]

        # tests to see if the login is found in the database
        x = 0
        for i in ulist:
            if enterusername == i:
                if enterpassword == plist[x]:
                    self.user = i
                    self.choice_window()
                    return
            x = x + 1
        self.attemptResult.set("Wrong credentials, try again!")
        return

    # function which runs the information window
    def loginInfoWindow(self):
        showinfo("LoginHelp", "Enter a valid Username and Password into appropriate entry boxes")

    # creates a new window(the choice window) and hides the original root window
    # this choice window allows a user to either proceed to add item page or search item page
    def choice_window(self):
        root.withdraw()
        choicewindow = Toplevel(root)
        self.choicewindow = choicewindow
        choicewindow.title("House Inventory - Selection Page")

        # info button displays pages information
        self.button_showinfo = Button(choicewindow, text="?", command=self.loginInfoWindow, width=2)
        self.button_showinfo.grid(column=3, row=1, sticky="e")

        self.currentUser = Label(choicewindow, text="Current User: "+self.user, font=("Times", "12", "bold italic"))
        self.currentUser.grid(column=1, columnspan=2, row=1)

        self.titleText = Label(choicewindow, text="House Inventory - Selection", font=("Times", "24", "bold italic"))
        self.titleText.grid(column=1, columnspan=2, row=2, pady=15)

        # button which proceeds to add item window
        self.addButton = Button(choicewindow, text="Add item", command=lambda: self.add_window(choicewindow))
        self.addButton.grid(column=1, row=3)

        # this runs the search_window command causing the current window to close and a new search window to open
        self.lookButton = Button(choicewindow, text="Lookup item", command=lambda: self.search_window(choicewindow))
        self.lookButton.grid(column=2, row=3)

        # this runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(choicewindow, text="Logout", command=lambda: self.logout(choicewindow))
        self.logoutButton.grid(row=4, column=0, sticky="w", pady=(15, 0))

        # button which closes the GUI
        self.close_button = Button(choicewindow, text="Exit", command=choicewindow.quit, width=4)
        self.close_button.grid(row=4, column=3, sticky="e", pady=(15, 0))

        # activates if the user ever exits this window using the default [X]
        choicewindow.protocol('WM_DELETE_WINDOW', self.defaultExit)


    def search_window(self, choicewindow):
        choicewindow.withdraw()
        searchwindow = Toplevel(root)
        self.searchwindow = searchwindow
        searchwindow.title("House Inventory - Search Page")

        # info button displays pages information
        self.button_showinfo = Button(searchwindow, text="?", command=self.loginInfoWindow, width=2)
        self.button_showinfo.grid(column=3, row=1, sticky="e")

        #displays currently logged in user
        self.currentUser = Label(searchwindow, text="Current User: "+self.user, font=("Times", "12", "bold italic"))
        self.currentUser.grid(column=1, columnspan=2, row=1)

        # this returns to previous window
        self.backButton = Button(searchwindow, text="Back", command=lambda: self.back(searchwindow, choicewindow))
        self.backButton.grid(row=1, column=0, sticky="w")

        # page title
        self.titleText = Label(searchwindow, text="House Inventory - Search", font=("Times", "24", "bold italic"))
        self.titleText.grid(column=1, columnspan=2, row=2, pady=15)

        self.searchLabel = Label(searchwindow, text="Enter Item Name")
        self.searchLabel.grid(column=1, columnspan=2, row=3)

        self.searchterm = StringVar()
        self.entryValue = Entry(searchwindow, textvariable=self.searchterm, width=15)
        self.entryValue.grid(row=4, column=1, columnspan=2)

        # button which proceeds to add item window
        self.addButton = Button(searchwindow, text="Search")
        self.addButton.grid(column=1, columnspan=2, row=5)

        # button which closes the GUI
        self.close_button = Button(searchwindow, text="Exit", command=choicewindow.quit, width=4)
        self.close_button.grid(row=6, column=3, sticky="e", pady=(15, 0))

        # this runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(searchwindow, text="Logout", command=lambda: self.logout(searchwindow))
        self.logoutButton.grid(row=6, column=0, sticky="w", pady=(15, 0))

        searchwindow.protocol('WM_DELETE_WINDOW', self.defaultExit)

    def add_window(self, choicewindow):
        choicewindow.withdraw()
        addwindow = Toplevel(root)
        self.addwindow = addwindow
        addwindow.title("House Inventory - New Item Page")

        # info button displays pages information
        self.button_showinfo = Button(addwindow, text="?", command=self.loginInfoWindow, width=2)
        self.button_showinfo.grid(column=3, row=1, sticky="e")

        #displays currently logged in user
        self.currentUser = Label(addwindow, text="Current User: "+self.user, font=("Times", "12", "bold italic"))
        self.currentUser.grid(column=1, columnspan=2, row=1)

        # this returns to previous window
        self.backButton = Button(addwindow, text="Back", command=lambda: self.back(addwindow, choicewindow))
        self.backButton.grid(row=1, column=0, sticky="w")

        # page title
        self.titleText = Label(addwindow, text="House Inventory - New Item", font=("Times", "24", "bold italic"))
        self.titleText.grid(column=1, columnspan=2, row=2, pady=15)

        #box in center of add item page
        self.addframe = Frame(addwindow, bd=2, relief="ridge", width=360, height=100)
        self.addframe.grid(row=3, column=0, columnspan=4)
        self.addframe.pack_propagate(0)

        self.newname = StringVar()
        self.newname.set("       <Item Name>")
        self.addframename = Entry(self.addframe, textvariable=self.newname, width=16)
        self.addframename.grid(column=0, row=1, sticky="w")

        self.addframeowner = Label(self.addframe, text="Owner: "+self.user, width=16)
        self.addframeowner.grid(column=1, row=1)

        self.newdescrip = StringVar()
        self.newdescrip.set("<Enter a description of the item>")
        self.addframedescrip = Entry(self.addframe, textvariable=self.newdescrip, width=33)
        self.addframedescrip.grid(column=0, row=2, columnspan=2)

        self.addlocation = StringVar()
        self.addlocation.set("     <Location>")
        self.addframelocation = OptionMenu(self.addframe, self.addlocation, "Lounge", "Bedroom", "Kitchen")
        self.addframelocation.grid(column=1, row=3, sticky="ew")

        self.addframepricelabel = Label(self.addframe, text="Price: ")
        self.addframepricelabel.grid(column=0, row=3, sticky="w")
        self.newPrice = IntVar()
        self.newPrice.set("")
        self.addframeprice = Entry(self.addframe, textvariable=self.newPrice, width=11)
        self.addframeprice.grid(column=0, row=3, sticky="e")

        # button which closes the GUI
        self.close_button = Button(addwindow, text="Exit", command=choicewindow.quit, width=4)
        self.close_button.grid(row=6, column=3, sticky="e")

        # this runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(addwindow, text="Logout", command=lambda: self.logout(addwindow))
        self.logoutButton.grid(row=6, column=0, sticky="w")

        addwindow.protocol('WM_DELETE_WINDOW', self.defaultExit)

    # if the user exits the window while not in the main login window this makes the code is fully shutdown
    def defaultExit(self):
        root.destroy()

    # logs the user out and shows the login screen again
    def logout(self, window):
        window.destroy()
        root.deiconify()

    def back(self, window, prewindow):
        window.destroy()
        prewindow.deiconify()


# starts up the GUI
root = Tk()
gui = InventorySystem(root)
root.mainloop()