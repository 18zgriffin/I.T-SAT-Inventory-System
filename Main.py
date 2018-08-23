from tkinter import *
from tkinter.messagebox import showinfo

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
        self.close_button = Button(master, text="Exit", command=lambda: self.defaultexit_window())
        self.close_button.grid(row=6, column=3, sticky="e")

        # result of login
        self.attemptResult = StringVar()
        self.feetLabel = Label(master, textvariable=self.attemptResult)
        self.feetLabel.grid(column=1, row=6, columnspan=2)

        self.fillSpace = Label(master, text="           ")
        self.fillSpace.grid(column=0, row=6)

        master.protocol('WM_DELETE_WINDOW', lambda: self.defaultexit_window())

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
        # hides the login page and sets up basics of new page
        root.withdraw()
        choicewindow = Toplevel(root)
        self.choicewindow = choicewindow
        choicewindow.title("House Inventory - Selection Page")

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

        # button which closes the GUI
        self.close_button = Button(choicewindow, text="Exit", command=lambda: self.defaultexit_window(), width=4)
        self.close_button.grid(row=4, column=3, sticky="e", pady=(15, 0))

        # activates if the user ever exits this window using the default [X]
        choicewindow.protocol('WM_DELETE_WINDOW', lambda: self.defaultexit_window())

    # function which contains the add window and its contents, the add window is where the user can add new items to the
    # database
    def add_window(self, choicewindow):
        # hides the previous page and sets up basics of new page
        choicewindow.withdraw()
        addwindow = Toplevel(root)
        self.addwindow = addwindow
        llocations = []
        flocations = open("locations.txt", "r")
        for line in flocations:
            llocations.append(line.strip("\n"))
        addwindow.title("House Inventory - New Item Page")

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

        # place that displays who the owner is which is the creator
        self.addframeowner = Label(self.addframe, text="Owner: "+self.user, width=16)
        self.addframeowner.grid(column=1, row=1)

        # entry box the item description can be entered into
        self.newdescrip = StringVar()
        self.newdescrip.set("<Enter a description of the item>")
        self.addframedescrip = Entry(self.addframe, textvariable=self.newdescrip, width=36)
        self.addframedescrip.grid(column=0, row=2, columnspan=2)

        # drop down menu the a user can select an item location from
        self.newlocation = StringVar()
        self.newlocation.set("     <Location>")
        self.addframelocation = OptionMenu(self.addframe, self.newlocation, *llocations)
        self.addframelocation.grid(column=1, row=3, sticky="ew")

        # label of price and entry box to enter the price of the item into
        self.addframepricelabel = Label(self.addframe, text="Price:$")
        self.addframepricelabel.grid(column=0, row=3, sticky="w")
        self.newPrice = IntVar()
        self.newPrice.set("0")
        self.addframeprice = Entry(self.addframe, textvariable=self.newPrice, width=11)
        self.addframeprice.grid(column=0, row=3, sticky="e")
        #### End ####

        # this runs the save command causing the program to save the entered item to the database
        self.saveButton = Button(addwindow, text="Save", command=lambda: (self.save(addwindow, choicewindow)))
        self.saveButton.grid(row=6, column=1, columnspan=2, pady=(2.5, 0))

        # button which closes the GUI
        self.close_button = Button(addwindow, text="Exit", command=lambda: self.defaultexit_window(), width=4)
        self.close_button.grid(row=7, column=3, sticky="e")

        # result of login
        self.addResult = StringVar()
        self.feetLabel = Label(addwindow, textvariable=self.addResult)
        self.feetLabel.grid(column=1, row=7, columnspan=2)

        # a button that runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(addwindow, text="Logout", command=lambda: self.logout_window(addwindow))
        self.logoutButton.grid(row=7, column=0, sticky="w")

        # makes the default exit command run, whenever the user presses the default exit button
        addwindow.protocol('WM_DELETE_WINDOW', lambda: self.defaultexit_window())

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
        self.searchButton = Button(searchwindow, text="Search", command=lambda: self.search(self.searchterm))
        self.searchButton.grid(column=1, columnspan=2, row=5)

        # button which closes the GUI
        self.close_button = Button(searchwindow, text="Exit", command=lambda: self.defaultexit_window(), width=4)
        self.close_button.grid(row=6, column=3, sticky="e", pady=(15, 0))

        # this runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(searchwindow, text="Logout", command=lambda: self.logout_window(searchwindow))
        self.logoutButton.grid(row=6, column=0, sticky="w", pady=(15, 0))

        # detects if the user pressed the default [X] button and runs the default exit function
        searchwindow.protocol('WM_DELETE_WINDOW', lambda: self.defaultexit_window())

    # this function is run when the user presses search in the search window, it runs the results window and then
    # searches if the term is mentioned in any of the items details, then displaying applicable results
    def search(self, searchterm):
        # starts up the results window
        self.results_window(self.searchwindow)
        searchterm = self.searchterm.get()
        # gets items file ready to use
        items = open("items.txt", "r")
        resultcount = 0
        if searchterm == " " or searchterm == "":
            self.noresults = Label(self.resultsframe, text="Please input a value")
            self.noresults.grid(row=2, column=0, columnspan=4, sticky="ew")
        else:
            # for every item set it checks if the search term is found in it, if it is then it adds the item and its other
            # details to the results page
            foundlist = []
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

        self.resultsframeidname = Label(self.resultsframe, text="Item Name")
        self.resultsframeidname.grid(row=1, column=0, padx=(0, 1), pady=(0,1), sticky="we")
        self.resultsframeidlocation = Label(self.resultsframe, text="   Location   ")
        self.resultsframeidlocation.grid(row=1, column=1, padx=(0, 1))
        self.resultsframeidvalue = Label(self.resultsframe, text="  Value  ")
        self.resultsframeidvalue.grid(row=1, column=2, padx=(0, 1))
        self.resultsframeidowner = Label(self.resultsframe, text="  Owner  ")
        self.resultsframeidowner.grid(row=1, column=3)
        #### Frame END ####

        # button which closes the GUI
        self.close_button = Button(resultswindow, text="Exit", command=lambda: self.defaultexit_window(), width=4)
        self.close_button.grid(row=7, column=3, sticky="e")

        # this runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(resultswindow, text="Logout", command=lambda: self.logout_window(resultswindow))
        self.logoutButton.grid(row=7, column=0, sticky="w")

        # if the user selecs the default [X] to exit it runs the default exit window
        resultswindow.protocol('WM_DELETE_WINDOW', lambda: self.defaultexit_window())

    def item_window(self, itemname, itemlocation, itemvalue, itemowner, itemdescrip):
        # hides the previous page and sets up basics of new page
        self.resultswindow.withdraw()
        itemwindow = Toplevel(root)
        self.itemwindow = itemwindow
        itemname = itemname.get()
        itemlocation = itemlocation.get()
        itemvalue = itemvalue.get()
        itemowner = itemowner.get()
        itemdescrip = itemdescrip.get()
        itemwindow.title("House Inventory - View Item Page")

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

        # entry box you can input the name of your item into
        self.itemframename = Label(self.itemframe, text=itemname, width=16, relief="ridge")
        self.itemframename.grid(column=0, row=1, pady=1, padx=1)

        # place that displays who the owner is which is the creator
        self.itemframeowner = Label(self.itemframe, text="Owner: " + str(itemowner), width=16, relief="ridge")
        self.itemframeowner.grid(column=1, row=1, padx=1)

        # entry box the item description can be entered into
        self.itemframedescrip = Label(self.itemframe, text=itemdescrip, width=33, relief="ridge")
        self.itemframedescrip.grid(column=0, row=2, columnspan=2, pady=2)

        # drop down menu the a user can select an item location from
        self.itemframelocation = Label(self.itemframe, text=itemlocation, relief="ridge")
        self.itemframelocation.grid(column=1, row=3, sticky="ew")

        # label of price and entry box to enter the price of the item into
        self.itemframeprice = Label(self.itemframe, text="Price:$"+itemvalue)
        self.itemframeprice.grid(column=0, row=3, pady=1)
        #### End ####

        # this checks if the user is authorised to edit or remove the item, if they are they get access to the proper
        # functions of the buttons, if the user isnt then the buttons simply do nothing
        if self.user == itemowner or self.user == "admin":
            # adds the edit button that when pressed runs the edit window
            self.editButton = Button(itemwindow, text="Edit", width=6, command=lambda: self.edit_window(itemwindow,
                itemname, itemlocation, itemvalue, itemowner, itemdescrip))
            self.editButton.grid(row=6, column=1, pady=(2.5, 0))

            self.removeButton = Button(itemwindow, text="Remove", command=lambda: self.remove_window(itemwindow,
                itemname, itemlocation, itemvalue, itemowner, itemdescrip))
            self.removeButton.grid(row=6, column=2, pady=(2.5, 0))
        else:
            self.editButton = Button(itemwindow, text="Edit", width=6)
            self.editButton.grid(row=6, column=1, pady=(2.5, 0))

            self.removeButton = Button(itemwindow, text="Remove")
            self.removeButton.grid(row=6, column=2, pady=(2.5, 0))

        # button which closes the GUI
        self.close_button = Button(itemwindow, text="Exit", command=lambda: self.defaultexit_window(), width=4)
        self.close_button.grid(row=7, column=3, sticky="e")

        # a button that runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(itemwindow, text="Logout", command=lambda: self.logout_window(itemwindow))
        self.logoutButton.grid(row=7, column=0, sticky="w")

        # makes the default exit command run, whenever the user presses the default exit button
        itemwindow.protocol('WM_DELETE_WINDOW', lambda: self.defaultexit_window())

    def edit_window(self, itemwindow, itemname, itemlocation, itemvalue, itemowner, itemdescrip):
        # hides the previous page and sets up basics of new page
        itemwindow.withdraw()
        editwindow = Toplevel(root)
        self.editwindow = editwindow
        llocations = []
        flocations = open("locations.txt", "r")
        for line in flocations:
            llocations.append(line.strip("\n"))
        lusers = []
        fusers = open("usernames.txt", "r")
        for line in fusers:
            lusers.append(line.strip("\n"))
        editwindow.title("House Inventory - Edit Item Page")

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
        self.titleText = Label(editwindow, text="House Inventory - New Item", font=("Times", "24", "bold italic"))
        self.titleText.grid(column=1, columnspan=2, row=2, pady=15)

        #### Add Item Page Frame and Contents ####
        # box in center of add item page
        self.editframe = Frame(editwindow, bd=2, relief="ridge", width=360, height=100)
        self.editframe.grid(row=3, column=0, columnspan=4)
        self.editframe.pack_propagate(0)

        # entry box you can input the name of your item into
        self.editname = StringVar()
        self.editname.set(itemname)
        self.editframename = Entry(self.editframe, textvariable=self.editname, width=16)
        self.editframename.grid(column=0, row=1, sticky="w")

        # place that displays who the owner is which is the creator
        self.editframeownerlabel = Label(self.editframe, text=" Owner:")
        self.editframeownerlabel.grid(column=1, row=1, sticky="w")
        self.edituser = StringVar()
        self.edituser.set(itemowner)
        self.editframeowner = OptionMenu(self.editframe, self.edituser, *lusers)
        self.editframeowner.config(width=10)
        self.editframeowner.grid(column=1, row=1, sticky="e")

        # entry box the item description can be entered into
        self.editdescrip = StringVar()
        self.editdescrip.set(itemdescrip)
        self.editframedescrip = Entry(self.editframe, textvariable=self.editdescrip, width=36)
        self.editframedescrip.grid(column=0, row=2, columnspan=2)

        # drop down menu the a user can select an item location from
        self.editlocation = StringVar()
        self.editlocation.set(itemlocation)
        self.editframelocation = OptionMenu(self.editframe, self.editlocation, *llocations)
        self.editframelocation.config(width=16)
        self.editframelocation.grid(column=1, row=3, sticky="ew")

        # label of price and entry box to enter the price of the item into
        self.editframepricelabel = Label(self.editframe, text="Price:$")
        self.editframepricelabel.grid(column=0, row=3, sticky="w")
        self.editPrice = IntVar()
        self.editPrice.set(itemvalue)
        self.editframeprice = Entry(self.editframe, textvariable=self.editPrice, width=11)
        self.editframeprice.grid(column=0, row=3, sticky="e")
        #### End ####

        # this runs the save command causing the program to save the entered item to the database
        self.saveeditButton = Button(editwindow, text="Save", command=lambda: (self.saveedit(editwindow, itemwindow,
            itemname, itemdescrip, itemowner, itemvalue, itemlocation)))
        self.saveeditButton.grid(row=6, column=1, columnspan=2, pady=(2.5, 0))

        # button which closes the GUI
        self.close_button = Button(editwindow, text="Exit", command=lambda: self.defaultexit_window(), width=4)
        self.close_button.grid(row=7, column=3, sticky="e")

        # result of login
        self.editResult = StringVar()
        self.feetLabel = Label(editwindow, textvariable=self.editResult)
        self.feetLabel.grid(column=1, row=7, columnspan=2)

        # a button that runs the logout command causing the current window to close and to return to the login screen
        self.logoutButton = Button(editwindow, text="Logout", command=lambda: self.logout_window(editwindow))
        self.logoutButton.grid(row=7, column=0, sticky="w")

        # makes the default exit command run, whenever the user presses the default exit button
        editwindow.protocol('WM_DELETE_WINDOW', lambda: self.defaultexit_window())

    def remove_window(self, window, prewindow, itemname, preitemdescrip, preitemowner, preitemvalue, preitemlocation):
        prewindow.withdraw()
        editwindow = Toplevel(root)
        self.editwindow = editwindow
    # if the user presses either of the exit buttons, default or the one labeled exit. this window pops up, and if the
    # user selects yes it runs default exit and closes everything, if the user presses no it just closes the pop up
    def defaultexit_window(self):
        defaultexitwindow = Toplevel(root)
        self.defaultexitwindow = defaultexitwindow
        self.exitsure = Label(defaultexitwindow, text="Are you sure about that?")
        self.exitsure.grid(row=1, column=0, columnspan=2)
        self.exityes = Button(defaultexitwindow, text="Yes", command=lambda: self.defaultExit(defaultexitwindow, "Yes"))
        self.exityes.grid(row=2, column=0)
        self.exitno = Button(defaultexitwindow, text="No", command=lambda: self.defaultExit(defaultexitwindow, "No"))
        self.exitno.grid(row=2, column=1)

    # run when a user makes a choice between yes or no when exiting, if they press yes it destroys all windows, if the
    # user pressed no it just destroys the popup
    def defaultExit(self, window, choice):
        if choice == "Yes":
            root.destroy()
        elif choice == "No":
            window.destroy()

    # runs a logout popup window that asks the user if they rally want to log out, if yes the user is returned to the
    # login window and other windows are destroyed if no then only the popup window is destroyed
    def logout_window(self, window):
        logoutwindow = Toplevel(root)
        self.logoutwindow = logoutwindow
        self.sure = Label(logoutwindow, text="Are you sure about that?")
        self.sure.grid(row=1, column=0, columnspan=2)
        self.yes = Button(logoutwindow, text="Yes", command=lambda: self.logoutConfirm(window, logoutwindow, "Yes"))
        self.yes.grid(row=2, column=0)
        self.no = Button(logoutwindow, text="No", command=lambda: self.logoutConfirm(window, logoutwindow, "No"))
        self.no.grid(row=2, column=1)

    # checks if the user selected a yes or no in the logout window, if yes the user is logged out, if no the logout pop
    # up is destroyed
    def logoutConfirm(self, window, logoutwindow, choice):
            if choice == "Yes":
                self.username.set("")
                self.password.set("")
                logoutwindow.destroy()
                window.destroy()
                root.deiconify()
            elif choice == "No":
                logoutwindow.destroy()

    # deletes the current window and returns to the previous one
    def back(self, window, prewindow):
        window.destroy()
        prewindow.deiconify()
    # run when a user tries to save an editted item, it will save the new one to the file and remove the original
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
                        editdescrip != "<Enter a description of the item>" and editlocation != "      <Location>"):
                    # if the input values are valid and the loop is currently on the one to be changed, it changes the
                    # item in the list to the appropriate editted item
                    cfline[currentline] = (editname + "," + editlocation + "," + str(editprice) + "," + edituser + "," +
                            editdescrip)
                else:
                    # tells the user to input a valid value into all boxes as the test noticed a problem
                    self.addResult.set("Please enter a valid value into all boxes")
                    return
            currentline += 1
        # writes the new list to the file
        witems = open("items.txt", "w")
        for x in cfline:
            witems.write(x)
            witems.write("\n")
        # runs the item edited window for the user
        self.itemedited_window(window, self.searchwindow)

    def save(self, window, prewindow):
        # opens items file and gets all of the users inputted variables
        items = open("items.txt", "a")
        newlocation = self.newlocation.get()
        newdescrip = self.newdescrip.get()
        newname = self.newname.get()
        newuser = self.user
        newprice = self.newPrice.get()
        # checks if all values the user input are valid and that the user actually input a value
        if (newdescrip and newname != 0 and newprice and newdescrip and newname != "" and
                newprice and newdescrip and newname != " " and newname != "       <Item Name>" and newdescrip !=
            "<Enter a description of the item>" and newlocation != "      <Location>"):
            # adds the item to the items.txt file and runs the itemadded window
            items.write("\n")
            items.write(newname + "," + newlocation + "," + str(newprice) + "," + newuser + "," + newdescrip)
            self.itemadded_window(window, prewindow)
        else:
            # tells the user to input a valid value into all boxes as the test noticed a problem
            self.addResult.set("Please enter a valid value into all boxes")

    # popup window that happens when a item is succesfully added
    def itemadded_window(self, window, prewindow):
        # destroys previous window add sets up new window with title
        window.destroy()
        itemaddedwindow = Toplevel(root)
        self.itemaddedwindow = itemaddedwindow
        itemaddedwindow.title("House Inventory")

        # adds a title telling the user that the item was succesfully added
        self.confirmtitle = Label(itemaddedwindow, text="Item added Successfully", font=("Times", "24", "bold italic"))
        self.confirmtitle.grid(row=1, column=0, columnspan=2)

        # a button that runs the back command as if the itemadded window was the add item window allowing the user to
        # return to the choice page
        self.confirmadded = Button(itemaddedwindow, text="OK", command=lambda: self.back(itemaddedwindow, prewindow))
        self.confirmadded.grid(row=2, column=0, columnspan=2)

        # runs the dfault exit function if the user uses the default exit button [X]
        itemaddedwindow.protocol('WM_DELETE_WINDOW', self.defaultexit_window)

    def itemedited_window(self, window, prewindow):
        # destroys previous window add sets up new window with title
        window.destroy()
        itemeditedwindow = Toplevel(root)
        self.itemeditedwindow = itemeditedwindow
        itemeditedwindow.title("House Inventory")

        # adds a title telling the user that the item was succesfully added
        self.confirmtitle = Label(itemeditedwindow, text="Item edit Successful", font=("Times", "24", "bold italic"))
        self.confirmtitle.grid(row=1, column=0, columnspan=2)

        # a button that runs the back command as if the itemadded window was the add item window allowing the user to
        # return to the choice page
        self.confirmadded = Button(itemeditedwindow, text="OK", command=lambda: self.back(itemeditedwindow, prewindow))
        self.confirmadded.grid(row=2, column=0, columnspan=2)

        # runs the dfault exit function if the user uses the default exit button [X]
        itemeditedwindow.protocol('WM_DELETE_WINDOW', self.defaultexit_window)

    # function which runs the information window
    def InfoWindow(self, window):
        # opens information files and writes their contents to a seperate lists
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
        # runs the showinfo which that displays the appropriate information
        showinfo(ititleslist[self.title], ilist[self.information])

# starts up the GUI
root = Tk()
gui = InventorySystem(root)
root.mainloop()