# Style 3: import * (names come from each module; uses __all__ in packages)
from graphics.rectangle import *
from graphics.circle import *
from graphics.graphics3d.cuboid import *
from graphics.graphics3d.sphere import *

shapes = {
    "Rectangle": Rectangle(8, 6),
    "Circle": Circle(2.5),
    "Cuboid": Cuboid(3, 3, 3),
    "Sphere": Sphere(1.5),
}
for name, shape in shapes.items():
    print("%-10s: area = %.2f, perimeter = %.2f" % (name, shape.area(), shape.perimeter()))
