'''
Author: Brett Swardenski 
Assignment: SDEV 140 Final Project
Description: 
'''

from tkinter import *
from collections import defaultdict

root = Tk()
root.title('Culinary Dynamics')
root.geometry('800x720')
root.resizable(False, False)



#Menu
######################################################################

#defines class for menu items.
class menu_item:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return "$" + str(self.price) + "  " + self.name

#menu list.
menu = [
    menu_item("Breadsticks", 5.79, "Appetizer"),
    menu_item("Starter Salad", 2.49, "Appetizer"),
    menu_item("Nachos", 8.99, "Appetizer"),
    menu_item("Mozzarella Sticks", 5.99, "Appetizer"),
    menu_item("Chips & Salsa", 3.99, "Appetizer"),
    menu_item("Buffalo Wings", 9.49, "Appetizer"),

    menu_item("Cheeseburger", 8.49, "Entree"),
    menu_item("Caeser Salad", 7.49, "Entree"),
    menu_item("Chicken Tenders", 8.99, "Entree"),
    menu_item("Club Sandwich", 6.99, "Entree"),
    menu_item("Pizza", 10.99, "Entree"),

    menu_item("Soft Drink", 1.49, "Drink"),
    menu_item("Coffee", 2.99, "Drink"),
    menu_item("Tea", 1.49, "Drink"),
    menu_item("Water", 0.00, "Drink"),

    menu_item("Sundae", 3.99, "Dessert"),
    menu_item("Chocolate Cake", 4.99, "Dessert")
]


######################################################################
######################################################################


#Order Building
######################################################################

#creates dictionary of orders.
global orders
orders = defaultdict(list)

#finds menu items associated with buttons.
def find_item(m):
    for menu_item in menu:
        if m == menu_item.name:
            return menu_item

#supposed to add items to selected order.
def add_to_order(menu_item):
    orders[orderID].append(menu_item)
    print(orders)

#displays order in the middle frame.
def display_order_middle(orderID):
    clear_display()
    global totalDisplay
    global total
    total = 0
    for menu_item in orders[orderID]:
        total = total + menu_item.price
        listItem = Label(middleFrame, text=menu_item, \
                         font=("Helvetica", 16), bg="light blue")
        listItem.grid(column=0, row=len(middleFrame.winfo_children()), \
                      pady=5, sticky=W)

    totalDisplay = Label(middleFrame, text="Total: $" + str(round(total, 2)),\
                         font=("Helvetica", 16), bg="light blue")
    totalDisplay.place(anchor=SW, y = 510)


######################################################################
######################################################################


#Menu Navigation Functions
######################################################################

#provides a blank frame for buttons to populate.
def clear_buttons():
    for widgets in rightFrame.winfo_children():
        widgets.destroy()

#displays appetizer items as buttons when called.
def app_menu():
    clear_buttons()
    global appMenu
    appMenu = []

    for menu_item in menu:
        if menu_item.category == "Appetizer":
            appMenu.append(menu_item)
            menuItem = Button(rightFrame, text=menu_item.name, \
                        font=('Helvetica', 18), width=14, height=1, \
                        command=lambda m=menu_item.name: \
                        [add_to_order(find_item(m)), \
                        display_order_middle(orderID)])
            menuItem.grid(column=0, row=appMenu.index(menu_item), pady=15)

#displays entree items as buttons when called.
def entree_menu():
    clear_buttons()
    global entreeMenu
    entreeMenu = []

    for menu_item in menu:
        if menu_item.category == "Entree":
            entreeMenu.append(menu_item)
            menuItem = Button(rightFrame, text=menu_item.name, \
                        font=('Helvetica', 18), width=14, height=1, \
                        command=lambda m=menu_item.name: \
                        [add_to_order(find_item(m)), \
                        display_order_middle(orderID)])
            menuItem.grid(column=0, row=entreeMenu.index(menu_item), pady=15)

#displays drink items as buttons when called.
def drink_menu():
    clear_buttons()
    global drinkMenu
    drinkMenu = []

    for menu_item in menu:
        if menu_item.category == "Drink":
            drinkMenu.append(menu_item)
            menuItem = Button(rightFrame, text=menu_item.name, \
                        font=('Helvetica', 18), width=14, height=1, \
                        command=lambda m=menu_item.name: \
                        [add_to_order(find_item(m)), \
                        display_order_middle(orderID)])
            menuItem.grid(column=0, row=drinkMenu.index(menu_item), pady=15)

#displays dessert items as buttons when called.
def dessert_menu():
    clear_buttons()
    global dessertMenu
    dessertMenu = []

    for menu_item in menu:
        if menu_item.category == "Dessert":
            dessertMenu.append(menu_item)
            menuItem = Button(rightFrame, text=menu_item.name, \
                        font=('Helvetica', 18), width=14, height=1, \
                        command=lambda m=menu_item.name: \
                        [add_to_order(find_item(m)), \
                        display_order_middle(orderID)])
            menuItem.grid(column=0, row=dessertMenu.index(menu_item), pady=15)

#dictionary of functions for category buttons.
menu_dict = {
    "Appetizer": app_menu,
    "Entree": entree_menu,
    "Drink": drink_menu,
    "Dessert": dessert_menu
}

#displays menu categories to choose from.
def category_list():
    clear_buttons()
    global categoryList
    categoryList = []

    for menu_item in menu:
        category = menu_item.category
        if category not in categoryList and category != "Mod":
            categoryList.append(category)

    for category in categoryList:
        catButton = Button(rightFrame, text=category, \
                        font=('Helvetica', 18), width=14, height=1, \
                        command=menu_dict[category])
        catButton.grid(column=0, row=categoryList.index(category), pady=15)


######################################################################
######################################################################


#Customer Order Display Frames and Navigation
######################################################################    
    
#resets middle frame to switch between orders.
def clear_display():
    for widgets in middleFrame.winfo_children():
        widgets.destroy()

#meant to be used as a way to retrieve orders from the 'orders' dictionary.
def find_order(m):
    if m in orders:
        return orders[m]

#displays orders from 'orders' dictionary as radio buttons.
def order_list():
    s = StringVar()
    global orderID
    orderID = s.get()
    for name in orders.keys():
        orderButton = Radiobutton(leftFrame, text=name, \
                            font=("Helvetica", 18), width=14, \
                            command= lambda m=name: (clear_display(),\
                                    display_order_middle(orders[m])),\
                            indicatoron=FALSE, variable=s, \
                            value=name)
        orderButton.grid(row=len(orders), column=0, pady=10)
    print(orders)

#new order screen.
def new_order():
    clear_display()
    e=StringVar()
    customers = []

    #adds entered name as key for dictionary and provides it with a blank list value.
    def add_order():
        name = e.get()
        if name not in customers and name != "":
            customers.append(name)
            for name in customers:
                orders[name] = []
            orderName.delete(0, 'end')

    enterName = Label(middleFrame, text="Enter name for order:", \
                    font=("Helvetica", 18), bg="light blue")
    enterName.grid(row=0, column=0, pady=10, padx=10, sticky=W)
    orderName = Entry(middleFrame, font=("Helvetica", 18), \
                    width=10, textvariable=e)
    orderName.grid(row=1, column=0, pady=10, padx=10, sticky=W)

    addOrder = Button(middleFrame, text="Add Order", width=19, height=1, \
                      command=lambda:[add_order(), order_list()])
    addOrder.grid(row=2, column=0, pady=10, padx=10, sticky=W)


######################################################################
######################################################################



#Windows
######################################################################

#primary window construction of frames and widgets for order system.
def mainWindow():
    welcome.destroy()
    start.destroy()

    topFrame.config(height=100)
    title.config(font=('Helvetica', 24))

    global leftFrame
    leftFrame = Frame(root, bg="light blue", \
                       highlightbackground="light slate gray", \
                       highlightthickness=1, height=520, width=(200))
    leftFrame.grid(row=1, column=0, sticky=W)
    leftFrame.grid_propagate(FALSE)

    newOrder = Button(leftFrame, text="New Order", \
                      font=("Helvetica", 18), width=14, height=1, \
                        command=new_order)
    newOrder.grid(row=0, column=0, pady=15)

    global middleFrame
    middleFrame = Frame(root, bg="light blue", \
                        highlightbackground="light slate gray", \
                        highlightthickness=1, height=520, width=(400))
    middleFrame.grid(row=1, column=1, sticky=W)
    middleFrame.grid_propagate(FALSE)

    global rightFrame
    rightFrame = Frame(root, bg="light blue", \
                       highlightbackground="light slate gray", \
                       highlightthickness=1, height=520, width=(200))
    rightFrame.grid(row=1, column=2, sticky=W)
    rightFrame.grid_propagate(FALSE)

    category_list()
        
    bottomFrame.config(height=100)
   
    categories = Button(bottomFrame, text="Categories", \
                    font=("Helvetica", 14), command=category_list)
    categories.place(anchor=NE, x=750, y=25)

#welcome window to display upon startup.
def startWindow():
    topFrame.config(height=360)
    bottomFrame.config(height=360)

    title.config(font=('Helvetica', 48))
    global start
    start = Button(bottomFrame, text='Start', font=('Helvetica', 20), \
                    width=12, height=3, command=mainWindow)
    start.place(anchor=CENTER, relx=0.5, rely=0.15)
    global welcome
    welcome = Label(topFrame, text='Welcome!', bg="light blue", \
                     font=('Helvetica', 28))
    welcome.place(anchor=CENTER, relx=0.5, rely=0.75)
    

topFrame = Frame(root, bg="light blue", \
                 highlightbackground="light slate gray", \
                 highlightthickness=1, width=800)
topFrame.grid(row=0, column=0, columnspan=3)
topFrame.grid_propagate(FALSE)

title = Label(topFrame, text='Culinary Dynamics', bg="light blue")
title.place(anchor=CENTER, relx=0.5, rely=0.5)

bottomFrame = Frame(root, bg="light blue", \
                    highlightbackground="light slate gray", \
                    highlightthickness=1, width=800)
bottomFrame.grid(row=2, column=0, columnspan=3, sticky=N)
bottomFrame.grid_propagate(FALSE)

startWindow()




root.mainloop()