"""
Examples to show available string methods in python
"""

# Replace method
a = "1abc2abc3abc4abc"
print(a.replace('abc', 'ABC', 2))

# Sub-Strings
# Starting index is inclusive
# Ending index is exclusive
sub = a[1:6]
step = a[1:6:2]

print("*******************************")

print(sub)
print(step)
