'''
firstString = 'A literal string'
secondString = 'A literal string'
print (secondString == firstString)
'''
'''
thirdString = 'A single quoted literal string with a "double quote'
fourthString = "A double quoted literal string with a 'single quote"
print (thirdString)
print (fourthString)
'''
'''
fifthString = 'A single quoted literal string with an \' escaped single quote'
sixthString = "A double quoted literal string with a \" double quote"
seventhString = 'A literal string with a \n new line character'
eighthString = 'A literal string with a \t tab character'

print (fifthString)
print (sixthString)
print (seventhString)
print (eighthString)
'''
'''
ninthString = r"A literal string with a \n new line character printed raw"
print (ninthString)
'''

'''
tenthString = """A literal string
on more than one line
sometimes known as a verbatim string"""

eleventhString = """Another literal string
    on more than one line
using double quotes"""
print (tenthString)
print (eleventhString)
'''

first = 'Conrad'
second = 'Grant'
third = 'Bob'
print (first, second)
print (first, second, third)
print (first, second, third, sep= '-')
print (first, second, third, sep='-', end='.')

