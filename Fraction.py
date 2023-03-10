class Fraction:
    """Fraction calculator"""
    def __init__(self, *args):
        if len(args) == 1 and self._is_number(args[0]):
            numerator = int(args[0])
            denominator = 1
        elif len(args) == 1:
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
    def _is_number(str):
        try:
            int(str)
            return True
        except ValueError:
            return False

    @staticmethod
    def _greatest_common_divisor(a, b):
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return a + b

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
        if isinstance(other, Fraction):
            num = self.sign * self.num * other.denom + other.sign * other.num * self.denom
            denom = self.denom * other.denom
        elif isinstance(other, int):
            num = self.sign * self.num + other * self.denom
            denom = self.denom
        else:
            raise TypeError
        return Fraction(num, denom)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            num = self.sign * self.num * other.denom - other.sign * other.num * self.denom
            denom = self.denom * other.denom
        elif isinstance(other, int):
            num = self.sign * self.num - other * self.denom
            denom = self.denom
        else:
            raise TypeError
        return Fraction(num, denom)

    def __rsub__(self, other):
        return -self.__sub__(other)

    def __iadd__(self, other):
        if isinstance(other, Fraction):
            num = self.sign * self.num * other.denom + other.sign * other.num * self.denom
            denom = self.denom * other.denom
        elif isinstance(other, int):
            num = self.sign * self.num + other * self.denom
            denom = self.denom
        else:
            raise TypeError

        if num < 0:
            self.sign = -1
            num *= -1

        self.num, self.denom = num, denom
        self._reduction()
        return self

    def __isub__(self, other):
        if isinstance(other, Fraction):
            num = self.sign * self.num * other.denom - other.sign * other.num * self.denom
            denom = self.denom * other.denom
        elif isinstance(other, int):
            num = self.sign * self.num - other * self.denom
            denom = self.denom
        else:
            raise TypeError

        if num < 0:
            self.sign = -1
            num *= -1

        self.num, self.denom = num, denom
        self._reduction()
        return self

    def __mul__(self, other):
        if isinstance(other, Fraction):
            num = self.sign * other.sign * self.num * other.num
            denom = self.denom * other.denom
        elif isinstance(other, int):
            num = self.sign * other * self.num
            denom = self.denom
        else:
            raise TypeError
        return Fraction(num, denom)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            num = self.sign * other.sign * self.num * other.denom
            denom = self.denom * other.num
        elif isinstance(other, int):
            num = self.sign * self.num
            denom = self.denom * other
        else:
            raise TypeError
        return Fraction(num, denom)

    def __rtruediv__(self, other):
        return self.__truediv__(other).reverse()

    def __imul__(self, other):
        if isinstance(other, Fraction):
            num = self.sign * other.sign * self.num * other.num
            denom = self.denom * other.denom
        elif isinstance(other, int):
            num = self.sign * other * self.num
            denom = self.denom
        else:
            raise TypeError

        if num < 0:
            self.sign = -1
            num *= -1

        self.num, self.denom = num, denom
        self._reduction()
        return self

    def __itruediv__(self, other):
        if isinstance(other, Fraction):
            num = self.sign * other.sign * self.num * other.denom
            denom = self.denom * other.num
        elif isinstance(other, int):
            num = self.sign * self.num
            denom = self.denom * other
        else:
            raise TypeError

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

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.sign * self.num / self.denom == other.sign * other.num / other.denom
        elif isinstance(other, int):
            return self.sign * self.num / self.denom == other
        else:
            raise TypeError

    def __ne__(self, other):
        if isinstance(other, Fraction):
            return self.sign * self.num / self.denom != other.sign * other.num / other.denom
        elif isinstance(other, int):
            return self.sign * self.num / self.denom != other
        else:
            raise TypeError

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.sign * self.num / self.denom < other.sign * other.num / other.denom
        elif isinstance(other, int):
            return self.sign * self.num / self.denom < other
        else:
            raise TypeError

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.sign * self.num / self.denom > other.sign * other.num / other.denom
        elif isinstance(other, int):
            return self.sign * self.num / self.denom > other
        else:
            raise TypeError

    def __le__(self, other):
        if isinstance(other, Fraction):
            return self.sign * self.num / self.denom <= other.sign * other.num / other.denom
        elif isinstance(other, int):
            return self.sign * self.num / self.denom <= other
        else:
            raise TypeError

    def __ge__(self, other):
        if isinstance(other, Fraction):
            return self.sign * self.num / self.denom >= other.sign * other.num / other.denom
        elif isinstance(other, int):
            return self.sign * self.num / self.denom >= other
        else:
            raise TypeError