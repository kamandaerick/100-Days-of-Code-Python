"""This script creates a game of finding a treasure"""
print("Welcome to Treasure Island. Your mission is to find the treasure.")

direction = input("Where would you like to go first? Left or Right? ")
if direction == "Right":
  print("Game Over")
  exit()
else:
  swim_or_wait = input("Would you like to Swim o Wait? ")
  if swim_or_wait == "Swim":
    print("Game Over")
    exit()
  else:
    chosen_door = input("Which door would you like to enter? Red, Blue, or Yellow? ")
    if chosen_door == "Blue" or chosen_door == "Red":
      print("Game over")
      exit()
    else:
      print("You win.")
