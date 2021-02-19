
#(type(VALOR)) imprime o tipo do valor inserido (int, str, float, etc.)

# print (type('7'))
# print (type(7))
# print (type(7.1))

#isinstance() retorna booleano ao verificar o tipo do valor inserido
'''
print(isinstance('7', str))
print(isinstance(7, int))
print(isinstance(7.1, float))

print(isinstance(7, str))
print(isinstance('7', int))
print(isinstance('7.1', float))
'''

### O tipo de dados compõe o valor e não a variável. Uma variável pode assumir qlq valor independente do tipo de dados

x = 'a string'
print(type(x))
x = 7
print(type(x))
x = False
print(type(x))


