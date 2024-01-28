"""This scripts calculates the number of weeks left to live.
It assumes a lifespan of 90"""

"""Accept age from user input"""
current_age = input("Current age: ")

"""Get the remaining years and convert to weeks"""
years_remaining = 90 - int(current_age)

weeks_remaining = years_remaining * 52

"""Print out the weeks remainining"""
print(f"You have {weeks_remaining} weeks left.")