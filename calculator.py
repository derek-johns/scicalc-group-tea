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

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

    def sqr(self, x):
        return x ** 2

    def sqroot(self, x):
        return round(math.sqrt(x), 4)

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
        #print(last_value)
        main_app.displayResult(memory_store[0])
        print("was added to memory." + "\n")

    def m_reset(self, memory, memory_store):
        #import importlib
        #main_app = importlib.import_module("main-app")

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

    def switch_display_list(self, mode):
        print("You are in " + mode)
        modes = ["decimal", "hexadecimal", "binary", "octal"]
        index = modes.index(mode)


    def switch_display_input(self, mode):
        import importlib
        main_app = importlib.import_module("main-app")

        print("You are in " + mode)
        new_mode = input("Input a new mode. \n")
        modes = ["decimal", "hexadecimal", "binary", "octal"]
        if new_mode in modes:
            print("You have switched to " + new_mode + ".")
            main_app.mode = new_mode
        else:
            print("That is not a valid mode.")



# add lots more methods to this calculator class.
    #def mul(self, ):

