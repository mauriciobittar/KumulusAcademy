
#capitalizar iniciais da cadeia

'''
message = str.capitalize ('first message')
print (message)

message = 'second message'.capitalize()
print (message)

message = 'third message'
print(message.capitalize())
'''
#Alternar entre maiusculas e minusculas
'''
message = 'hello creuzebeck'
print (message.lower())
print (message.upper())

message = message.title()
print (message)
print (message.swapcase())
'''

#Conta qtd de um caractere em uma cadeia
'''
location = 'Mississippi'
print (location.count('s'))
'''

#Conta qtd de caractere total em uma cadeia
'''
print (len('Mississippi Queen'))
'''

#inspeciona a cadeia de caracteres e retorna se corresponde ao esperado no inicio e fim; retorna true/false
'''
message = 'racecar'
print (message.startswith('r'))
print (message.startswith('a'))
print (message.startswith('ra'))

print (message.endswith('r'))
print (message.endswith('a'))
print (message.endswith('ra'))
'''

#localiza uma cadeia de caracteres dentro de outra

'''
message = 'The quick brown fox jumps over the lazy black dog'
print (len(message)) #comprimento total da cadeia
print(message.find('q')) #posição do 'q' na cadeia, diferencia maiuscula/minuscula

print(message.find('t'))
print(message.find('T'))
'''

#remove espaços vazios nas cadeias de caracteres ( esq, dir e ambos os lados)
'''
message = '      middle       '
print ('.' + message.lstrip() + '.')
print ('.' + message.rstrip() + '.')
print ('.' + message.strip() + '.')
'''

#substitui uma cadeia de caracteres encontrada em outra cadeia
'''
message = 'brevity is the essence of wit'
message = message.replace('essence', 'soul')
print(message)
'''

#justifica adicionando caracteres de espaço vazio
'''
message = 'howdy'
print(message.rjust(20))
print(message.rjust(20, '-'))
print(message.ljust(20))
print(message.ljust(20, '-'))
'''