"""Ask the user to enter a two digit number"""
two_digit_number = input("Enter a two-digit number: ")
"""Inputs are usually strings. Convert them to integers and perfom the summation"""
result = int(two_digit_number[0]) + int(two_digit_number[1])
"""Print out the output"""
print(result)