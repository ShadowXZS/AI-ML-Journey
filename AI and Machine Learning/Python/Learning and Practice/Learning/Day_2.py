#Control Flow and Logical Operators
#Control FLow with If/Else and Conditional Operators
# if/else statement = Depending on a Particular Condition, Do a or B
#if condition:
    #do this
#else:
    #do this
#Draw.io to create Flow Charts or Diagrams
print("Welcome to the Roller-Coaster :")
height = int(input("Please Enter Your Height in Cms :"))
if height >= 120:
    print("Here is your ticket, Enjoy the Ride ")
# If and Else are Pair, Be careful of the Indentation of the Else Following IF Statement ( You will get Indentation Error if you don't satisfy this rule )
# also care about the colon after the If and Else Statement
else:
    print("Sorry you have to grow taller before you can ride")
#Comparison Operators
# > Greater than
# > Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to
# One Equal Sign = Assignment Two Equal Sign == Check Equality ( Error Captured = Invalid Syntax )

# Modulo Operator
# % Goes between 2 Numbers, Finds out the remainder of the Division Carried out between 2 Numbers
expression = 10%3
print(expression)
#Check Odd Or Even
OE_Number = int(input("Enter the Number: "))
if OE_Number%2 == 0:
    print("You have entered a Even Number.")
else:
    print("You have entered a Odd Number.")

#Nested If Statements and Elif Statements

#if condition:
    #if another condition:
        #do this
    #else:
        #do this
#else:
    #do this
print("Welcome to the Roller-Coaster :")
height = int(input("Please Enter Your Height in Cms :"))
age = int(input("Please Enter Your Age In Years:"))
if height >= 120:
    print("Here is your ticket, Enjoy the Ride ")
    if age >= 18:
        print("Please Pay ₹800")
    else:
        print("Please Pay ₹350")
else:
    print("Sorry you have to grow taller before you can ride")

#Elif
#if condition1:
    #do A
#elfi condition2:
    #do B
#else:
    #do this
print("Welcome to the Roller-Coaster :")
height = int(input("Please Enter Your Height in Cms :"))
age = int(input("Please Enter Your Age In Years:"))
if height >= 120:
    print("Here is your ticket, Enjoy the Ride ")
    if age >= 18:
        print("Please Pay ₹950")
    elif age < 18 and age >= 12:
#Improvised and added and Operator To Learn, Not Sure if this is Optimal Tried something Not Explained in the Course
        print("Please Pay ₹550")
    else:
        print("Please Pay ₹350")
else:
    print("Sorry you have to grow taller before you can ride")

#Multiple if Statements in Succession
#if condition 1:
 #do A
#if condition 2:
 #do B
#if condtion 3:
 #do C
print("Welcome to the Roller-Coaster :")
height = int(input("Please Enter Your Height in Cms :"))
age = int(input("Please Enter Your Age In Years:"))
bill = 0
if height >= 120:
    print("Here is your ticket, Enjoy the Ride ")
    if age >= 18:
        bill = 950
        print("Adult Tickets are ₹950")
    elif age < 18 and age >= 12:
        # Improvised and added and Operator To Learn, Not Sure if this is Optimal Tried something Not Explained in the Course ( Done this Before Going through Logical Operator Module)
        bill = 550
        print("Youth Tickets are ₹550")
    else:
        bill = 350
        print("Child Tickets are ₹350")
    wants_photo = input("Do you want to have a Photo Taken ? Type Y for Yes and N for No.")
    if wants_photo == "Y":
        bill += 120

        #Short form of bill = bill + 120
        #Current Value of Bill + the Photo Charges Ensures the charges of the Photo is Updated.
    print(f"Please Pay: ₹{bill}")

else:
    print("Sorry you have to grow taller before you can ride")

#Logical Operators
#A and B : And Operator : Both have to be True
#C or D : Or Operator : One of them have to be True
# not E : Not Operator : True becomes False and Vise Versa
#Python Console To Quickly Evaluate the Code
