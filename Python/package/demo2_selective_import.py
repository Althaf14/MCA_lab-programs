# Style 2: selective import (from ... import ...) and aliases
from graphics.rectangle import Rectangle
from graphics.circle import Circle
from graphics.graphics3d import cuboid                    # module only
from graphics.graphics3d.sphere import Sphere as Sph      # with alias

r = Rectangle(10, 4)
c = Circle(7)
cb = cuboid.Cuboid(6, 5, 4)
s = Sph(5)

print("Rectangle : area = %.2f, perimeter = %.2f" % (r.area(), r.perimeter()))
print("Circle    : area = %.2f, perimeter = %.2f" % (c.area(), c.perimeter()))
print("Cuboid    : area = %.2f, perimeter = %.2f" % (cb.area(), cb.perimeter()))
print("Sphere    : area = %.2f, perimeter = %.2f" % (s.area(), s.perimeter()))
