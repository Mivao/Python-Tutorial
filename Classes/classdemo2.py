"""
Object Oriented Programming
"""


class Car(object):

    def __init__(self, make):
        self.make = make


c1 = Car('bmw')
print(c1.make)

c2 = Car('benz')
print(c2.make)
