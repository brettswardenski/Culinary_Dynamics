#Reference file for main project file to avoid clutter.

class menu_item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        
menuCategories = [
    "Appetizers",
    "Entrees",
    "Drinks",
    "Desserts"
]

appetizers = [
    menu_item("Breadsticks", 5.79),
    menu_item("Starter Salad", 2.49),
    menu_item("Nachos", 8.99),
    menu_item("Mozzarella Sticks", 5.99),
    menu_item("Chips & Salsa", 3.99),
    menu_item("Wings", 9.49)
]

entrees = {
    menu_item("Cheeseburger", 8.49),
    menu_item("Caeser Salad", 7.49),
    menu_item("Chicken Tenders", 8.99),
    menu_item("Club Sandwich", 6.99),
    menu_item("Pizza", 10.99)
}

pizzaOptions = [
    "Sausage",
    "Pepperoni",
    "Cheese",
    "Veggie",
]

drinks = [
    menu_item("Soft Drink", 1.49),
    menu_item("Coffee", 2.99),
    menu_item("Tea", 1.49),
    menu_item("Water", 0.00)
]

desserts = [
    menu_item("Sundae", 3.99),
    menu_item("Chocolate Cake", 4.99)
]


foodMods = [
    menu_item("ranch", 0.20),
    menu_item("bleu cheese", 0.20),
    menu_item("shredded cheese", 0.30),
    menu_item("plain", 0.00),
    menu_item("pickles", 0.00),
    menu_item("tomato", 0.00),
    menu_item("lettuce", 0.00),
    menu_item("hot sauce", 0.25)
]
