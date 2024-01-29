"""This script accepts inputs for weight and height, calculates the BMI
and outputs a custom message ased on the BMI value"""
# Enter your height in meters
height = float(input("Height: "))

# Enter your weight in kilograms
weight = int(input("Weight: "))

#Calculate the BMI
bmi = (weight / (height ** 2))

#Output custom message based on the value of bmi
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >= 25 and bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 30 and bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")