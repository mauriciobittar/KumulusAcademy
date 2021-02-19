print('Simple calculator')

firstNumber = input('Enter the first number: ') #declara a variavel e já printa a solicitação de valor pelo usuario

if firstNumber.isnumeric() == False:  #testa o valor inserido, se é um numero, se nao for encerra o programa
    print('Enter only numbers.')
    exit()

operation = input('Operation: ') #declara a variavel operação e printa solicitação de entrada

secondNumber = input('Enter the second number: ')

if secondNumber.isnumeric() == False:
    print('Enter only numbers.')
    exit()

firstNumber = int(firstNumber)
secondNumber = int(secondNumber)

result = 0
if operation == '+':
    result = firstNumber + secondNumber
    label = 'sum'
elif operation == '-':
    result = firstNumber - secondNumber
    label = 'difference'
elif operation == '*':
    result = firstNumber * secondNumber
    label = 'product'
elif operation == '/':
    result = firstNumber / secondNumber
    label = 'quotient'
elif operation == '**':
    result = firstNumber ** secondNumber
    label = 'exponent'
elif operation == '%':
    result = firstNumber % secondNumber
    label = 'modulus'
else:
    print ('Operation not recognized.')
    exit()

print(label + ' of ' + str(firstNumber) + ' ' + operation + ' ' + str(secondNumber) + ' equals ' + str(result))





