# pylint: disable=too-few-public-methods missing-module-docstring
import math
class Shape:
    """A class representing a geometric shape."""

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def say_name(self):
        """Prints the name of the shape."""
        return(f"My name is {self.name}.")

class Rectangle(Shape):
    """A class representing a rectangle, inheriting from Shape."""

    def __init__(self, color, name, width, height):
        super().__init__(color, name)
        self.width = width
        self.height = height

    def say_name(self):
        """Prints the name of the rectangle."""
        return(f"My name is {self.name} and I am a {self.__class__.__name__.lower()}.")

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

class Circle(Shape):

    def __init__(self, color, name, radius):
        super().__init__(color, name)
        self.radius = radius

    def say_name(self):
        """Prints the name of the circle."""
        return(f"My name is {self.name} and I am a {self.__class__.__name__.lower()}.")

    def area(self):
        """Calculates the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates the perimeter of the circle."""
        return 2 * math.pi * self.radius

r = Rectangle("blue", "MyRectangle", 5, 10)
c = Circle("red", "MyCircle", 7)

print(f"Rectangle Area: {r.area()}")
print(f"Rectangle Perimeter: {r.perimeter()}")
print(r.say_name())

print(f"Circle Area: {c.area()}")
print(f"Circle Perimeter: {c.perimeter()}")
print(c.say_name())