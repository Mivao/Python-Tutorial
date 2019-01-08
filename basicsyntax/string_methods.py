"""
Examples to show available string methods in Python
"""

# Accessing characters in a string
# Index starts from 0
first = "nyc"[0]
city = "sfo"
print(first)
ft = city[0]
print(ft)

"""
len()
lower()
upper()
str()
"""

stri = "This is a Mixed Case"
print(stri.lower())
print(stri.upper())
print(len(stri))

print(stri + str(2))

"""
Concatenation
"""
print("Hello " + " " " World !!!")
print(first + " " + city)


