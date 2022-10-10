from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
machine_money = MoneyMachine()
is_on = True
while is_on:
    order = input(f"What drink do you want? {menu.get_items()} ")
    if order.lower() == 'report':
        coffee_machine.report()
        machine_money.report()
    elif order.lower() == 'off':
        is_on = False
    else:
        drink = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink) and machine_money.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)

