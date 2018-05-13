import os

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b
    
def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b
    
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b
    
def divide(a, b):
    if b != 0:
        print(f"DIVIDING {a} / {b}")
        return a / b
    else:
        print("Dividend must be positive...")
        
os.system("clear")
print("\tLet's do some math with just functions!\n")

choice = "soy un guarro"
while (choice != True or choice != False):
    print("Would you like to conform yourself with Zed Shaw prepotency?")
    choice = input("Yes or No? (Y/N): ")
    
    if choice == "Y" or choice == "y" or choice == "1":
        print("YOU LAZY PIECE OF FAGGET\n")
        choice = True
        break
    elif choice == "N" or choice == "n" or choice == 0:
        print("DAT'S MA BOI!!1\n")
        choice = False
        break
    else:
        print("Wrong input. Read Carefully the instructions.")
        os.system("clear")
    
if choice == True:
    age = add(30, 5)
    height = substract(78, 4)
    weight = multiply(90, 2)
    iq = divide(100, 2)
    
    print(f"\nAge: {age}\nHeight: {height}\nWeight: {weight}\nIQ: {iq}\n")
elif choice == False:
    age1 = int(input("Age 1: "))
    age2 = int(input("Age 2: "))
    age = add(age1, age2)
    
    height1 = int(input("Height 1 (in cm): "))
    height2 = int(input("Height 2 (in cm): "))
    height = substract(height1, height2)
    
    weight1 = float(input("Weight 1 (in kg): "))
    weight2 = float(input("Weight 2 (in kg): "))
    weight = multiply(weight1, weight2)
        
    iq1 = int(input("IQ 1: "))
    iq2 = int(input("IQ 2: "))
    iq = divide(iq1, iq2)
    
    print(f"\n\nAge: {age}\nHeight: {height}\nWeight: {weight}\nIQ: {iq}\n")
else:
    print("NO POSIBLE :DDDD")

#A puzzle for the extra credit, type it in anyway.
if choice == False:
    print("Here's a puzzle.")
    what = add(age, substract(height, multiply(weight, divide(iq, 2))))
    print("That becomes: ", what, "\nCould you have done it by hand?")
        
