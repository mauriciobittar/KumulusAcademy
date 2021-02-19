


#mesclagem da função format()
'''
medicine = 'Coughussin'
dosage = 5
duration = 4.5

#campos de substituição vazios, com valores atribuidos pela função format(), em ordem respectiva

instructions = '{} - Take {} ML by mouth every {} hours'.format(medicine, dosage, duration)
print(instructions)

#insere nos campos de substituição vazios os argumentos da função format(), os números entre as chaves indicam a posição do argumento dentro da função

instructions = '{2} - take {1} ML by mouth every {0} hours'.format(medicine, dosage, duration)
print (instructions)

#os campos de subtituição são preenchidos com nomes de variaveis que são passadas dentro da função format()

instructions = '{medicine} - Take {dosage} ML by mouth every {duration} hours'.format(medicine = 'Sneezergen', dosage = 10, duration = 6)

print(instructions)
'''

#f-strings

#campo de substituição com variavel atribuida
'''
name = ' Creuzebeck'
message = f'Atenção,{name}.'
print(message)

#f-string converte o tipo de dados da variável na saída, dispensa chamar str()

count = 10 
value = 3.14
message = f'Count to {count}. Multiply by {value}'
print(message)
'''

#expressões simples dentro do campo de substituição f-string (usar com cautela pois torna o código menos legível)
#ficar atento com parenteses e chaves abertos e fechados corretamente
'''
width = 5
heigth = 10

print(f'The perimeter is {(2 * width) + (2 * heigth)} and the area is {width * heigth}.')
'''


#especificadores de formato (:) para controlar alinhamento e preenchimento

value = 'hi'
# o dois pontos  (:) apos o nome da variavel especifica como o valor deve ser formatado
# o simbolo 'menor que (<)' alinha o texto à esquerda, 'maior que (>) alinha à direita, circunflexo (^) centraliza. 
# o traço antes do simbolo de alinhamnto preenche os espaços vazios. O valor 25 especifica o comprimento da cadeia de caracteres. 
# Os pontos ao lado do campo de substituição ajuda a ver a largura total da cadeia de caracteres

'''
print(f'.{value:<25}.')
print(f'.{value:>25}.')
print(f'.{value:^25}.')
print(f'.{value:-^25}.')
'''
