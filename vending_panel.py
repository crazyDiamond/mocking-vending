#!/usr/bin/python3
import vending_machine
import RPi.GPIO as GPIO

# Must be done before instantiating a VendingMachine
GPIO.setmode(GPIO.BCM)

x = vending_machine.VendingMachine()
run = True


print(30 * '-')
print("   V E N D - O - M A T I C   ")
print(30 * '-')
print("Press X to Exit")
print("Press C to see Cash Balance")
print(30 * '-')

message = "INSERT COIN"

terminate = False
product_selected = False
selected_product = None
product_price = None

while not selected_product:
    print("")
    print(40 * "#")
    print("Choose a product")
    products = x.get_products()
    keys = list(products)
    for index in range(len(keys)):
        product = keys[index]
        print("{} + ${:0,.2f}".format(product, products[product]))
    print(40 * "#")
    print("")

    choice = input("Select product [A,O,B]: ")
    if choice == "A":
        selected_product = vending_machine.APPLE
    if choice == "O":
        selected_product = vending_machine.ORANGE
    if choice == "B":
        selected_product = vending_machine.BANANA

while not terminate:
    print("")
    print(40 * "#")
    print(message)
    print(40 * "#")
    print("")

    choice = input("Input coin [N,D,Q,$]: ")

    if choice == "N":
        x.input_coin(vending_machine.NICKEL)
    elif choice == "D":
        x.input_coin(vending_machine.DIME)
    elif choice == "Q":
        x.input_coin(vending_machine.QUARTER)
    elif choice == "$":
        x.input_coin(vending_machine.DOLLAR)
    elif choice == "X":
        print("Exit")
        terminate = True
    else:
        print("Invalid coin. Try again...")

    if x.can_purchase(selected_product):
        print(x.purchase_product(selected_product))

    if x.get_coins_value() > 0:
        message = "${:0,.2f}".format(x.get_coins_value())
    else:
        message = "INSERT COIN"
