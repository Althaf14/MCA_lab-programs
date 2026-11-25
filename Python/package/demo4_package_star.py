# Style 4: import * on the packages (loads modules listed in __all__)
from graphics import *
from graphics.graphics3d import *

r = rectangle.Rectangle(9, 2)
c = circle.Circle(1)
cb = cuboid.Cuboid(2, 2, 5)
s = sphere.Sphere(2)

for name, shape in [("Rectangle", r), ("Circle", c), ("Cuboid", cb), ("Sphere", s)]:
    print("%-10s: area = %.2f, perimeter = %.2f" % (name, shape.area(), shape.perimeter()))
