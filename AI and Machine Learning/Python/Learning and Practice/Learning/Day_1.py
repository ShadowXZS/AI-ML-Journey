#Data Types String
print("Hello"[-1])
#Method to extracting a Single Character from a String is called Subscripting
#Can use Negative Number to Count from the Last -1 (-1 is the last character)
#Integer Numbers without any decimal places (Whole Numbers)
print(123+345)
#Large Integers
print(363_456_789)
#Float Floating Point Number Decimal Point
print(3.14159)
#Boolean True/False .. Note T and F should be Uppercase
print(True)
print(False)
#Type Error  When the function dont work with Data Type given ..Len Function Dont work with Integer
len(str(12345))
len("12345")
#type() To check the data type, Note to Print it So it displays
print(type("Hello"))
print(type(363))
print(type(363.567))
print(type(True))
#Type Conversion or Type Casting
print(int("100"+"263"))
#Value Error Invalid Data Types
#Pause Challenge [print("Number of letters in Your Name: " + len((input("Enter Your Name: \n"))))
print("Number of letters in Your Name: " + str(len((input("Enter Your Name: \n")))))
#Completed Without Errors
#Mathematical Operations in Python
print(300+63)
print(400-27)
print(23*56)
print(9/3)
print(12//3)
#Division always gives floating point number : Implicit Typecasting use // to remove the decimal and the numbers after the decimal point
#Exponent ** astrix
print(2**3)
#PEMDAS priority of Order of Operations : Multiplication and Division almost have equal priority Calculation goes from Left to Right
#Number Manipulation and F Strings in Python
#round() Round of the Number Round (number , 2 (Decimal Points Included))
#int()  Flooring the Number
#Assignment Operator : Accumulate results of Operation
score = 0
score += 1
score -= 1
score *= 1
score /= 1
#Are different types of assignment Operator
print(score)
#Fstrings : Allows to Mix Different Data Types and Strings
score = 0
height = 1.8
is_winning = True
#Fstring Syntax print(f "use {variable}")
print(f"Your Score is :{score} \n Your Height is : {height} \n Are You Winning ? : {is_winning}")

