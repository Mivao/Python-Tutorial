"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are strings, lists, tuples or dictionaries
"""

x = 0

while x < 10:
    print("Value of x is: " + str(x))
    x = x + 1

list_eg = []
num = 0

while num < 10:
    list_eg.append(num)
    num += 1
    print("Value of num is: " + str(num))

print(list_eg)
