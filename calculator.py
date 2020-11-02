import math
import switch_mode as switch

class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        if y == 0:
            return Calculator.display_error(self)
        else:
            return x / y

    def sqr(self, x):
        return x ** 2

    def sqroot(self, x):
        if x < 0:
            return Calculator.display_error(self)
        else:
            return round(math.sqrt(x), 4)

    def exponentiation(self, x, y):
        return x ** y

    def inverse(self, x):
        if x == 0:
            return Calculator.display_error(self)
        else:
            return 1 / x

    def invert_sign(self, x):
        return -x

    def display_error(self):
        return 'Error!'

    def sine(self, x, mode):
        if mode == "degrees":
            x = switch.angle_conversion("radians", x)
            print("radians: " + str(x))
        return float(f"{math.sin(x):0.5}")

    def cosine(self, x, mode):
        if mode == "degrees":
            x = switch.angle_conversion("radians", x)
            print("radians: " + str(x))
        return float(f"{math.cos(x):0.5}")

    def tangent(self, x, mode):
        if mode == "degrees":
            x = switch.angle_conversion("radians", x)
            print("radians: " + str(x))
        return float(f"{math.tan(x):0.5}")

    def inverse_sine(self, x, mode):
        if x > 1 or x < -1:
            return Calculator.display_error(self)
        elif mode == "degrees":
            x = switch.angle_conversion("radians", x)
            print("radians: " + str(x))
        else:
            return float(f"{math.asin(x):0.5}")

    def inverse_cosine(self, x, mode):
        if x > 1 or x < -1:
            return Calculator.display_error(self)
        elif mode == "degrees":
            x = switch.angle_conversion("radians", x)
            print("radians: " + str(x))
        else:
            return float(f"{math.acos(x):0.5}")

    def inverse_tan(self, x, mode):
        if mode == "degrees":
            x = switch.angle_conversion("radians", x)
            print("radians: " + str(x))
        return float(f"{math.atan(x):0.4}")

    def factorial(self, x):
        if x < 0:
            return Calculator.display_error(self)
        else:
            return math.factorial(x)

    def absolute_value(self, x): #no yet
        return abs(x)

    def log(self, x):
        return round(math.log10(x), 4)

    def ilog(self, x):
        return 10 ** x

    def nlog(self, x):
        return round(math.log(x), 4)

    def inlog(self, x):
        return round(math.exp(x), 4)

    def floor(self,x):
        return math.floor(x)

    def ceil(self,x):
        return math.ceil(x)

    def m_plus(self, memory, memory_store):
        import importlib
        main_app = importlib.import_module("main-app")

        memory_store[0] = memory.pop()
        print(str(memory_store[0]) + " was added to memory." + "\n")

    def m_reset(self, memory, memory_store):

        memory.clear()
        memory_store.clear()
        memory.append(0)
        memory_store.append(0)
        print("Memory was cleared")
        #main_app.displayResult(0)

    def m_recall(self, memory_store):
        import importlib
        main_app = importlib.import_module("main-app")

        stored_value = memory_store[0]
        main_app.displayResult(stored_value)


