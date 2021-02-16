first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
first_value = str.strip(first_value)
first_value = str.title(first_value)

# Second challenge
second_value = str.replace(second_value, '-', '')
second_value = str.strip(second_value)
second_value = str.capitalize(second_value)

# Third challenge
third_value = str.replace(third_value," ", "")
third_value = str.replace(third_value,"-", " ")
third_value = str.capitalize(third_value)

print('\t', first_value)
print(second_value)
print('\t\t', third_value)

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value + '#' + fifth_value + '#' + sixth_value + '!')

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print('\t' + fourth_value + '\n' + '\t' + fifth_value + '\n' + '\t' + sixth_value)