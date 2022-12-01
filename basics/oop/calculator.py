import math


class Calculator:

    def sum(self, a, b):
        return a + b

    def difference(self, a, b):
        return a - b

    def factor(self, a, b):
        return a * b

    def divisor(self, a, b):
        return a / b

    def inverted(self, a):
        return 1 / a

    def factorial(self, a):
        return math.factorial(a)


calculator = Calculator()
