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

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
       if order_ingredients[item] >= resources[item]:
           print(f"Sorry there is not enough {item}")
           return False
    return True

continue_prompting = True

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if mones is insufficient"""
    if money_received > drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money. Money refunded")
        return False

# Add money to the resources
def add_money():
    """Returns the total coins inserted."""
    print("Please insert coins)")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return quarters + dimes + nickles + pennies

# Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while continue_prompting:
    choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
# Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == "off":
        continue_prompting = False
# Print report on the cofee machine resources 
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
# Refill ingredients
    elif choice == "refill":  
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
        print("Resources have been refilled")
# Check resources sufficient?
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = add_money()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice,drink["ingredients"] )