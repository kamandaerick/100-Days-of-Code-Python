"""This script accepts a year and checks if it is a leap year or not"""
year = int(input("Year: "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"{year} is Leap")
    else:
      print(f"{year} is not Leap")
  else:
    print(f"{year} is Leap")
else:
  print(f"{year} is not Leap")

