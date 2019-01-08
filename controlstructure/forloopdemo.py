"""
Execute statements repeatedly
Conditions are used tos top the execution of loops
Iterable items are strings, lists, tuples or dictionaries
"""
# String for loop
my_string = 'abcabc'

for c in my_string:
    if c == 'a':
        print('A', end=" ")
    else:
        print(c, end=" ")

print()

# List for loop
cars = ['bmw', 'benz', 'honda']

for car in cars:
    print(car)

nums = [1, 2, 3]
for n in nums:
    print(n * 10)

print('*' * 20)

# Dictionary for loop
dict_eg = {'one': 1, 'two': 2, 'three': 3}
for k in dict_eg:
    print(k + " " + str(dict_eg[k]))

print("*" * 20)

for k, v in dict_eg.items():
    print(k)
    print(v)

