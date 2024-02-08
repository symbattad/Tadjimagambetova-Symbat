class Myshape:
    def __init__(self,color,isfilled):
        self.color = color
        self.isfilled = isfilled
    def __str__(self,color,isfilled):
        print(f"{self.color}({self.isfilled})")
circle=Myshape("white",True)

print(circle.color)
print(circle.isfilled)


  