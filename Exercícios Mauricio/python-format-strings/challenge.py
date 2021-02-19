

first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
first_value = first_value.strip() #justifica
first_value = first_value.title() #todas iniciais maiusculas
first_value = f'{first_value:^30}' #centraliza dentro da cadeia de caracteres

# Second challenge
second_value = second_value.replace('-', '') #troca o traço por espaço vazio
second_value = second_value.strip() #justifica
second_value = second_value.capitalize() #somente a primeira maiuscula


# Third challenge
third_value = third_value.replace(' ', '') # tira espaços vazios
third_value = third_value.replace('-', ' ') #remove o traço
third_value = third_value.swapcase() #troca de caixa alta para caixa baixa
third_value = f'{third_value:>30}' #justifica à direita dentro da cadeia de 30 caracteres


print(first_value)
print(second_value)
print(third_value)

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value, fifth_value, sixth_value, sep='#', end='!') #enfileira os valores, adiciona um simbolo entre eles (sep ='#') e adiciona um caracter final (end='!')



# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print (f'\n\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}') # n pula linha e t adiciona tab

