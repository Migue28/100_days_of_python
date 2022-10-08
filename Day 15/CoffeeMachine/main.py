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

machine_resources = {
    "ingredients": {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    },
    "money": 0,
}

is_still_purchasing = True
while is_still_purchasing:
    # TODO: Ask user what type of coffee does he wants
    user_coffee_choice = input("What would you like? (espresso/latte/cappuccino) ")

    # TODO: Accept 'off' as an instruction to finish code
    if user_coffee_choice.lower() == 'off':
        print("Turning machine off")
        break

    # TODO: Accept 'report' as an instruction to show resources
    if user_coffee_choice.lower() == 'report':
        print(f"""Water: {machine_resources["ingredients"]['water']} ml
Milk: {machine_resources["ingredients"]['milk']} ml
Coffee: {machine_resources["ingredients"]['coffee']} g
Money: {machine_resources['money']} $""")

    # TODO: Check if there is enough resources to make the coffee

    else:
        def check_resources(machine_resources_available, user_choice):
            """Receive machines resources and user coffee choice to check if there is enough ingredients. Returns dictionary
     with ingredients and availability for coffee.
            """
            global MENU
            new_machine_resources = {
                "enough_ingredients": True,
                "ingredients": {},
            }
            for ingredient in MENU[user_choice]['ingredients']:
                menu_ingredient_quantity = MENU[user_choice]['ingredients'][ingredient]
                machine_ingredient_quantity = machine_resources_available['ingredients'][ingredient]
                if menu_ingredient_quantity > machine_ingredient_quantity:
                    new_machine_resources["enough_ingredients"] = False
                    break
                else:
                    new_machine_resources["ingredients"][ingredient] = machine_ingredient_quantity - menu_ingredient_quantity
            return new_machine_resources

            # TODO: Make coffee and reduce resources from the machine


        def reduce_machine_resources(machine_resources_available, order_resources, coffee_cost):
            """Get machine resources and reduce coffee order from machine resources. Returns
     machine resources less order ingredients.
            """
            for ingredient in order_resources["ingredients"]:
                order_ingredient_quantity = order_resources["ingredients"][ingredient]
                machine_resources_available["ingredients"][ingredient] = order_ingredient_quantity
            machine_resources_available["money"] += coffee_cost
            return machine_resources_available

        machine_checked_resources = check_resources(machine_resources, user_coffee_choice)
        if not machine_checked_resources["enough_ingredients"]:
            print("Not enough ingredients")
        else:
            # TODO: Process user coins
            user_quarters = int(input("How many quarters?: ")) * 0.25
            user_dimes = int(input("How many dimes?: ")) * 0.10
            user_nickles = int(input("How many nickles?: ")) * 0.05
            user_pennies = int(input("How many pennies?: ")) * 0.01
            user_total = user_pennies + user_nickles + user_dimes + user_quarters
            # TODO: Check if user have enough coins
            cost_of_coffee = MENU[user_coffee_choice]["cost"]
            if user_total == cost_of_coffee or user_total > cost_of_coffee:
                # TODO: Tell user to enjoy their drink
                print(f"Your change is {round(user_total - cost_of_coffee, 2)} $")
                print("Enjoy your coffee!")
                reduce_machine_resources(machine_resources, machine_checked_resources, cost_of_coffee)
            else:
                print("Sorry that's not enough money. Money refunded.")

