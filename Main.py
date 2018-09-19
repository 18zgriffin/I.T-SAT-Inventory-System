from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import messagebox
import random
import tkinter.ttk as ttk

class InventorySystem(Frame):
    # initializes master
    def __init__(self, master):
        root.option_add("*Font", "arial")
        # allows me to use frames within other windows as frame is declared as the parent window
        Frame.__init__(self, master)
        # names the window
        self.master = master
        master.title("House Inventory - Login")

        # title text at the top window
        self.titleText = Label(master, text="House Inventory - Login", font=("Times", "24", "bold italic"))
        self.titleText.grid(column=1,columnspan=2, row=2, pady=15)

        # info button displays pages information
        self.button_showinfo = Button(master, text="?", command=lambda: self.InfoWindow("master"))
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
        self.entryValue = Entry(master, textvariable=self.password, width=15, show="\u25CF")
        self.entryValue.grid(row=4, column=2, sticky="e")

        # this runs the submit command making the program check if the username and password is correct
        self.loginButton = Button(master, text="Login", command=self.login)
        self.loginButton.grid(row=5, column=1, columnspan=2, pady=(2.5, 0))

        # button which closes the GUI
        self.close_button = Button(master, text="Exit", command=lambda: self.exit_window())
        self.close_button.grid(row=6, column=3, sticky="e")

        # result of login
        self.attemptResult = StringVar()
        self.feetLabel = Label(master, textvariable=self.attemptResult)
        self.feetLabel.grid(column=1, row=6, columnspan=2)

        self.fillSpace = Label(master, text="           ")
        self.fillSpace.grid(column=0, row=6)

        master.protocol('WM_DELETE_WINDOW', lambda: self.exit_window())

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

        # tests to see if the login is found in the database if it is, it logs in if not it returns as incorrect login
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

    # creates a new window(the choice window) and hides the original root window
    # this choice window allows a user to either proceed to add item page, search item page or admin page if they admin
    def choice_window(self):
        # hides the login page and sets up basics of new page
        root.withdraw()
        choicewindow = Toplevel(root)
        self.choicewindow = choicewindow
        choicewindow.title("House Inventory - Selection Page")

        # only appears if the user is the admin
        if self.user == "admin":
            # special button to access admin only settings
            self.adminButton = Button(choicewindow, text="Admin Settings", command=lambda: self.admin_window(choicewindow))
            self.adminButton.grid(row=1, column=0, columnspan=2, sticky="w")

        # info button displays pages information
        self.button_showinfo = Button(choicewindow, text="?", command=lambda: self.InfoWindow("choicewindow"), width=2)
        self.button_showinfo.grid(column=3, row=1, sticky="e")

        # small display showing which user is currently logged in
        self.currentUser = Label(choicewindow, text="Current User: "+self.user, font=("Times", "12", "bold italic"))
        self.currentUser.grid(column=1, columnspan=2, row=1)

        # large title text of what page is, is displayed
        self.titleText = Label(choicewindow, text="House Inventory - Selection", font=("Times", "24", "bold italic"))
        self.titleText.grid(column=1, columnspan=2, row=2, pady=15)

        # button which proceeds to add item window
        self.addButton = Button(choicewindow, text="Add item", command=lambda: self.add_window(choicewindow))
        self.addButton.grid(column=1, row=3)

        # this runs the search_window command causing the current window to close and a new search window to open
        self.lookButton = Button(choicewindow, text="Lookup item", command=lambda: self.search_window(choicewindow))
        self.lookButton.grid(column=2, row=3)

        # this runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(choicewindow, text="Logout", command=lambda: self.logout_window(choicewindow))
        self.logoutButton.grid(row=4, column=0, sticky="w", pady=(15, 0))

        # button which closes the GUI but asks the user if they are sure first
        self.close_button = Button(choicewindow, text="Exit", command=lambda: self.exit_window(), width=4)
        self.close_button.grid(row=4, column=3, sticky="e", pady=(15, 0))

        # activates if the user ever exits this window using the default [X] and asks the user if they are sure
        choicewindow.protocol('WM_DELETE_WINDOW', lambda: self.exit_window())

    # special admin window that an admin can choose to add a user or location from
    def admin_window(self, choicewindow):
        choicewindow.withdraw()
        adminwindow = Toplevel(root)
        self.adminwindow = adminwindow
        adminwindow.title("House Inventory - Admin Options")

        # info button displays pages information
        self.button_showinfo = Button(adminwindow, text="?", command=lambda: self.InfoWindow("adminwindow"), width=2)
        self.button_showinfo.grid(column=3, row=1, sticky="e")

        # small display showing which user is currently logged in
        self.currentUser = Label(adminwindow, text="Current User: "+self.user, font=("Times", "12", "bold italic"))
        self.currentUser.grid(column=1, columnspan=2, row=1)

        # this returns to previous window
        self.backButton = Button(adminwindow, text="Back", command=lambda: self.back(adminwindow, choicewindow))
        self.backButton.grid(row=1, column=0, sticky="w")

        # large title text of what the current page is, is displayed
        self.titleText = Label(adminwindow, text="House Inventory - Admin Options", font=("Times", "24", "bold italic"))
        self.titleText.grid(column=1, columnspan=2, row=2, pady=15)

        # this runs the add user command causing the current window to close and  add new user window to open
        self.adduserButton = Button(adminwindow, text="New User", command=lambda: self.adduser_window(adminwindow))
        self.adduserButton.grid(column=1, row=3)

        # this runs the add location command causing the current window to close and add new location window to open
        self.lookButton = Button(adminwindow, text="New Location", command=lambda: self.addlocation_window(adminwindow))
        self.lookButton.grid(column=2, row=3)

        # this runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(adminwindow, text="Logout", command=lambda: self.logout_window(adminwindow))
        self.logoutButton.grid(row=4, column=0, sticky="w", pady=(15, 0))

        # button which closes the GUI after asking the user if they are sure
        self.close_button = Button(adminwindow, text="Exit", command=lambda: self.exit_window(), width=4)
        self.close_button.grid(row=4, column=3, sticky="e", pady=(15, 0))

        # activates if the user ever exits this window using the default [X] and asks if they are sure
        adminwindow.protocol('WM_DELETE_WINDOW', lambda: self.exit_window())

    # special admin only window which includes options to add a new user to the system
    def adduser_window(self, adminwindow):
        adminwindow.withdraw()
        adduserwindow = Toplevel(root)
        self.adduserwindow = adduserwindow
        adduserwindow.title("House Inventory - New User Page")

        # info button displays pages information
        self.button_showinfo = Button(adduserwindow, text="?", command=lambda: self.InfoWindow("adduserwindow"))
        self.button_showinfo.grid(column=3, row=1, sticky="e")

        # displays currently logged in user
        self.currentUser = Label(adduserwindow, text="Current User: " + self.user, font=("Times", "12", "bold italic"))
        self.currentUser.grid(column=1, columnspan=2, row=1)

        # this returns to previous window
        self.backButton = Button(adduserwindow, text="Back", command=lambda: self.back(adduserwindow, adminwindow))
        self.backButton.grid(row=1, column=0, sticky="w")

        # title text at the top window
        self.titleText = Label(adduserwindow, text="House Inventory - New User Page", font=("Times", "24", "bold italic"))
        self.titleText.grid(column=1, columnspan=2, row=2, pady=15)

        # lable point for new username
        self.feetLabel = Label(adduserwindow, text="New Username")
        self.feetLabel.grid(column=1, row=3, padx=(0, 10))
        # point where the new username is entered
        self.newusername = StringVar()
        self.entryValue = Entry(adduserwindow, textvariable=self.newusername, width=15)
        self.entryValue.grid(row=4, column=1, sticky="w")

        # lable of new password
        self.feetLabel = Label(adduserwindow, text="New Password")
        self.feetLabel.grid(column=2, row=3, padx=(10, 0))
        # point where the new password is entered
        self.newpassword = StringVar()
        self.entryValue = Entry(adduserwindow, textvariable=self.newpassword, width=15)
        self.entryValue.grid(row=4, column=2, sticky="e")

        # runs the newuser command causing program see if username already exist, if not it adds them to the database
        self.savenewuserButton = Button(adduserwindow, text="Add New User", command=lambda: self.newuser())
        self.savenewuserButton.grid(row=5, column=1, columnspan=2, pady=(2.5, 0))

        # button which closes the GUI after asking the user if they are sure
        self.close_button = Button(adduserwindow, text="Exit", command=lambda: self.exit_window())
        self.close_button.grid(row=6, column=3, sticky="e")

        # result of login, says if new user already existed or any other errors
        self.newattemptResult = StringVar()
        self.feetLabel = Label(adduserwindow, textvariable=self.newattemptResult)
        self.feetLabel.grid(column=1, row=6, columnspan=2)

        # a button that runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(adduserwindow, text="Logout", command=lambda: self.logout_window(adduserwindow))
        self.logoutButton.grid(row=6, column=0, sticky="w")

        # runs the default exit if the default exit button is clicked asks user if they are sure before quiting
        adduserwindow.protocol('WM_DELETE_WINDOW', lambda: self.exit_window())

    # special new user command which is run when a new user is being added, this checks if the user exists and if it
    # doesnt it adds the new user if it does it tells the user
    def newuser(self):
        # gets new username and password, opens files and appends them to lists
        username = self.newusername.get()
        password = self.newpassword.get()
        lusers = []
        fusers = open("usernames.txt", "r")
        for line in fusers:
            lusers.append(line.strip("\n"))
        lpasses = []
        fpasses = open("passwords.txt", "r")
        for line in fpasses:
            lpasses.append(line.strip("\n"))
        fusers.close()
        fpasses.close()

        # checks if the new username already exists, if it does it ends this function and returns username exists
        for name in lusers:
            if name == username:
                self.newattemptResult.set("Username already exists, try again")
                return

        # runs when the user doesnt exists, adds the username and password to appropriate lists
        lusers.append(username)
        lpasses.append(password)

        # writes username and password lists back to their appropriate username and password files
        fusers = open("usernames.txt", "w")
        fpasses = open("passwords.txt", "w")
        for line in lusers:
            fusers.write(line)
            fusers.write("\n")
        for line in lpasses:
            fpasses.write(line)
            fpasses.write("\n")

        # sets action to "user" this tells the itemchanged window why it exists and which popup window to display
        self.action = ("user")
        # runs the itemchanged window and uses action to display appropriate popup window
        self.itemchanged_window(self.adduserwindow, self.adminwindow)

    # special admin addlocation window, in this window the admin can add a new location to the database
    def addlocation_window(self, adminwindow):
        adminwindow.withdraw()
        addlocationwindow = Toplevel(root)
        self.addlocationwindow = addlocationwindow
        addlocationwindow.title("House Inventory - New Location Page")

        # info button displays pages information
        self.button_showinfo = Button(addlocationwindow, text="?", command=lambda: self.InfoWindow("addlocationwindow"))
        self.button_showinfo.grid(column=3, row=1, sticky="e")

        # displays currently logged in user
        self.currentUser = Label(addlocationwindow, text="Current User: " + self.user, font=("Times", "12", "bold italic"))
        self.currentUser.grid(column=1, columnspan=2, row=1)

        # this returns to previous window
        self.backButton = Button(addlocationwindow, text="Back", command=lambda: self.back(addlocationwindow, adminwindow))
        self.backButton.grid(row=1, column=0, sticky="w")

        # title text at the top window
        self.titleText = Label(addlocationwindow, text="House Inventory - New Location", font=("Times", "24", "bold italic"))
        self.titleText.grid(column=1, columnspan=2, row=2, pady=15)

        # lable point for new location name
        self.feetLabel = Label(addlocationwindow, text="Location Name")
        self.feetLabel.grid(column=1, row=3, columnspan=2)
        # point where the new location name is entered
        self.newaddlocation = StringVar()
        self.entryValue = Entry(addlocationwindow, textvariable=self.newaddlocation, width=15)
        self.entryValue.grid(row=4, column=1, columnspan=2)

        # this runs the newlocation function command making the program check if location exists if it doesnt it adds it
        self.savenewuserButton = Button(addlocationwindow, text="Add New Location", command=lambda: self.newlocationfunc())
        self.savenewuserButton.grid(row=5, column=1, columnspan=2, pady=(2.5, 0))

        # button which closes the GUI after asking the user if they are sure
        self.close_button = Button(addlocationwindow, text="Exit", command=lambda: self.exit_window())
        self.close_button.grid(row=6, column=3, sticky="e")

        # result of adding new location, may return that the location exists or that there was an error when adding
        self.newattemptResult = StringVar()
        self.feetLabel = Label(addlocationwindow, textvariable=self.newattemptResult)
        self.feetLabel.grid(column=1, row=6, columnspan=2)

        # a button that runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(addlocationwindow, text="Logout", command=lambda: self.logout_window(addlocationwindow))
        self.logoutButton.grid(row=6, column=0, sticky="w")

        # runs the exit window, asking user if they are sure they wish to exit if so then it exits
        addlocationwindow.protocol('WM_DELETE_WINDOW', lambda: self.exit_window())

    # special function that is run when an admin adds a new location to the database
    def newlocationfunc(self):
        # gets the new location, opens locations file and appends it to a list
        location = self.newaddlocation.get()
        fnewlocations = open("locations.txt", "r")
        lnewlocations = []
        for line in fnewlocations:
            lnewlocations.append(line.strip("\n"))

        # checks if the location already exists in the file, if it does it returns attemptresult and ends the function
        # if not the function continues
        for place in lnewlocations:
            if place == location:
                self.newattemptResult.set("Location already exists, try again")
                return

        # appends the newlocation to the list of all locations
        lnewlocations.append(location)

        # writes all the locations back to the locations file
        fnewlocations = open("locations.txt", "w")
        for line in lnewlocations:
            fnewlocations.write(line)
            fnewlocations.write("\n")

        # sets action to "loca" this tells the itemchanged window why it exists and which popup window to display
        self.action = ("loca")
        # runs the itemchanged window and uses action to display appropriate popup window
        self.itemchanged_window(self.addlocationwindow, self.adminwindow)

    # function which contains the add window and its contents, the add window is where the user can add new items to
    # the database
    def add_window(self, choicewindow):
        # hides the previous page and sets up basics of new page
        choicewindow.withdraw()
        addwindow = Toplevel(root)
        self.addwindow = addwindow
        addwindow.title("House Inventory - New Item Page")

        # sets up locations list from a file for add display
        llocations = []
        flocations = open("locations.txt", "r")
        for line in flocations:
            llocations.append(line.strip("\n"))

        # info button displays pages information
        self.button_showinfo = Button(addwindow, text="?", command=lambda: self.InfoWindow("addwindow"), width=2)
        self.button_showinfo.grid(column=3, row=1, sticky="e")

        # displays currently logged in user
        self.currentUser = Label(addwindow, text="Current User: "+self.user, font=("Times", "12", "bold italic"))
        self.currentUser.grid(column=1, columnspan=2, row=1)

        # this returns to previous window
        self.backButton = Button(addwindow, text="Back", command=lambda: self.back(addwindow, choicewindow))
        self.backButton.grid(row=1, column=0, sticky="w")

        # page title
        self.titleText = Label(addwindow, text="House Inventory - New Item", font=("Times", "24", "bold italic"))
        self.titleText.grid(column=1, columnspan=2, row=2, pady=15)

        #### Add Item Page Frame and Contents ####
        # box in center of add item page
        self.addframe = Frame(addwindow, bd=2, relief="ridge", width=360, height=100)
        self.addframe.grid(row=3, column=0, columnspan=4)
        self.addframe.pack_propagate(0)

        # entry box you can input the name of your item into
        self.newname = StringVar()
        self.newname.set("      <Item Name>")
        self.addframename = Entry(self.addframe, textvariable=self.newname, width=16)
        self.addframename.grid(column=0, row=1, sticky="w")
        self.addframename.bind("<Button-1>", self.clear)

        # place that displays who the owner is which is the creator
        self.addframeowner = Label(self.addframe, text="Owner: "+self.user, width=16)
        self.addframeowner.grid(column=1, row=1)

        # entry box the item description can be entered into
        self.newdescrip = StringVar()
        self.newdescrip.set("<Enter a description of the item>")
        self.addframedescrip = Entry(self.addframe, textvariable=self.newdescrip, width=36)
        self.addframedescrip.grid(column=0, row=2, columnspan=2)
        self.addframedescrip.bind("<Button-1>", self.clear)

        # drop down menu the a user can select an item location from
        self.newlocation = StringVar()
        self.newlocation.set("     <Location>")
        self.addframelocation = OptionMenu(self.addframe, self.newlocation, *llocations)
        self.addframelocation.grid(column=1, row=3, sticky="ew")

        # label of price and entry box to enter the price of the item into
        self.addframepricelabel = Label(self.addframe, text="Price:$")
        self.addframepricelabel.grid(column=0, row=3, sticky="w")
        self.newPrice = DoubleVar()
        self.newPrice.set("0")
        self.addframeprice = Entry(self.addframe, textvariable=self.newPrice, width=11)
        self.addframeprice.grid(column=0, row=3, sticky="e")
        self.addframeprice.bind("<Button-1>", self.clear)
        #### End ####

        # this runs the save command causing the program to save the entered item to the database
        self.saveButton = Button(addwindow, text="Save", command=lambda: (self.save(addwindow, choicewindow)))
        self.saveButton.grid(row=6, column=1, columnspan=2, pady=(2.5, 0))

        # button which closes the GUI
        self.close_button = Button(addwindow, text="Exit", command=lambda: self.exit_window(), width=4)
        self.close_button.grid(row=7, column=3, sticky="e")

        # result of adding an item, returns if there was an error with entered information
        self.addResult = StringVar()
        self.feetLabel = Label(addwindow, textvariable=self.addResult)
        self.feetLabel.grid(column=1, row=7, columnspan=2)

        # a button that runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(addwindow, text="Logout", command=lambda: self.logout_window(addwindow))
        self.logoutButton.grid(row=7, column=0, sticky="w")

        # makes the default exit command run, whenever the user presses the default exit button asks user if they are sure
        addwindow.protocol('WM_DELETE_WINDOW', lambda: self.exit_window())

    # save command that is run when a new item is trying to be added
    def save(self, window, prewindow):
        # opens items file and gets all of the users inputted variables
        items = open("items.txt", "r")
        newlocation = self.newlocation.get()
        newdescrip = self.newdescrip.get()
        newname = self.newname.get()
        newuser = self.user
        # tests if the user input a valid float number in as the price, if not it tells user to do so
        try:
            newprice = self.newPrice.get()
        except TclError:
            self.addResult.set("Please input price as a number character eg(1,2...)")
            return

        # checks if all values the user input are valid and that the user actually input a value
        if (newdescrip and newname != 0 and newprice and newdescrip and newname != "" and
                newprice and newdescrip and newname != " " and newname != "       <Item Name>" and newdescrip !=
            "<Enter a description of the item>" and newlocation != "     <Location>") and len(str(newprice)) <= 9:
            # checks if the invalid value of "," is inputed important exception that a user cannot input
            if "," in newdescrip or "," in newname or "," in newuser:
                self.addResult.set("DO NOT INPUT (,) anywhere in a item")
                return
            # checks if the item name already exists in the database
            for item in items:
                if newname == item.split(",")[0]:
                    self.addResult.set("Item name already exists, try again")
                    return

            # adds the item to the items.txt file and runs the itemadded window
            items = open("items.txt", "a")
            items.write("\n")
            items.write(newname + "," + newlocation + "," + str(newprice) + "," + newuser + "," + newdescrip)

            # sets action to "add" which lets the itemchanged window know what to display
            self.action = ("add")
            # runs itemchanged window which displays a popup as determined by the action value
            self.itemchanged_window(window, prewindow)
        else:
            if newprice > 999999:
                # tells the user to input a valid value into all boxes as the test noticed a problem
                self.addResult.set("Please enter a valid value into all boxes")

    # function that contains the searchwindow window
    def search_window(self, window):
        # hides previous window and sets up basics of new page
        window.withdraw()
        searchwindow = Toplevel(root)
        self.searchwindow = searchwindow
        searchwindow.title("House Inventory - Search Page")

        # info button displays pages information
        self.button_showinfo = Button(searchwindow, text="?", command=lambda: self.InfoWindow("searchwindow"), width=2)
        self.button_showinfo.grid(column=3, row=1, sticky="e")

        # displays currently logged in user
        self.currentUser = Label(searchwindow, text="Current User: "+self.user, font=("Times", "12", "bold italic"))
        self.currentUser.grid(column=1, columnspan=2, row=1)

        # this button returns to previous window
        self.backButton = Button(searchwindow, text="Back", command=lambda: self.back(searchwindow, self.choicewindow))
        self.backButton.grid(row=1, column=0, sticky="w")

        # page title
        self.titleText = Label(searchwindow, text="House Inventory - Search", font=("Times", "24", "bold italic"))
        self.titleText.grid(column=1, columnspan=2, row=2, pady=15)

        #### Frame which contains search label and entry box for the search ####
        # box in center of add item page
        self.searchframe = Frame(searchwindow, bd=2, relief="ridge", width=360, height=100)
        self.searchframe.grid(row=3, column=1, columnspan=2)

        # label for what you must enter for the search
        self.searchLabel = Label(self.searchframe, text="Enter Item Name or Related Content")
        self.searchLabel.grid(column=1, columnspan=2, row=3, padx=5, pady=5)

        # entry window that you enter you search term into
        self.searchterm = StringVar()
        self.entryValue = Entry(self.searchframe, textvariable=self.searchterm, width=20)
        self.entryValue.grid(row=4, column=1, columnspan=2, padx=5, pady=(0, 5))
        #### End ####

        # button which activates the search function causing a search in database to be performed and the search results
        # page to appear
        self.searchButton = Button(searchwindow, text="Search", command=lambda: self.search())
        self.searchButton.grid(column=1, columnspan=2, row=5)

        # button which closes the GUI, asking user if they are sure first
        self.close_button = Button(searchwindow, text="Exit", command=lambda: self.exit_window(), width=4)
        self.close_button.grid(row=6, column=3, sticky="e", pady=(15, 0))

        # this runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(searchwindow, text="Logout", command=lambda: self.logout_window(searchwindow))
        self.logoutButton.grid(row=6, column=0, sticky="w", pady=(15, 0))

        # detects if the user pressed the default [X] button and runs the default exit function, ask user if they are sure
        searchwindow.protocol('WM_DELETE_WINDOW', lambda: self.exit_window())

    # this function is run when the user presses search in the search window, it runs the results window and then
    # searches if the term is mentioned in any of the items details, then displaying applicable results
    def search(self):
        # starts up the results window
        self.results_window(self.searchwindow)
        searchterm = self.searchterm.get()
        resultcount = 0

        # gets items file ready to use and sets up list variables
        fitems = open("items.txt", "r")
        lnames = []

        # creates a list of just the names of the items in the database
        for details in fitems:
            splitdetails = details.split(",")
            name = splitdetails[0]
            lnames.append(name.lower())

        # sorts this list using the mergesort function called WordSort
        sortedlist = self.WordSort(lnames)

        # using the sorted list of names a new list is created in the same order but with all the other details included
        # only one of each item name can be in the database because of this. A test for that was added to the add
        # function after this. Items are sorted alphabetically so that they can be easily searched by a user in results
        sorteditems = []
        for sortedvalue in sortedlist:
            fitems = open("items.txt", "r")
            for details in fitems:
                name = details.split(",")[0].lower()
                if name == sortedvalue:
                    sorteditems.append(details.strip("\n"))

        # checks if a search was even input and tells the user on the next page to input an actual value
        if searchterm == " " or searchterm == "":
            self.noresults = Label(self.resultsframe, text="Please input a value")
            self.noresults.grid(row=2, column=0, columnspan=4, sticky="ew")
        else:
            # for every item set it checks if the search term is found in it, if it is then it adds the item and its other
            # details to the results page
            foundlist = []
            for item in sorteditems:
                found = re.search(str(searchterm.lower()), item.lower())
                # this is run if the searchterm is found in the item this adds it to the results
                if found:
                    itemdetails = item.rstrip('\n')
                    itemdetails = itemdetails.split(",")

                    # re-setups variable names to be added to the window of results everytime a new result is found
                    self.resultname = StringVar()
                    self.resultname.set(itemdetails[0])
                    self.resultlocation = StringVar()
                    self.resultlocation.set(itemdetails[1])
                    self.resultvalue = StringVar()
                    self.resultvalue.set(itemdetails[2])
                    self.resultowner = StringVar()
                    self.resultowner.set(itemdetails[3])
                    self.resultdescrip = StringVar()
                    self.resultdescrip.set(itemdetails[4])

                    foundlist.append(itemdetails[0])

                    # adds the new results to the window, dropping down by 1 row every time to avoid them overlapping
                    # also assigns the variables to the current button (default variable method?)
                    self.resultsframename = Button(self.resultsframe, textvariable=self.resultname, command=lambda
                        resultname=self.resultname, resultlocation=self.resultlocation, resultvalue=self.resultvalue,
                        resultowner=self.resultowner, resultdescrip=self.resultdescrip: self.item_window(resultname
                        , resultlocation, resultvalue, resultowner, resultdescrip))
                    self.resultsframename.grid(row=resultcount+2, column=0, padx=(0, 1), sticky="ew", pady=(0,1))
                    self.resultsframelocation = Label(self.resultsframe, textvariable=self.resultlocation)
                    self.resultsframelocation.grid(row=resultcount+2, column=1, padx=(0, 1), sticky="nsew", pady=(0,1))
                    self.resultsframevalue = Label(self.resultsframe, textvariable=self.resultvalue)
                    self.resultsframevalue.grid(row=resultcount+2, column=2, padx=(0, 1), sticky="nsew", pady=(0,1))
                    self.resultsframeowner = Label(self.resultsframe, textvariable=self.resultowner)
                    self.resultsframeowner.grid(row=resultcount+2, column=3, sticky="nsew", pady=(0, 1))
                    # increases resultcount so that next result is displayed down the next row in the frame
                    resultcount += 1

        # if the search term was never found it displays on the window "Sorry no results were found"
            if resultcount == 0:
                self.noresults = Label (self.resultsframe, text="Sorry no results were found")
                self.noresults.grid(row=2, column=0, columnspan=4, sticky="ew")

    # function the contains the results window which displays results found in the search window function
    def results_window(self, searchwindow):
        # hides previous window and sets up basics of new one
        searchwindow.withdraw()
        resultswindow = Toplevel(root)
        self.resultswindow = resultswindow
        resultswindow.title("House Inventory - Search Results")

        # info button displays pages information
        self.button_showinfo = Button(resultswindow, text="?", command=lambda: self.InfoWindow("resultswindow"), width=2)
        self.button_showinfo.grid(column=3, row=1, sticky="e")

        # displays currently logged in user
        self.currentUser = Label(resultswindow, text="Current User: "+self.user, font=("Times", "12", "bold italic"))
        self.currentUser.grid(column=1, columnspan=2, row=1)

        # this button returns to previous window
        self.backButton = Button(resultswindow, text="Back", command=lambda: self.back(resultswindow, searchwindow))
        self.backButton.grid(row=1, column=0, sticky="w")

        # page title
        self.titleText = Label(resultswindow, text="House Inventory - Results", font=("Times", "24", "bold italic"))
        self.titleText.grid(column=1, columnspan=2, row=2, pady=15)

        #### Frame containing search results ####
        # box in center of add item page
        self.resultsframe = Frame(resultswindow, bd=2, relief="ridge", bg="black")
        self.resultsframe.grid(row=3, column=0, columnspan=6)

        # basic titles for each column of the search results
        self.resultsframeidname = Label(self.resultsframe, text="Item Name")
        self.resultsframeidname.grid(row=1, column=0, padx=(0, 1), pady=(0,1), sticky="we")
        self.resultsframeidlocation = Label(self.resultsframe, text="   Location   ")
        self.resultsframeidlocation.grid(row=1, column=1, padx=(0, 1), sticky="we")
        self.resultsframeidvalue = Label(self.resultsframe, text="  Value  ")
        self.resultsframeidvalue.grid(row=1, column=2, padx=(0, 1), sticky="we")
        self.resultsframeidowner = Label(self.resultsframe, text="  Owner  ")
        self.resultsframeidowner.grid(row=1, column=3, sticky="we")
        #### Frame END ####

        # button which closes the GUI, after asking user if they are sure
        self.close_button = Button(resultswindow, text="Exit", command=lambda: self.exit_window(), width=4)
        self.close_button.grid(row=7, column=3, sticky="e")

        # this runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(resultswindow, text="Logout", command=lambda: self.logout_window(resultswindow))
        self.logoutButton.grid(row=7, column=0, sticky="w")

        # if the user selecs the default [X] to exit it runs the default exit window, asks user if they are sure they do
        resultswindow.protocol('WM_DELETE_WINDOW', lambda: self.exit_window())

    # item window that is displayed when an item is clicked on, it displays an items details and options to do with it
    def item_window(self, itemname, itemlocation, itemvalue, itemowner, itemdescrip):
        # hides the previous page and sets up basics of new page
        self.resultswindow.withdraw()
        itemwindow = Toplevel(root)
        self.itemwindow = itemwindow
        itemwindow.title("House Inventory - View Item Page")
        # gets information of selected item
        itemname = itemname.get()
        itemlocation = itemlocation.get()
        itemvalue = itemvalue.get()
        itemowner = itemowner.get()
        itemdescrip = itemdescrip.get()

        # info button displays pages information
        self.button_showinfo = Button(itemwindow, text="?", command=lambda: self.InfoWindow("itemwindow"), width=2)
        self.button_showinfo.grid(column=3, row=1, sticky="e")

        # displays currently logged in user
        self.currentUser = Label(itemwindow, text="Current User: " + self.user, font=("Times", "12", "bold italic"))
        self.currentUser.grid(column=1, columnspan=2, row=1)

        # this returns to previous window
        self.backButton = Button(itemwindow, text="Back", command=lambda: self.back(itemwindow, self.resultswindow))
        self.backButton.grid(row=1, column=0, sticky="w")

        # page title
        self.titleText = Label(itemwindow, text="House Inventory - View Item", font=("Times", "24", "bold italic"))
        self.titleText.grid(column=1, columnspan=2, row=2, pady=15)

        #### Add Item Page Frame and Contents ####
        # box in center of add item page
        self.itemframe = Frame(itemwindow, bd=2, relief="ridge")
        self.itemframe.grid(row=3, column=0, columnspan=4)
        self.itemframe.pack_propagate(0)

        # label of the items name
        self.itemframename = Label(self.itemframe, text=itemname, width=16, relief="ridge")
        self.itemframename.grid(column=0, row=1, pady=1, padx=1)

        # place that displays who the owner is
        self.itemframeowner = Label(self.itemframe, text="Owner: " + str(itemowner), width=16, relief="ridge")
        self.itemframeowner.grid(column=1, row=1, padx=1)

        # label which contains the items description
        self.itemframedescrip = Label(self.itemframe, text=itemdescrip, width=33, relief="ridge")
        self.itemframedescrip.grid(column=0, row=2, columnspan=2, pady=2)

        # label that displays the items location
        self.itemframelocation = Label(self.itemframe, text=itemlocation, relief="ridge")
        self.itemframelocation.grid(column=1, row=3, sticky="ew")

        # label of price and item value
        self.itemframeprice = Label(self.itemframe, text="Price:$"+itemvalue)
        self.itemframeprice.grid(column=0, row=3, pady=1)
        #### End ####

        # this checks if the user is authorised to edit or remove the item, if they are they get access to the proper
        # functions of the buttons, if the user isnt then the buttons tell the user they have no permission
        if self.user == itemowner or self.user == "admin":
            # adds the edit button that when pressed runs the edit window
            self.editButton = Button(itemwindow, text="Edit", width=6, command=lambda: self.edit_window(itemwindow,
                itemname, itemlocation, itemvalue, itemowner, itemdescrip))
            self.editButton.grid(row=6, column=1, pady=(2.5, 0))

            # adds the remove button that runs the remove function
            self.removeButton = Button(itemwindow, text="Remove", command=lambda: self.remove_window(itemwindow,
                itemname, itemlocation, itemvalue, itemowner, itemdescrip))
            self.removeButton.grid(row=6, column=2, pady=(2.5, 0))
        else:
            # runs a special popup telling the user they do not have permission to edit the item
            self.editButton = Button(itemwindow, text="Edit", command=lambda: messagebox.showinfo("Permission",
                "You dont have permission to do that"))
            self.editButton.grid(row=6, column=1, pady=(2.5, 0))

            # runs a special popup telling the user they do not have permission to remove the item
            self.removeButton = Button(itemwindow, text="Remove", command=lambda: messagebox.showinfo("Permission",
                "You dont have permission to do that"))
            self.removeButton.grid(row=6, column=2, pady=(2.5, 0))

        # button which closes the GUI, asks user if they are sure first
        self.close_button = Button(itemwindow, text="Exit", command=lambda: self.exit_window(), width=4)
        self.close_button.grid(row=7, column=3, sticky="e")

        # a button that runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(itemwindow, text="Logout", command=lambda: self.logout_window(itemwindow))
        self.logoutButton.grid(row=7, column=0, sticky="w")

        # makes the default exit command run, whenever the user presses the default exit button, asks user if sure first
        itemwindow.protocol('WM_DELETE_WINDOW', lambda: self.exit_window())

    # edit window contains the previous pages item details but with the ability to edit and save the new ones
    def edit_window(self, itemwindow, itemname, itemlocation, itemvalue, itemowner, itemdescrip):
        # hides the previous page and sets up basics of new page
        itemwindow.withdraw()
        editwindow = Toplevel(root)
        self.editwindow = editwindow
        editwindow.title("House Inventory - Edit Item Page")

        # opens locations and users files and appends them to lists for dropdown menu selections
        llocations = []
        flocations = open("locations.txt", "r")
        for line in flocations:
            llocations.append(line.strip("\n"))
        lusers = []
        fusers = open("usernames.txt", "r")
        for line in fusers:
            lusers.append(line.strip("\n"))

        # info button displays pages information
        self.button_showinfo = Button(editwindow, text="?", command=lambda: self.InfoWindow("editwindow"), width=2)
        self.button_showinfo.grid(column=3, row=1, sticky="e")

        # displays currently logged in user
        self.currentUser = Label(editwindow, text="Current User: "+self.user, font=("Times", "12", "bold italic"))
        self.currentUser.grid(column=1, columnspan=2, row=1)

        # this returns to previous window
        self.backButton = Button(editwindow, text="Back", command=lambda: self.back(editwindow, itemwindow))
        self.backButton.grid(row=1, column=0, sticky="w")

        # page title
        self.titleText = Label(editwindow, text="House Inventory - Edit Item", font=("Times", "24", "bold italic"))
        self.titleText.grid(column=1, columnspan=2, row=2, pady=15)

        #### Add Item Page Frame and Contents ####
        # box in center of edit item page
        self.editframe = Frame(editwindow, bd=2, relief="ridge", width=360, height=100)
        self.editframe.grid(row=3, column=0, columnspan=4)
        self.editframe.pack_propagate(0)

        # entry box containing the item name which you can change
        self.editname = StringVar()
        self.editname.set(itemname)
        self.editframename = Entry(self.editframe, textvariable=self.editname, width=16)
        self.editframename.grid(column=0, row=1, sticky="w")

        # place that displays who the owner is and they option to change it through a dropdown menu
        self.editframeownerlabel = Label(self.editframe, text=" Owner:")
        self.editframeownerlabel.grid(column=1, row=1, sticky="w")
        self.edituser = StringVar()
        self.edituser.set(itemowner)
        self.editframeowner = OptionMenu(self.editframe, self.edituser, *lusers)
        self.editframeowner.config(width=10)
        self.editframeowner.grid(column=1, row=1, sticky="e")

        # entry box the item description is in, this can be changed
        self.editdescrip = StringVar()
        self.editdescrip.set(itemdescrip)
        self.editframedescrip = Entry(self.editframe, textvariable=self.editdescrip, width=36)
        self.editframedescrip.grid(column=0, row=2, columnspan=2)

        # drop down menu currently displaying items location, it can be changed to another value in the dropdown menu
        self.editlocation = StringVar()
        self.editlocation.set(itemlocation)
        self.editframelocation = OptionMenu(self.editframe, self.editlocation, *llocations)
        self.editframelocation.config(width=16)
        self.editframelocation.grid(column=1, row=3, sticky="ew")

        # entry box displaying items current price, this can be changed through integer entry
        self.editframepricelabel = Label(self.editframe, text="Price:$")
        self.editframepricelabel.grid(column=0, row=3, sticky="w")
        self.editPrice = IntVar()
        self.editPrice.set(itemvalue)
        self.editframeprice = Entry(self.editframe, textvariable=self.editPrice, width=11)
        self.editframeprice.grid(column=0, row=3, sticky="e")
        #### End ####

        # this runs the saveedit command causing the program to save the edited item to the database
        self.saveeditButton = Button(editwindow, text="Save", command=lambda: (self.saveedit(editwindow, itemwindow,
            itemname, itemdescrip, itemowner, itemvalue, itemlocation)))
        self.saveeditButton.grid(row=6, column=1, columnspan=2, pady=(2.5, 0))

        # button which closes the GUI, asks user if they are sure first
        self.close_button = Button(editwindow, text="Exit", command=lambda: self.exit_window(), width=4)
        self.close_button.grid(row=7, column=3, sticky="e")

        # result of item edit, changes if there was something wrong the input edits
        self.editResult = StringVar()
        self.feetLabel = Label(editwindow, textvariable=self.editResult)
        self.feetLabel.grid(column=1, row=7, columnspan=2)

        # a button that runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(editwindow, text="Logout", command=lambda: self.logout_window(editwindow))
        self.logoutButton.grid(row=7, column=0, sticky="w")

        # makes the default exit command run, whenever the user presses the default exit button, asks user if sure first
        editwindow.protocol('WM_DELETE_WINDOW', lambda: self.exit_window())

    # run when a user tries to save an editted item, it will save the new one to the file and remove the original, after
    # check if input values are valid
    def saveedit(self, window, prewindow, preitemname, preitemdescrip, preitemowner, preitemvalue, preitemlocation):
        # opens items file and gets all of the users inputted variables
        ritems = open("items.txt", "r")
        editlocation = self.editlocation.get()
        editdescrip = self.editdescrip.get()
        editname = self.editname.get()
        edituser = self.edituser.get()
        editprice = self.editPrice.get()
        cfline = []
        currentline = 0
        # checks if all values the user input are valid. Also identifies where in the file the item to be changed is. It
        # then replaces that item with the new edit in a list
        for line in ritems:
            # adds every item to a list and checks if its the one to be changed
            cline = line.strip("\n").split(",")
            cfline.append(line.strip("\n"))
            # checks if current line matches one to be changed
            if (preitemname == cline[0] and preitemlocation == cline[1] and preitemvalue == cline[2] and preitemowner ==
                    cline[3] and preitemdescrip == cline[4]):
                # checks if inputs are valid
                if (editdescrip and editname != 0 and editprice and editdescrip and editname != "" and
                        editprice and editdescrip and editname != " " and editname != "       <Item Name>" and
                        editdescrip != "<Enter a description of the item>" and editlocation != "      <Location>"
                        and editprice <= 999999):
                    if "," in editdescrip or "," in editname or "," in edituser:
                        self.editResult.set("DO NOT INPUT (,) anywhere in a item")
                        return
                    # if the input values are valid and the loop is currently on the one to be changed, it changes the
                    # item in the list to the appropriate editted item
                    cfline[currentline] = (editname + "," + editlocation + "," + str(editprice) + "," + edituser + "," +
                            editdescrip)
                else:
                    # tells the user to input a valid value into all boxes as the test noticed a problem
                    self.editResult.set("Please enter a valid value into all boxes")
                    return
            currentline += 1
        # writes the new list to the file
        witems = open("items.txt", "w")
        for x in cfline:
            witems.write(x)
            witems.write("\n")

        # sets action to edit so that itemchange window will be able to determine which popup to display
        self.action = "edit"
        # runs the itemchanged window uses the value of action to determine which popup to display
        self.itemchanged_window(window, self.searchwindow)

    # remove window popup that asks the user if they are sure they want to remove an item, if yes then it removes it
    def remove_window(self, prewindow, itemname, preitemlocation, preitemvalue, preitemowner, preitemdescrip):
        # creates popup window asking if the user is sure they want to remove the item
        if messagebox.askyesno("Remove", "Are you sure you want to remove the item \n"+itemname):
            # opens items file
            ritems = open("items.txt", "r")
            cfline = []
            currentline = 0

            for line in ritems:
                # adds every item to a list and checks if its the one to be changed
                cline = line.strip("\n").split(",")
                cfline.append(line.strip("\n"))
                # checks if current line matches one to be remove and if it is then it removes it
                if (itemname == cline[0] and preitemlocation == cline[1] and preitemvalue == cline[2] and preitemowner
                == cline[3] and preitemdescrip == cline[4]):
                    cfline.remove(itemname+","+preitemlocation+","+preitemvalue+","+preitemowner+","+preitemdescrip)
                currentline += 1

            # writes the list without the removed item back to the items file
            witems = open("items.txt", "w")
            for x in cfline:
                witems.write(x)
                witems.write("\n")
            # sets action to "remove" for the use of itemchange window
            self.action = "remove"
            # creates a popup based on the recieve value of action
            self.itemchanged_window(prewindow, self.searchwindow)

    # popup window that happens when something is done with an item (added, edited, removed) or user/location added
    def itemchanged_window(self, window, prewindow):
        # destroys previous window and sets up new pop up window
        window.destroy()
        # checks which action value was created(determined by previous function run) and creates appropriate popup window
        # which once exited goes back to earlier window
        if self.action == "add":
            if messagebox.showinfo("Item Added", "Item Added Successfully"):
                self.action = None
                self.back(window, prewindow)
        elif self.action == "edit":
            if messagebox.showinfo("Item Edited", "Item Edited Successfully"):
                self.action = None
                self.back(window, prewindow)
        elif self.action == "remove":
            if messagebox.showinfo("Item Removed", "Item Removed Successfully"):
                self.action = None
                self.back(window, prewindow)
        elif self.action == "user":
            if messagebox.showinfo("User Added", "New User Added Successfully"):
                self.action = None
                self.back(window, prewindow)
        elif self.action == "loca":
            if messagebox.showinfo("Location Added", "New Location Added Successfully"):
                self.action = None
                self.back(window, prewindow)

    # function which runs the information window
    def InfoWindow(self, window):
        # opens information files and writes their contents to a separate lists
        i = open("Info.txt", "r")
        ilist = [line.rstrip('\n') for line in i]
        ititles = open("InfoTitles.txt", "r")
        ititleslist = [line.rstrip('\n') for line in ititles]
        # checks which window the user is on and then assigns a int value that corresponds to the information for the
        # current window out of the lists
        if window == "master":
            self.title = 0
            self.information = 0
        elif window == "choicewindow":
            self.title = 1
            self.information = 1
        elif window == "searchwindow":
            self.title = 2
            self.information = 2
        elif window == "addwindow":
            self.title = 3
            self.information = 3
        elif window == "resultswindow":
            self.title = 4
            self.information = 4
        elif window == "itemwindow":
            self.title = 5
            self.information = 5
        elif window == "editwindow":
            self.title = 6
            self.information = 6
        elif window == "adminwindow":
            self.title = 7
            self.information = 7
        elif window == "adduserwindow":
            self.title = 8
            self.information = 8
        elif window == "addlocationwindow":
            self.title = 9
            self.information = 9
        # runs the showinfo which that displays the appropriate information
        showinfo(ititleslist[self.title], ilist[self.information])

    # if the user presses either of the exit buttons, default or the one labeled exit. this window pops up, and if the
    # user selects yes it destroys the root and closes everything, if the user presses no it just closes the popup
    def exit_window(self):
        if messagebox.askyesno("Quit", "Are you sure you want to quit"):
            root.destroy()

    # runs a logout popup window that asks the user if they really want to log out, if yes the user is returned to the
    # login window, login variables are set to nothin and other windows are destroyed if no then it closes the popup
    def logout_window(self, window):
        if messagebox.askyesno("Logout", "Are you sure you want to logout"):
            self.username.set("")
            self.password.set("")
            self.attemptResult.set("")
            root.deiconify()
            window.destroy()

    # This is the complex algorithm
    ## Mergesort Based function based upon Mergesort.py but Stuart Thornhill created on 2/8/2018 ##
    # Merge sort function, recursively sorts 2 lists to return a fully sorted list in the end
    # Used to sort results of a search into alphabetical order so that results display is easier to understand
    def WordSort(self, sortinglist):
        # Check to see if the list is only a single item, if so return the single item list
        if (len(sortinglist) <= 1):
            return sortinglist

        # Setting up initial variable for splitting lists
        listLength = len(sortinglist)
        index = 0
        list1 = []
        list2 = []

        # Loop that splits 1 list into 2 lists of roughly equal length
        while index < listLength:
            if (index + 1 <= int((listLength) / 2)):
                list1.append(sortinglist[index])
            else:
                list2.append(sortinglist[index])
            index += 1

        # Take our 2 lists, and give one each to a recursive call of MergeSort (this function)
        returnedList1 = self.WordSort(list1)
        returnedList2 = self.WordSort(list2)

        # Initise the list to return
        sortedList = []

        # This loop will run based on the total length of both lists
        for i in range(0, len(list1) + len(list2)):
            # We check if we are out of value for list1
            if len(returnedList1) < 1:
                # If we are out of values append the rest of list2 and end the loop
                for i in returnedList2:
                    sortedList.append(i)
                break
            # Same as above, only for list2, then appending list1
            if len(returnedList2) < 1:
                for i in returnedList1:
                    sortedList.append(i)
                break
            # Check which value is smaller and add that next to the sorted list
            if returnedList1[0] < returnedList2[0]:
                sortedList.append(returnedList1.pop(0))
            elif returnedList2[0] < returnedList1[0]:
                sortedList.append(returnedList2.pop(0))
            # Values must be equal, add both to sorted list
            else:
                sortedList.append(returnedList1.pop(0))
                sortedList.append(returnedList2.pop(0))

        return sortedList

    # deletes the current window and returns to the previous one
    def back(self, window, prewindow):
        window.destroy()
        prewindow.deiconify()

    # event function which is run when a entry box is clicked on in the add item window, this cause the default text in
    # the box to be cleared allowing the user to enter their own entry straight away without having to remove the
    # default text themselves
    def clear(self, event):
        event.widget.delete(0, "end")
        return None

# starts up the GUI
root = Tk()
gui = InventorySystem(root)
root.mainloop()
