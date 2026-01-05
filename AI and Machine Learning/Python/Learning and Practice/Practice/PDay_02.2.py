#Pizza Order Practice.
print("Welcome to Python Pizza Deliveries!")
size = input("What Size Pizza do You want ? P, M or L: ")
pepperoni = input("Do you want Pepperoni on Your Pizza ? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "P":
    bill += 99
    print("Price of Personal Pizza is ₹99,")
    if pepperoni == "Y":
        bill += 29
        print("Price of Pepperoni Topping is ₹29.")
    elif pepperoni == "N":
        print("No Topping Added.")
    else:
        print("Please Type Y Or N to Select Toppings.")
    if extra_cheese == "Y":
        bill += 59
        print("Price of Extra Cheese is ₹59.")
    elif extra_cheese == "N":
        print("Regular Cheese Topping.")
    else:
        print("Please Type Y Or N to Confirm Extra Cheese.")
elif size == "M":
    bill += 199
    print("Price of Medium Pizza is ₹199,")
    if pepperoni == "Y":
        bill += 49
        print("Price of Pepperoni Topping is ₹49.")
    elif pepperoni == "N":
        print("No Topping Added.")
    else:
        print("Please Type Y Or N to Select Toppings.")
    if extra_cheese == "Y":
        bill += 89
        print("Price of Extra Cheese is ₹89")
    elif extra_cheese == "N":
        print("Regular Cheese Topping.")
    else:
        print("Please Type Y Or N to Confirm Extra Cheese.")
elif size == "L":
    bill += 399
    print("Price of Large Pizza is ₹399,")
    if pepperoni == "Y":
        bill += 69
        print("Price of Pepperoni Topping is ₹69.")
    elif pepperoni == "N":
        print("No Topping Added.")
    else:
        print("Please Type Y Or N to Select Toppings.")
    if extra_cheese == "Y":
        bill += 109
        print("Price of Extra Cheese is ₹109.")
    elif extra_cheese == "N":
        print("Regular Cheese Topping.")
    else:
        print("Please Type Y Or N to Confirm Extra Cheese.")
else:
    print("You have Selected Wrong Size")
print(f"Your Order Total is: ₹{bill}.")
#Was Afraid the Code Will Break at First before starting, Started Addressing One Problem At a Time, Completed without Error.
#Dry (Do Not Repeat Your Self)