"""
Object Oriented Programming
"""


class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the car: " + str(self.make))
        print("Model of the car: " + str(self.model))


print(Car.wheels)
c1 = Car('bmw', '550i')
c1.info()
print(c1.wheels)

c2 = Car('benz', 'E350')
c2.info()
print(c2.wheels)
