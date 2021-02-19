'''
print (type('Creuzebeck reloaded'))
print (type(7))
print (type(True))
print (type(False))
print (type("True"))
print (type("false"))

print (bool("True"))
print (bool("False"))
print (bool(''))
print (bool(' '))
print (bool('creuzebeck'))

print (bool(7))
print (bool(1))
print (bool(0))
print (bool(-1))

print (1+1==3)
print (1+1==2)

print (3 == 4)
print (3 != 4)

print (3>4)
print (3<4)
print (3 >= 4)
print (3 <= 4)
'''

firstNumber = 5
secondNumber = 0
trueValue = True
falseValue = False

if firstNumber >1 and firstNumber <10:
    print ("The value is between 1 and 10.")
print (not trueValue)
print (not falseValue)

if not firstNumber >1 and secondNumber <10:
    print ("Both values pass the test")
else:
    print ("Both values do NOT pass the test")

