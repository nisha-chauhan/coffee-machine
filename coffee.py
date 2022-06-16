from logo import *
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 240,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

# ----------------Function for getting Money----------


def insert_money():
    '''returns the total ammount of money you entered'''
    print("please insert the money")
    total = int(input("enter the no of 10 rs.  note: "))*10
    total += int(input("enter the no of 20 rs. note: "))*20
    total += int(input("enter the no of 50 rs. note: "))*50
    total += int(input("enter the no of 100 rs.note: "))*100

    return total


# ----------------Function for Checking Transactions----------


def check_transaction(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        global profit
        profit += drink_cost
        print(profit)
        change = round(money_recieved-drink_cost)
        print(f"Here is your {change}")
        print("your drink is making ")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# -----------Working of machine---------


on = True
while on:
    print(coffee_logo)
    choice = input("What whould you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        on = False
    elif choice == "report":
        for item in resources:
            print(resources)
        print(f"Money: rs.{profit}")
    else:
        order_drink = MENU[choice]
        print(f"Ingredients for {choice}, {order_drink['ingredients']}\n")
        print(f"Cost of your {choice} {order_drink['cost']}\n")
        print(f'Available resources {resources}')

        # insert_money()
        payment = insert_money()
        print(payment)

        check_transaction(payment, order_drink["cost"])