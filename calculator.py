import math

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




# add lots more methods to this calculator class.
    #def mul(self, ):