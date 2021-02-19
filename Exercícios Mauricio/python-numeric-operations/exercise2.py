
#verifica se a string pode ser convertida para int ou float e retorna true/false

'''
numericValue = '7'
print(numericValue.isnumeric())

stringValue = 'qwerty'
print(stringValue.isnumeric())
'''


firstValue = input('First Number: ')

if firstValue.isnumeric() == False:
    print('Value is not a number.')
    exit()

secondValue = input('Second Number: ')

if secondValue.isnumeric() == False:
    print('Value is not a number')
    exit()

firstValue = int(firstValue)
secondValue = int(secondValue)

sum = firstValue + secondValue
print('Sum: ' + str(sum))

#exemplo anterior utilizando operador lógico OR
'''
firstValue = input('First Number: ')
secondValue = input('Second Number: ')

if firstValue.isnumeric() == False or secondValue.isnumeric() == False:
    print('Please enter numbers only.')
    exit()

firstValue = int(firstValue)
secondValue = int(secondValue)

sum = firstValue + secondValue
print('Sum: ' + str(sum))
'''