"""This script accets the weight (kgs) and height (m) and calculates the BMI"""

"""Input the height"""
height = input("Height: ")

"""Input the weight"""
weight = input("Weight: ")

"""Calculate the BMI and print result as an integer"""
bmi = float(weight) // (float(height) ** 2)

"""Print the bmi"""
print(int(bmi))
