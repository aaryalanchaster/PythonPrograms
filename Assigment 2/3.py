# calculator
class calculator:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a

    def __sub__(self, other):
        return self.a - other.a

    def __mul__(self, other):
        return self.a * other.a

    def __truediv__(self, other):
        if other.a == 0:
            print('wrong input')
        else:
            return self.a / other.a

    def __mod__(self, other):
        if other.a == 0:
            print('wrong input')
        else:
            return self.a % other.a


n1 = calculator(3)
n2 = calculator(4)
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
print(n1 % n2)
