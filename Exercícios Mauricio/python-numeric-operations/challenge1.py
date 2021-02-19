
print('Enter the Fahrenheit temperature:' )
fahTemp = (input())

if fahTemp.isnumeric() == False:
    print ('Enter only numbers')
    exit()

fahTemp = int(fahTemp)

celsius = (fahTemp - 32) * 5/9
print('Temp in celsius is: ' + str(celsius))





    