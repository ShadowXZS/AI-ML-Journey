#Tip Calculator
print("Lets Calculate Tip and Your Share of the Bill:")
total = float(input("What was the Total Bill: ₹ "))
tip_percentage = float(input("How much tip would you like to give ? 10% / 12% / 15% ? "))
total_people = int(input("How many people split the bill ? "))
bill_with_tip = (total + (total*(tip_percentage/100)) )
your_share = (total + (total*(tip_percentage/100)) )/ total_people
#print(f"Your Share is {round(your_share,2)}") This fails because it drops trailing zeros.
print(f"Your Bill Total with tip is ₹ {bill_with_tip:.2f}")
print(f"Your Share is ₹{your_share:.2f}")
#Equation was a Bit off, Verified the Calculation on Calculator and Corrected it
#Use :.2f inside f-strings for currency to force 2 decimal places (e.g., 10.5 -> 10.50); round() fails because it drops trailing zeros.