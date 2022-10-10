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
    elif order.lower() == 'off':
        print("Turning machine off")
        break
    else:
        drink = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink):
            ingredients = drink.ingredients
            coffee = MenuItem(name=drink.name, water=ingredients['water'],
                              coffee=ingredients['coffee'], milk=ingredients['milk'], cost=drink.cost)
            user_quarters = int(input("How many quarters?: ")) * 0.25
            user_dimes = int(input("How many dimes?: ")) * 0.10
            user_nickles = int(input("How many nickles?: ")) * 0.05
            user_pennies = int(input("How many pennies?: ")) * 0.01
            user_total = user_pennies + user_nickles + user_dimes + user_quarters
            if machine_money.make_payment(user_total):
                coffee_machine.make_coffee(coffee)
            else:
                print("Not enough money")
