class parameters():
    Base = ""
    Height = ""
    def __init__(self,base,height):
        self.Base = base
        self.Height = height
    def Area(self):
        area = 0.5*self.Base*self.Height
        print("Area of the triangle is:",area)


t1 = parameters(10,20)
t1.Area()
t2 = parameters(20,30)
t2.Area()
