"""This script calculates the Love Scores and outputs a message based the score"""

print("The Love Calculator is calculating your score...")
name1 = input("Your Name: ") # What is your name?
name2 = input("Your Spouse Name: ") # What is their name?

names = name1 + name2
letters_in_true = 0
letters_in_love = 0

for letter in names.lower():
  if letter in "true":
    letters_in_true += 1
  if letter in "love":
    letters_in_love += 1
#print(str(letters_in_love) + " " + str(letters_in_true))

total_score = str(letters_in_true) + str(letters_in_love)
total_score = int(total_score)

if total_score < 10 or total_score > 90:
  print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
  print(f"Your score is {total_score}, you are alright together.")
else:
  print(f"Your score is {total_score}.")