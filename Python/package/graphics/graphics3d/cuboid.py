"""Cuboid module."""


class Cuboid:
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height

    def area(self):               # total surface area
        l, b, h = self.length, self.breadth, self.height
        return 2 * (l * b + b * h + h * l)

    def perimeter(self):          # sum of all 12 edges
        return 4 * (self.length + self.breadth + self.height)
