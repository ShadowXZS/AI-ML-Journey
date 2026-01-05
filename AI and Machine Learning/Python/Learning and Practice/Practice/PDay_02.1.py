#BMI calculator with Weight Advice
height = float(input("Enter Your height (In Meters):"))
weight = float(input("Enter Your Weight (In KG) : "))
bmi= (weight/(height**2))
print("Your BMI is: "+str(bmi))
if bmi < 18.5:
    print("You are Underweight, Please Eat More Protein and Exercise.")
elif bmi >=18.5 and bmi < 25:
    print("You are Normal Weight, Keep Fit.")
elif bmi >= 25:
    print("You are Overweight, Please Cutdown on Carbs and Exercise.")
#Ending with else is optional ending the If Statement with elif is Okay.