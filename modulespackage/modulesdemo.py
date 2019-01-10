"""
https://docs.python.org/3/library/
"""

from math import sqrt
# import modulesexternal.car as car
from modulesexternal.car import info


class ModulesDemo():

    def builtin_modules(self):
        print(sqrt(100))

    def car_description(self):
        make = 'bmw'
        model = '550i'
        info(make, model)


m = ModulesDemo()
m.builtin_modules()
m.car_description()
