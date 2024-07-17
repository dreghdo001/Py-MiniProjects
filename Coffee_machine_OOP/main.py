from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
machine_menu = Menu()
coffee_maker = CoffeeMaker()

still_on = True
while still_on:
    options = machine_menu.get_items()
    choice = input(f"What coffee would you like ? {options}) ").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        still_on = False
    else:
        drink = machine_menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

