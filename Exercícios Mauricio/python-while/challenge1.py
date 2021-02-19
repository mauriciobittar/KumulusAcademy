import random

roll = 0
count = 0

print('Number guesser 3000!!! ')
while roll !=5: 

    guess = input('Guess a number between 1 and 5: ')
    if guess >'5':
        print ('Enter a number equal or under 5.')

    elif guess.strip() == '':
        continue    
    count += 1
    roll = random.randint(1, 5)
else:
    print(f'You guessed it in {count} tries!')