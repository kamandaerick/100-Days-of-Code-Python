#!/usr/bin/python3
"""This calculator calculates the bill to be paid by each person
based on the percentage of tip they choose"""

"""Welcome note"""
print("Welcome to the tip calculator.")

"""Enter the total bill"""
total_bill = input("What was the total bill? $")

"""Enter the number of people to split the bill"""
people_to_split = input("How many people are going to split the bill? ")

"""Calculating the tip"""
tip_percentage = input("What percentage tip would you like to give? Enter any value between 1 and 100. ")

bill_after_tip = float(total_bill) + (float(total_bill) * int(tip_percentage) / 100)

"""Bill per person in 2 decimal places"""
bill_per_person = round((bill_after_tip / int(people_to_split)), 2)

"""Print the bill per person"""
print(f"Each person should pay: ${bill_per_person}")