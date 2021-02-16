print("Simple calculator!")
first = input("First number ")
operation = input("Operation number ")
second = input("Second number ")

if operation == '*':
    result = int(first) * int(second)
    result = int(result)
    operationName = 'product'
elif operation == '/':
    result = int(first) / int(second)
    result = int(result)
    operationName = 'quotient'
elif operation == '+':
    result = int(first) + int(second)
    result = int(result)
    operationName = 'sum'
elif operation == '-':
    result = int(first) - int(second)
    result = int(result)
    operationName = 'diference'
elif operation == '%':
    result = int(first) % int(second)
    result = int(result)
    operationName = 'modulus'
elif operation == '**':
    result = int(first) ** int(second)
    result = int(result)
    operationName = 'exponent'
else:
    print("operation not recognized")

print(operationName, "of", str(first),operation, str(second), "equals", str(result))
