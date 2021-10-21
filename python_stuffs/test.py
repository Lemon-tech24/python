import os

try_again = True
pi = 3.1416

def clrscr():
    os.system("cls")

def lab6():
    clrscr()
    I_code = int(input(" Enter Item code: "))
    Quantity = int(input(" Enter the Quantity: "))
    money = int(input(" Enter Amount Tendered: "))

    if I_code == 111:
        item_price = 54
    elif I_code == 222:
        item_price = 25
    elif I_code == 333:
        item_price = 100
    else:
        print("Invalid Item Code!! ")

    Item_Cost = item_price * Quantity
    vat_tax = 0.06 * Item_Cost
    total_Cost = Item_Cost + vat_tax
    money_change = money - total_Cost

    os.system("cls")
    print(" Item Code: " + str(I_code))
    print(" Quantity: " + str(Quantity))
    print(" Item Price: " + str(item_price))
    print(" Total Item Cost: " + str(Item_Cost))
    print()

    print(" VAT 6%: " + str(vat_tax))
    print(" Total Cost: " + str(total_Cost))
    print()

    print(" Amount Tendered: " + str(money))
    print(" Amount Change: " + str(money_change))

def lab8():
    clrscr()
    print(" This program computes circumference and diameter")
    radius = int(input("  Enter the radius: "))
    circum = 2 * pi * radius
    diameter = 2 * radius
    print("  The Circumference is: " + str(circum))
    print("  The Diameter is: " + str(diameter))

def lab10():
    clrscr()
    print(" This Program computes surface are and volume of sphere")
    given = int(input(" Input radius of sphere: "))
    area = 4 * pi * given ** 2
    volume = 4 / 3 * pi * given ** 3
    print(" The surface area of sphere is: " + str(area))
    print(" The volume of a sphere is: " + str(volume))

def lab11():
    clrscr()
    fahren = int(input(" Input temperature in Fahrenheit: "))
    cels = (5/9) * (fahren - 32)
    print(" The converted temperature in celsius is: " + str(cels))

def lab16():
    clrscr()
    d1 = int(input(" Input the value of D1: "))
    d2 = int(input(" Input the value of D2: "))
    area = 1/2 * d1 * d2
    print("The Area of Rhombus is: " + str(area))

while try_again:
    clrscr()
    print(" Main Menu")
    print("     [1] Lab 6")
    print("     [2] Lab 8")
    print("     [3] Lab 10")
    print("     [4] Lab 11")
    print("     [5] Lab 16")
    print("     [6] Exit")
    choice = int(input(" Enter your choice: "))

    if choice != 0 and choice <= 6:
        if choice == 1:
            lab6()
        elif choice == 2:
            lab8()
        elif choice == 3:
            lab10()
        elif choice == 4:
            lab11()
        elif choice == 5:
            lab16()
        elif choice == 6:
            clrscr()
            print("")
            answer = input("Do you really want to exit?[Y/N]: ")
            if answer == 'Y' or answer == 'y':
                exit()
            elif answer == 'N' or answer == 'n':
                try_again = True

    else:
        print("Invalid Choice!!!")

    print("")
    choice2 = input(" Do you want to choose again? [Y/N]: ")

    if choice2 == 'Y' or choice2 == 'y':
        try_again = True
    elif choice == 'N' or choice == 'n':
        try_again = False
    else:
        print("Invalid Choice Y/y and N/n only")
        exit()