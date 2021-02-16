# import random

# value = random.randint(1, 5)
# guess = 0
# count = 0
# while guess != value:
#     guess = int(input("Guess a number between 1 and 5 "))
#     count += 1

# print(f"You guessed it in {count} tries!")

import random

value = random.randint(1, 15)
guess = 0
count = 0
while guess != value:
    guess = int(input("Guess a number between 1 and 15 "))
    if guess < value:
        print("Your guess is too low")
    elif guess > value:
        print("Your guess is too high")
    count += 1

print(f"You guessed it in {count} tries!")

