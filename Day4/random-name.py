import random
names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']

random_name = names[random.randint(0, len(names) - 1)]

print(f"{random_name} is going to buy the meal today.")