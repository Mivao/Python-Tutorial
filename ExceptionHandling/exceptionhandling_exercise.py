
car = {'make': 'bmw', 'model': '550i', 'year': '2016'}

try:
    colour = car[colour]

except NameError:
    print("This is not one of the keys")

finally:
    print("We've finished the exercise")


