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
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficient(order_ingredients):
    """retorna verdadeiro quando o pedido pode ser feito e falso quando não tiver ingredientes suficientes."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Faz o processamentos das moedas inseridas, soma o total e retorna esse valor"""
    total = 0
    print("Please, insert coins.")
    total += int(input("How manny quarters: ")) * 0.25
    total += int(input("How manny dimes: ")) * 0.1
    total += int(input("How manny nickels: ")) * 0.05
    total += int(input("How manny pennies: ")) * 0.01
    return total

def transaction_is_successful(money_received, drink_cost):
    """Retorna verdadeiro quando o valor na máquina cobrir o valor da bebida. 
    Retorna falso quando não há dinheiro suficiente"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} as change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, there is not enouth money! Money refunded.")
        return False

def make_drink(drink_name, order_ingredients):
    """tira o equitativo de ingredientes solicitados para a bebida da máquina."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


game_on = True

while game_on:
    choice = input("“What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        game_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_is_successful(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])
