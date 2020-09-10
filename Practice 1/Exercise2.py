

class shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2
    def Area(self):
        pass


class Triangle(shape):
    def Area(self):
        Area = 0.5 * self.dim1 * self.dim2
        print("Area of the triangle:",Area)

class Rectangle(shape):
    def Area(self):
        Area = self.dim1 * self.dim2
        print("Area of the rectangle:",Area)


t1 = Triangle(10,20)
t1.Area()
r1 = Rectangle(10,20)
r1.Area()