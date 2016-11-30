class Rational():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def printMe(self):
        print self.numerator, "/", self.denominator

    def reduce(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __rmul__(self,other):
        newRational = Rational(other,1)
        return newRational * self

    def __mul__(self, other):
        newNumerator = self.numerator * other.numerator
        newDenominator = self.denominator * other.denominator
        return Rational(newNumerator, newDenominator)

    def __div__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __repr__(self):
        return str(self.numerator) + '/' + str(self.denominator)

half = Rational(1,2)
anotherHalf = Rational(2,4)

print half * anotherHalf
print 1 * half
