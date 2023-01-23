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
quarter = 0
dime = 0
nickle = 0
penny = 0
stop = False
def check_resources():
    if resources["water"] < 0:
        return "Sorry, there isn't enough water"
    if resources ["coffee"]< 0:
        return "Sorry, there isn't enough coffee"
    if resources["milk"] < 0:
        return "Sorry there isn't enough milk"

#getting the clients'orders
while not stop:
  order = input("What would you like? (espresso/latte/cappuccino): ")
  if order == "report":
    print(resources)
    
  elif order == "espresso":
    check_resources()
    resources["water"] -= 50
    resources["coffee"] -= 18
    print(check_resources())
    
  elif order == "latte":
    check_resources()
    resources["water"] -= 200
    resources["coffee"] -= 24
    resources["milk"] -= 150
    print(check_resources())
    
  elif order == "cappuccino":
    check_resources()
    resources["water"] -= 250
    resources["coffee"] -= 24
    resources["milk"] -= 100
    print(check_resources())
    
    
    #print("Please insert coins ")

    #quarter = int(input("How many quarters?: "))
    #penny = int(input("How many pennies?: "))
    #dime = int(input("How many dimes?: "))
    #nickle = int(input("How many nickles?: "))

  if input("Turn off the machine? off or no ") == "off":
    stop = True
    



