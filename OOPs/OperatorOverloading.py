class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # String representation
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Addition: v1 + v2
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    # Subtraction: v1 - v2
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    # Multiply by scalar: v * k
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector2D(self.x * scalar, self.y * scalar)
        # Vector multiplication (dot product)
        elif isinstance(scalar, Vector2D):
            return self.x * scalar.x + self.y * scalar.y

    # True division: v / k
    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Division by zero")
        return Vector2D(self.x / scalar, self.y / scalar)

    # Unary negation: -v
    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    # Equality: v1 == v2
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Not equal: v1 != v2
    def __ne__(self, other):
        return not self.__eq__(other)

    # Less than (by magnitude)
    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    # Greater than (by magnitude)
    def __gt__(self, other):
        return self.magnitude() > other.magnitude()

    # Length (absolute value): abs(v)
    def __abs__(self):
        return self.magnitude()

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # In-place add: v += w
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    # In-place multiply: v *= k
    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return self

# ------ MAIN WORKFLOW ---------
v1 = Vector2D(3, 4)
v2 = Vector2D(1, -2)

print("v1 =", v1)
print("v2 =", v2)

print("Addition v1 + v2 =", v1 + v2)
print("Subtraction v1 - v2 =", v1 - v2)
print("Negation -v1 =", -v1)
print("Scalar multiplication v1 * 2 =", v1 * 2)
print("Dot product v1 * v2 =", v1 * v2)
print("Division v1 / 2 =", v1 / 2)
print("Magnitude of v1 =", abs(v1))
print("Check v1 == v2:", v1 == v2)
print("Check v1 != v2:", v1 != v2)
print("Is v1 > v2? (by magnitude)", v1 > v2)
print("Is v1 < v2? (by magnitude)", v1 < v2)

v1 += v2
print("v1 after v1 += v2:", v1)

v2 *= 3
print("v2 after v2 *= 3:", v2)



"""
Operators Demonstrated:
__add__, __sub__, __mul__, __truediv__: arithmetic (+, -, *, /)
__eq__, __ne__, __lt__, __gt__: comparison (==, !=, <, >)
__neg__: unary (-)
__abs__: absolute value (abs())
__iadd__, __imul__: in-place operators (+=, *=)
__str__: for printing

"""
