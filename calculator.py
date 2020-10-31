import math


class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def exponentiation(self, x, y):
        return x ** y

    def inverse(self, x):
        return 1 / x

    def invert_sign(self, x):
        return -x

    def display_error(self):
        return 'Error!'

    def sine(self, x):
        return math.sin(x)

    def cosine(self, x):
        return math.cos(x)

    def tangent(self, x):
        return math.tan(x)

    def inverse_sine(self, x):
        return math.asin(x)

    def inverse_cosine(self, x):
        return math.acos(x)

    def inverse_tan(self, x):
        return math.atan(x)

    def factorial(self, x):
        return math.factorial(x)

    def absolute_value(self, x):
        return abs(x)
