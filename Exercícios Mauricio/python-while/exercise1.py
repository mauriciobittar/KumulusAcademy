import random

roll = 0
count = 0

print('First person to roll a 5 wins')
while roll !=5: #enquanto roll for diferente de 5, a saída é TRUE, quando for igual será FALSE 

    name = input('Enter a name, or \'q\' to quit: ')
    if name.strip() == '':
        continue
    
    if name.strip() == 'q':
        break
        
        #break #quando atendida a função que aciona o break o programa sai do loop while e o else é ignorado pois o while nao foi atendido
    count = count + 1
    roll = random.randint(1, 5)
    print(f'{name} rolled {roll}')
else:
    print(f'{name} Wins')


print(f'You rolled the dice {count} times.')
