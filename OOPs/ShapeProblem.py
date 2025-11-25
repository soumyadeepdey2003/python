from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def display(self):
        print(f"Area: {self.area():.2f}")
        print(f"Perimeter: {self.perimeter():.2f}")
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Polygon(Shape):
    def __init__(self, n_sides, side_length):
        self.n = n_sides
        self.a = side_length
    def perimeter(self):
        return self.n * self.a
    def area(self):
        if self.n < 3:
            return 0
        return (self.n * (self.a ** 2)) / (4 * math.tan(math.pi / self.n))

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def perimeter(self):
        return 2 * (self.length + self.width)
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.a = radius
    def perimeter(self):
        return 2 * math.pi * self.a
    def area(self):
        return math.pi * self.a * self.a

poly = Polygon(5, 6)
rect = Rectangle(4, 7)
circ = Circle(3)

print("Polygon:")
poly.display()
print("\nRectangle:")
rect.display()
print("\nCircle:")
circ.display()
