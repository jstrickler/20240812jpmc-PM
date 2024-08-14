fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"{fruits[1] = }")
print(f"{fruits[0] = }")
print(f"{fruits[-1] = }")

print(f"{fruits[0:3] = }")

#  S[start-at:stop-before:count-by]

print(f"{fruits[:3] = }")
print(f"{fruits[4:9] = }")
print(f"{fruits[-5:] = }")
print(f"{fruits[1:-1] = }")

s = """'in quotes'"""
print(s)
print(s[1:-1])

print(f"{fruits[::2] = }")

a = [1, 2, 3]
b = a[::] 
c = a
print('-' * 60)

for fruit in fruits:
    #  fruit = fruits[0]
    #  fruit = fruits[1]
    #  ...
    print(fruit.upper())

# for VAR in ITERABLE:
#     ...use VAR...

x = "abc"
for letter in x:
    print(letter)
