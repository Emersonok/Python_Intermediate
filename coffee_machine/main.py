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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
espresso_cost = 1.5
latte_cost = 2.5
cappuccino_cost = 3.0
change = 0
stop = False

def check_resources():
    if resources["water"] < 0:
        return "Sorry, there isn't enough water"
    if resources ["coffee"]< 0:
        return "Sorry, there isn't enough coffee"
    if resources["milk"] < 0:
        return "Sorry there isn't enough milk"

def calculate_change(quarter, penny, dime, nickle):
    quarter = 0.25 * quarter
    penny = 0.01 * penny
    dime = 0.10 * dime
    nickle = 0.05 * nickle
    money = quarter + penny + dime + nickle
    if order == "espresso":
        change = money - espresso_cost
        return f"Your change is {change}"
    elif order == "latte":
        change = money - latte_cost
        return f"Your change is {change}"
    elif order == "cappuccino":
        change = money - cappuccino_cost
        return f"Your change is {change}"

#getting the clients'orders
while not stop:
  order = input("What would you like? (espresso/latte/cappuccino): ")
  if order == "report":
    print(resources)
    
  elif order == "espresso":
    resources["water"] -= 50
    resources["coffee"] -= 18
    
  elif order == "latte":
    resources["water"] -= 200
    resources["coffee"] -= 24
    resources["milk"] -= 150
    
  elif order == "cappuccino":
    resources["water"] -= 250
    resources["coffee"] -= 24
    resources["milk"] -= 100
    
    
  if resources ["water"] <= 0 or resources["coffee"] <= 0 or resources["milk"] <= 0:
    print(check_resources())
  else:
    print("Please insert coins ")

    quarter = float(input("How many quarters?: "))
    penny = float(input("How many pennies?: "))
    dime = float(input("How many dimes?: "))
    nickle = float(input("How many nickles?: "))
    print(calculate_change(quarter, penny, dime, nickle))

  if input("Turn off the machine? off or no ") == "off":
    stop = True
    



