basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print ('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra') # a set of unique letters in the string
b = set('alacazam')

print(a)
print(b)

# letters in a but not in b
print("letters in a but not in b", a - b)

# letters in a or b
print("letters in a or b", a | b)

# letters in a and b
print("letters in a and b", a & b)

# letters in a or b but not in both
print("letters in a or b but not in both", a ^ b)
