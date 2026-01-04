#BMI calculator
height = float(input("Enter Your height (In Meters):"))
weight = float(input("Enter Your Weight (In KG) : "))
bmi= (weight/(height**2))
print("Your BMI is: "+str(bmi))
#Always convert the Float or Int Value to Str if you wish to concat the value with print.