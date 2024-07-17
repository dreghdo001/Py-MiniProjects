import time
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee_maker": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee_maker": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee_maker": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee_maker": 100,
}

def is_resource_enough(ingredients):
    """RETURN TRUE IF INGREDIENTS ARE SUFFICIENT AND FALSE IF THEY ARE NOT"""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not eough {item}")
            return False
    return True

def process_coins():
    """RETURNS THE TOTAL CALCULATED FROM THE COINS INSERTED."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transsaction_successfull(payment, drink_cost):
    """CHECKS IF ENOUGH MONEY WERE INTRODUCED. RETURN TRUE OR FALSE !"""
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry, not enough money. Money refounded")
        return False

def make_coffee(drink_name, order_ingredients):
    """MAKES COFFEE AND EXTRACT INGREDIENTS FROM TOTAL RESOURCES"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy !")

still_on = True
while still_on:
    choice = input("What coffee_maker would you like ? (espresso/latte/cappuccino) ").lower()
    if choice == "report":
        for key,value in resources.items():
            print(f"{key}: {value}")
        print(f"Protift: {profit}$")
    elif choice == "off":
        print("Turning off...")
        time.sleep(3)
        break
    else:
        drink = MENU[choice]
        if is_resource_enough(drink["ingredients"]):
            payment = process_coins()
            if is_transsaction_successfull(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])





