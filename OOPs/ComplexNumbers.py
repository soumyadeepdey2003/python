class Compolex:
    def __init__(self, real=0, imaginary=0):
        self.r = real
        self.i = imaginary

    def use(self):
        return [self.r, self.i]

    def display(self):
        real, imag = self.r, self.i
        if imag == 0:
            print(f"{real}")
        elif imag > 0:
            print(f"{real} + {imag}i")
        else:
            print(f"{real} - {abs(imag)}i")

    @staticmethod
    def display_static(l):
        real, imag = l[0], l[1]
        if imag == 0:
            print(f"{real}")
        elif imag > 0:
            print(f"{real} + {imag}i")
        else:
            print(f"{real} - {abs(imag)}i")

    @staticmethod
    def sum(l1, l2):
        l3 = [l1[0]+l2[0], l1[1]+l2[1]]
        Compolex.display_static(l3)

    @staticmethod
    def mul(l1, l2):
        a, b = l1[0], l1[1]
        c, d = l2[0], l2[1]
        l3 = [a*c - b*d, a*d + b*c]
        Compolex.display_static(l3)


# Usage / Test cases:
a = Compolex(2, 3)
b = Compolex(1, -4)

print("Complex Number =")
a.display()
print("Complex Number =")
b.display()

print("Sum:")
Compolex.sum(a.use(), b.use())      

print("Product:")
Compolex.mul(a.use(), b.use())      
c = Compolex()
print("Complex Number =")
c.display()

d = Compolex(6)
print("Complex Number= ")
d.display()
