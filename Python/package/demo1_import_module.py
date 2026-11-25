# Style 1: import the whole module (full dotted path)
import graphics.rectangle
import graphics.circle
import graphics.graphics3d.cuboid
import graphics.graphics3d.sphere

r = graphics.rectangle.Rectangle(5, 3)
c = graphics.circle.Circle(4)
cb = graphics.graphics3d.cuboid.Cuboid(4, 3, 2)
s = graphics.graphics3d.sphere.Sphere(3)

print("Rectangle : area = %.2f, perimeter = %.2f" % (r.area(), r.perimeter()))
print("Circle    : area = %.2f, perimeter = %.2f" % (c.area(), c.perimeter()))
print("Cuboid    : area = %.2f, perimeter = %.2f" % (cb.area(), cb.perimeter()))
print("Sphere    : area = %.2f, perimeter = %.2f" % (s.area(), s.perimeter()))
