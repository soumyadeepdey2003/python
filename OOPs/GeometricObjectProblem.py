from abc import ABC, abstractmethod
import math

class GeometricObject(ABC):
    def __init__(self, colour, weight):
        self.colour = colour
        self.weight = weight

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def circumference(self):
        pass

    def display(self):
        print(f"Colour: {self.colour}")
        print(f"Weight: {self.weight}")
        print(f"Area: {self.area():.2f}")
        print(f"Circumference: {self.circumference():.2f}")

class Circle(GeometricObject):
    def __init__(self, radius, colour, weight):
        super().__init__(colour, weight)
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return 2 * math.pi * self.radius

class Triangle(GeometricObject):
    def __init__(self, a, b, c, colour, weight):
        super().__init__(colour, weight)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def circumference(self):
        return self.a + self.b + self.c

# Main
circ = Circle(4, "red", 2.5)
tri = Triangle(3, 4, 5, "blue", 1.8)
print("Circle:")
circ.display()
print("\nTriangle:")
tri.display()
