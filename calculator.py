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
        return math.sqrt(x)

    def log(self, x):
        return math.log10(x)

    def ilog(self, x):
        return 10 ** x

    def nlog(self, x):
        return math.log(x)

    def inlog(self, x):
        return math.exp(x)

    def floor(self,x):
        return math.floor(x)

    def ceil(self,x):
        return math.ceil(x)




# add lots more methods to this calculator class.
    #def mul(self, ):