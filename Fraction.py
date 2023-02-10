class Fraction:
    """Fraction calculator"""
    def __init__(self, *args):
        if len(args) == 1:
            numerator, denominator = [int(value) for value in args[0].split('/')]
        else:
            numerator, denominator = args
        if not (numerator < 0 and denominator < 0) and (numerator < 0 or denominator < 0):
            self.sign = -1
        else:
            self.sign = 1
        self.num, self.denom = abs(numerator), abs(denominator)
        self._reduction()

    @staticmethod
    def _greatest_common_divisor(a, b):
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return a + b

    def _smallest_common_multiple(self, a, b):
        return a // self._greatest_common_divisor(a, b) * b

    def _reduction(self):
        divisor = self._greatest_common_divisor(self.num, self.denom)
        self.num //= divisor
        self.denom //= divisor

    def numerator(self, number=None):
        if number is None:
            return self.num
        if number < 0:
            self.sign *= -1
        self.num = abs(number)
        self._reduction()

    def denominator(self, number=None):
        if number is None:
            return self.denom
        if number < 0:
            self.sign *= -1
        self.denom = abs(number)
        self._reduction()

    def __str__(self):
        return f"{self.sign * self.num}/{self.denom}"

    def __repr__(self):
        return f"Fraction('{self.sign * self.num}/{self.denom}')"

    def __neg__(self):
        return Fraction(-self.sign * self.num, self.denom)

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        num = self.sign * self.num * other.denom + other.sign * other.num * self.denom
        denom = self.denom * other.denom
        return Fraction(num, denom)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        num = self.sign * self.num * other.denom - other.sign * other.num * self.denom
        denom = self.denom * other.denom
        return Fraction(num, denom)

    def __iadd__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        num = self.sign * self.num * other.denom + other.sign * other.num * self.denom
        denom = self.denom * other.denom
        if num < 0:
            self.sign = -1
            num *= -1
        self.num, self.denom = num, denom
        self._reduction()
        return self

    def __isub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        num = self.sign * self.num * other.denom - other.sign * other.num * self.denom
        denom = self.denom * other.denom
        if num < 0:
            self.sign = -1
            num *= -1
        self.num, self.denom = num, denom
        self._reduction()
        return self

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        num = self.sign * other.sign * self.num * other.num
        denom = self.denom * other.denom
        return Fraction(num, denom)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        num = self.sign * other.sign * self.num * other.denom
        denom = self.denom * other.num
        return Fraction(num, denom)

    def __imul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        num = self.sign * other.sign * self.num * other.num
        denom = self.denom * other.denom
        if num < 0:
            self.sign = -1
            num *= -1
        self.num, self.denom = num, denom
        self._reduction()
        return self

    def __itruediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        num = self.sign * other.sign * self.num * other.denom
        denom = self.denom * other.num
        if num < 0:
            self.sign = -1
            num *= -1
        self.num, self.denom = num, denom
        self._reduction()
        return self

    def reverse(self):
        self.num, self.denom = self.denom, self.num
        self._reduction()
        return self