h = int(input("Height (in centimeters):"))
w = int(input("Weight (in kilograms):"))

bmi = w/((h*h)/10000)

print("Your BMI value is: ",bmi)

if bmi <= 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have healthy weight.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
