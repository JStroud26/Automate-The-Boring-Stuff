#Take user input
print('Enter TB or GB for the advertised unit: ')
unit = input('>')

#Calculate the amount that the advertised capacity lies
if unit == 'TB' or unit == 'tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
    discrepancy = 1000000000 / 1073741824

print('Enter the advertised capacity')
advertised_cap = input('>')
advertised_cap = float(advertised_cap)

#Calculate real capacity, rounded to the nearest hundredth, convert to a string
real_cap = str(round(advertised_cap * discrepancy, 2))

print('The real capacity of your unit is ' + real_cap + ' ' + unit)
