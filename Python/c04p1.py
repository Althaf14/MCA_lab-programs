class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()



r1 = Rectangle(5, 4)
r2 = Rectangle(6, 3)

print("Rectangle 1: area =", r1.area(), ", perimeter =", r1.perimeter())
print("Rectangle 2: area =", r2.area(), ", perimeter =", r2.perimeter())

if r1 > r2:
    print("Rectangle 1 has the larger area")
elif r1 < r2:
    print("Rectangle 2 has the larger area")
else:
    print("Both rectangles have equal area")
