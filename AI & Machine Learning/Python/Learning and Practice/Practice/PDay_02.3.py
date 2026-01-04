#Incorporating Logical Operators
print("Welcome to the Roller-Coaster :")
height = float(input("Please Enter Your Height in Cms :"))
age = int(input("Please Enter Your Age In Years:"))
bill = 0
if height >= 120:
    print("Here is your ticket, Enjoy the Ride ")
    if age >= 18:
        bill = 950
        print("Adult Tickets are ₹950")
    elif age < 18 and age >= 12:
        bill = 550
        print("Youth Tickets are ₹550")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Yay!, You are Eligible for a Promotional Offer, You Get to Ride for Free ")
#Above elseif was added after going through Logical Operators Module.
    else:
        bill = 350
        print("Child Tickets are ₹350")
    wants_photo = input("Do you want to have a Photo Taken ? Type Y for Yes and N for No.")
    if wants_photo == "Y":
        bill += 120
    else:
        print("No Photo will be Given.")

    print(f"Please Pay: ₹{bill}")

else:
    print("Sorry you have to grow taller before you can ride")