#this file is simply used when coding to test snippets from inside the code outside the code
#and to test snippets of other code and how to integrate that into my code
#throughout commits this file (will of had/will have) random code in it they may not ever
#appear in the actuall code although these lines will be all that remains once completed


def search():
    items = open("items.txt", "r")
    for line in items:
        itemdetails = line.rstrip('\n')
        itemdetails = itemdetails.splitlines()
        print(itemdetails)

search()