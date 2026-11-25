class Rectangle:
    def __init__(self, length, width):
        self.__length = length  
        self.__width = width        

    
    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def area(self):
        return self.__length * self.__width

    
    def __lt__(self, other):
        return self.area() < other.area()



r1 = Rectangle(4, 5)
r2 = Rectangle(6, 7)

print("Area of Rectangle 1:", r1.area())
print("Area of Rectangle 2:", r2.area())

if r1 < r2:
    print("Rectangle 1 is smaller than Rectangle 2")
else:
    print("Rectangle 1 is not smaller than Rectangle 2")
