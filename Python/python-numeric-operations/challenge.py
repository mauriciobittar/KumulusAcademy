fahr = input('What is the temperature in fahrenheit? ')

if fahr.isnumeric():
    celsius = (int(fahr) - 32) * 5/9
    celsius = int(celsius)
    print("Temperature in celsius is " + str(celsius))

else: print('Input is not a number')