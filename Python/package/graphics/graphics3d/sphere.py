"""Sphere module."""
import math


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def area(self):               # surface area
        return 4 * math.pi * self.radius ** 2

    def perimeter(self):          # circumference of a great circle
        return 2 * math.pi * self.radius
