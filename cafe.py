# This program calculates the total stock worth in a cafe based a list of 4 menu items
# Total calculation based on the price of each item on the menu and how much stock the cafe contains

print("Welcome to Cafe Brazil!")
menu = ["pão de queijo", "misto", "tapioca", "omelete"]
print(f"This is the menu: {menu}")

stock = {"pão de queijo": 50,
        "misto": 45,
        "tapioca": 30,
        "omelete": 25}

price = {"pão de queijo": 3,
         "misto": 4,
         "tapioca": 6,
         "omelete": 5}

total_stock = 0 # Total stock is how much the entire stock of the cafe is worth based on the price of each item and how much stock there is each item

for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

print("The total of items in stock is " + str(sum(stock.values())))
print("The total value of all stock in Cafe Brazil is £ " + str(total_stock))
