"""This script tells the user Heads or Tails"""
from random import randint

number = randint(0,1)
if number == 1:
  print('Heads')
else:
  print('Tails')
