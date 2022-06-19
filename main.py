from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()

my_coffee_maker = CoffeeMaker()

my_menu = Menu()

# my_coffee_maker.report()
# my_money_machine.report()

ongoing = True

while ongoing:
    options = my_menu.get_items()
    choice = input(f"What would you like? ({options})")

    if choice == "off":
        ongoing = False
    elif choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        user_drink = my_menu.find_drink(choice)

        if my_coffee_maker.is_resource_sufficient(user_drink):
            if my_money_machine.make_payment(user_drink.cost):
                my_coffee_maker.make_coffee(user_drink)
