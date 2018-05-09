def add(a, b):
    print("ADDING %d + %d" %(a, b))
    return a + b
    
def substract(a, b):
    print("SUBSTRACTING %d - %d" %(a, b))
    return a - b
    
def multiply(a, b):
    print("MULTIPLYING %d * %d" %(a, b))
    return a * b
    
def divide(a, b):
    if b != 0:
        print("DIVIDING %d / %d" %(a, b))
        return a / b
    else:
        print("Dividend must be positive...")
        
print("Let's do some math with just functions!")

print("Would you like to conform yourself with Zed Shaw prepotency?")
choice = (input("1 for True and 0 for False."))

while (choice == True) or (choice == False):
    if (choice == "Y") or (choice == 1):
        choice = True
        break
    elif (choice == "N") or (choice == 0):
        choice == False
        break
    else:
        print("Wrong input. Read Carefully the instructions.")
        break

if choice == True:
    age = add(30, 5)
    height = substract(78, 4)
    weight = multiply(90, 2)
    iq = divide(100, 2)
else:
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

print("Age: %d\nHeight: %d\nWeight: %d\nIQ: %d" %(age, height, weight, iq))

#A puzzle for the extra credit, type it in anyway.
print("Here's a puzzle.")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "\nCan you do it by hand?")
        
