class Fraction:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    def __mul__(self, other):
        return Fraction(self.dividend * other.dividend, self.divider * other.divider)

    def __add__(self, other):
        return Fraction((self.dividend * other.divider) + (self.divider * other.dividend ), self.divider * other.divider)

    def __sub__(self, other):
        return Fraction((self.dividend * other.divider) - (self.divider * other.dividend), self.divider * other.divider)

    def __eq__(self, other):
        if self.dividend/self.divider == other.dividend/other.divider:
            return True
        return False

    def __gt__(self, other):
        if self.dividend/self.divider > other.dividend/other.divider:
            return True
        return False

    def __lt__(self, other):
        if self.dividend/self.divider < other.dividend/other.divider:
            return True
        return False

    def __str__(self):
        return f"Fraction: {self.dividend}, {self.divider}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
