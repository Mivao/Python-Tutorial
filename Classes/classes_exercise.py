
class Fruit(object):
    def __init__(self):
        print("You've made a fruit, you tree motherfucker.")

    def nutrition(self):
        print("Your fruit is nutritious ;)")

    def fruit_shape(self):
        print("Aesthetic af m8")


class Orange(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print("You made citrus? Questionable.")

    def nutrition(self):
        Fruit.nutrition(self)
        print("Can't get scurvy now")

    def color(self):
        print("What did you expect, it's orange")


f1 = Fruit()
o1 = Orange()

f1.nutrition()
f1.fruit_shape()

o1.nutrition()
o1.color()
o1.fruit_shape()

