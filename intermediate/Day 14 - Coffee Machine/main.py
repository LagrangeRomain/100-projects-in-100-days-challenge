MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

COINS = {
        "quarters" : 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01,
    }

INGREDIENTS = ["water", "milk", "coffee"]

def report(actual_resources, actual_money):
    for ingredient in INGREDIENTS:
        print(f"{ingredient} : {actual_resources[ingredient]}")
    print(f"Money : {actual_money}")

def are_sufficient_resources(actual_drink, actual_resources):
    for ingredient in INGREDIENTS:
        if MENU[actual_drink]["ingredients"][ingredient] > actual_resources[ingredient]:
            return ingredient
    return None

def insert_money():
    print("Please insert coins.")
    inserted_money = 0
    for coin in COINS:
        try:
            inserted_money += int(input(f"How many {coin}?: ")) * COINS[coin]
        except ValueError:
            print("Wrong value")
    return inserted_money

def is_enough_money(actual_money, chosen_drink):
    return actual_money - MENU[chosen_drink]["cost"]

def make_coffee(chosen_drink, actual_resources):
    for ingredient in INGREDIENTS:
        actual_resources[ingredient] -= MENU[chosen_drink]["ingredients"][ingredient]
    return actual_resources

resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
money = 0

def main(actual_resources, earned_money):
    while True:
        drink = input("What would you like? (espresso/latte/cappuccino): ")
        if drink == "report":
            report(actual_resources, earned_money)
        elif drink == "off":
            break
        else:
            try:
                insufficient_resource = are_sufficient_resources(drink, actual_resources)
            except KeyError:
                continue
            if insufficient_resource:
                print(f"Sorry, not enough {insufficient_resource}.")
                continue
            else:
                user_money = insert_money()
                money_rest = is_enough_money(user_money, drink)
                if money_rest < 0 :
                    print("Not enough. Money refunded")
                    continue
                else:
                    earned_money += MENU[drink]["cost"]
                    print(f"Money returned : {money_rest}")
                    actual_resources = make_coffee(drink, actual_resources)
                    print(f"Voila ! Your {drink}.")

main(resources, money)