from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    drink_name = input(f"What would you like? ({menu.get_items()})")
    if drink_name == "off":
        is_on = False
    elif drink_name == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(drink_name)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
