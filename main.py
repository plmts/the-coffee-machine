MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def is_resources_sufficient(order_ingredients):
    """Return true when the order can be made and false if ingredients ar insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    total = 0
    print("Please, insert coins.")
    total += int(input("How manny quarters: ")) * 0.25
    total += int(input("How manny dimes: ")) * 0.1
    total += int(input("How manny nickels: ")) * 0.05
    total += int(input("How manny pennies: ")) * 0.01
    return total

balance = 0
game_on = True

while game_on:
    choice = input("“What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        game_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${balance}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            process_coins()
            