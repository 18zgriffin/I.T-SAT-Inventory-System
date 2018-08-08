from tkinter import *
from tkinter.messagebox import showinfo

class InventorySystem(Frame):
    # initializes master
    def __init__(self, master):
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

    # creates a new window(the choice window) and hides the original root window
    # this choice window allows a user to either proceed to add item page or search item page
    def choice_window(self):
        root.withdraw()
        choicewindow = Toplevel(root)
        self.choicewindow = choicewindow
        choicewindow.title("House Inventory - Selection Page")

        # info button displays pages information
        self.button_showinfo = Button(choicewindow, text="?", command=lambda: self.InfoWindow("choicewindow"), width=2)
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

    # function which contains the add window and its contents, the add window is where the user can add new items to the
    # database
    def add_window(self, choicewindow):
        choicewindow.withdraw()
        addwindow = Toplevel(root)
        self.addwindow = addwindow
        addwindow.title("House Inventory - New Item Page")

        # info button displays pages information
        self.button_showinfo = Button(addwindow, text="?", command=lambda: self.InfoWindow("addwindow"), width=2)
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

        #### Add Item Page Frame and Contents ####
        # box in center of add item page
        self.addframe = Frame(addwindow, bd=2, relief="ridge", width=360, height=100)
        self.addframe.grid(row=3, column=0, columnspan=4)
        self.addframe.pack_propagate(0)

        # entry box you can input the name of your item into
        self.newname = StringVar()
        self.newname.set("       <Item Name>")
        self.addframename = Entry(self.addframe, textvariable=self.newname, width=16)
        self.addframename.grid(column=0, row=1, sticky="w")

        # place that displays who the owner is which is the creator
        self.addframeowner = Label(self.addframe, text="Owner: "+self.user, width=16)
        self.addframeowner.grid(column=1, row=1)

        # entry box the item description can be entered into
        self.newdescrip = StringVar()
        self.newdescrip.set("<Enter a description of the item>")
        self.addframedescrip = Entry(self.addframe, textvariable=self.newdescrip, width=33)
        self.addframedescrip.grid(column=0, row=2, columnspan=2)

        # drop down menu the a user can select an item location from
        self.addlocation = StringVar()
        self.addlocation.set("     <Location>")
        self.addframelocation = OptionMenu(self.addframe, self.addlocation, "Lounge", "Bedroom", "Kitchen")
        self.addframelocation.grid(column=1, row=3, sticky="ew")

        # label of price and entry box to enter the price of the item into
        self.addframepricelabel = Label(self.addframe, text="Price: ")
        self.addframepricelabel.grid(column=0, row=3, sticky="w")
        self.newPrice = IntVar()
        self.newPrice.set("")
        self.addframeprice = Entry(self.addframe, textvariable=self.newPrice, width=11)
        self.addframeprice.grid(column=0, row=3, sticky="e")
        #### End ####

        # this runs the save command causing the program to save the entered item to the database
        self.saveButton = Button(addwindow, text="Save", command=self.save)
        self.saveButton.grid(row=6, column=1, columnspan=2, pady=(2.5, 0))

        # button which closes the GUI
        self.close_button = Button(addwindow, text="Exit", command=choicewindow.quit, width=4)
        self.close_button.grid(row=7, column=3, sticky="e")

        # this runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(addwindow, text="Logout", command=lambda: self.logout(addwindow))
        self.logoutButton.grid(row=7, column=0, sticky="w")

        addwindow.protocol('WM_DELETE_WINDOW', self.defaultExit)

    def search_window(self, choicewindow):
        choicewindow.withdraw()
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
        self.backButton = Button(searchwindow, text="Back", command=lambda: self.back(searchwindow, choicewindow))
        self.backButton.grid(row=1, column=0, sticky="w")

        # page title
        self.titleText = Label(searchwindow, text="House Inventory - Search", font=("Times", "24", "bold italic"))
        self.titleText.grid(column=1, columnspan=2, row=2, pady=15)

        #### Frame which contains search label and entry box for the search ####
        # box in center of add item page
        self.searchframe = Frame(searchwindow, bd=2, relief="ridge", width=360, height=100)
        self.searchframe.grid(row=3, column=1, columnspan=2)
        self.searchframe.pack_propagate(0)

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
        self.searchButton = Button(searchwindow, text="Search", command=lambda: self.search(self.searchterm))
        self.searchButton.grid(column=1, columnspan=2, row=5)

        # button which closes the GUI
        self.close_button = Button(searchwindow, text="Exit", command=choicewindow.quit, width=4)
        self.close_button.grid(row=6, column=3, sticky="e", pady=(15, 0))

        # this runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(searchwindow, text="Logout", command=lambda: self.logout(searchwindow))
        self.logoutButton.grid(row=6, column=0, sticky="w", pady=(15, 0))

        # detects if the user pressed the default [X] button and shuts down code fully
        searchwindow.protocol('WM_DELETE_WINDOW', self.defaultExit)

    def results_window(self, searchwindow):
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

        self.resultsframeidname = Label(self.resultsframe, text="Item Name")
        self.resultsframeidname.grid(row=1, column=0, padx=(0, 1), pady=(0,1), sticky="ew")
        self.resultsframeidlocation = Label(self.resultsframe, text="   Location   ")
        self.resultsframeidlocation.grid(row=1, column=1, padx=(0, 1))
        self.resultsframeidvalue = Label(self.resultsframe, text="  Value  ")
        self.resultsframeidvalue.grid(row=1, column=2, padx=(0, 1))
        self.resultsframeidowner = Label(self.resultsframe, text="  Owner  ")
        self.resultsframeidowner.grid(row=1, column=3)
        #### Frame END ####

        # button which closes the GUI
        self.close_button = Button(resultswindow, text="Exit", command=resultswindow.quit, width=4)
        self.close_button.grid(row=7, column=3, sticky="e")

        # this runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(resultswindow, text="Logout", command=lambda: self.logout(resultswindow))
        self.logoutButton.grid(row=7, column=0, sticky="w")

        resultswindow.protocol('WM_DELETE_WINDOW', self.defaultExit)

    # if the user exits the window while not in the main login window this makes the code is fully shutdown
    def defaultExit(self):
        root.destroy()

    # logs the user out and shows the login screen again
    def logout(self, window):
        window.destroy()
        root.deiconify()

    # deletes the current window and returns to the previous one
    def back(self, window, prewindow):
        window.destroy()
        prewindow.deiconify()

    def save(self):
        print("Hey")

    # this function is run when the user presses search in the search window, it runs the results window and then
    # searches if the term is mentioned in any of the items details, then displaying applicable results
    def search(self, searchterm):
        # starts up the results window
        self.results_window(self.searchwindow)
        searchterm = self.searchterm.get()
        # gets items file ready to use
        items = open("items.txt", "r")
        resultcount = 0
        # for every item set it checks if the search term is found in it, if it is then it adds the item and its other
        # details to the results page
        for line in items:
            found = re.search(str(searchterm), line)
            if found:
                itemdetails = line.rstrip('\n')
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

                # adds the new results to the window, dropping down by 1 row everytime to avoid them overlapping
                self.resultsframename = Button(self.resultsframe, textvariable=self.resultname)
                self.resultsframename.grid(row=resultcount+2, column=0, padx=(0, 1), sticky="ew", pady=(0,1))
                self.resultsframelocation = Label(self.resultsframe, textvariable=self.resultlocation)
                self.resultsframelocation.grid(row=resultcount+2, column=1, padx=(0, 1), sticky="nsew", pady=(0,1))
                self.resultsframevalue = Label(self.resultsframe, textvariable=self.resultvalue)
                self.resultsframevalue.grid(row=resultcount+2, column=2, padx=(0, 1), sticky="nsew", pady=(0,1))
                self.resultsframeowner = Label(self.resultsframe, textvariable=self.resultowner)
                self.resultsframeowner.grid(row=resultcount+2, column=3, sticky="nsew", pady=(0,1))
                resultcount += 1

        # if the search term was never found it displays on the window "Sorry no results were found"
        if resultcount == 0:
            self.noresults = Label (self.resultsframe, text="Sorry no results were found")
            self.noresults.grid(row=2, column=0, columnspan=4, sticky="ew")


    # function which runs the information window
    def InfoWindow(self, window):
        # opens information files and writes their contents to a list
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
        # runs the showinfo which that displays the appropriate information
        showinfo(ititleslist[self.title], ilist[self.information])

# starts up the GUI
root = Tk()
gui = InventorySystem(root)
root.mainloop()
