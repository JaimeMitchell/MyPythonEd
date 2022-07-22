class Rectangle:
    def __init__(self, c, l, w):
        self.color = c
        self.length = l
        self.width = w

    def area(self):
        self.area = self.length * self.width
        return self.area

    def per(self):
        self.perimeter = 2 * self.length + 2 * self.width
        return self.perimeter

    def diag(self):
        self.diagonal = (self.width**2 + self.length**2) ** (1/2)
        return round(self.diagonal,2)
    
    def volume(self, h):
        self.height=h
        vol=self.length*self.height*self.width
        return vol



myRect1 = Rectangle('red', 2, 1)
myRect2 = Rectangle('blue', 4, 2)
myRect3 = Rectangle('green', 5, 6)

print(myRect1.color)
print(f'myRect 1 color is {myRect1.color}')
print(f'myRect 2 color is {myRect2.color}')
print(f'myRect 1 length is {myRect1.length}')
print(f'myRect 2 length is {myRect2.length}')
print(f'myRect 1 width is {myRect1.width}')
print(f'myRect 2 width is {myRect2.width}')

# calling methods
print(f'myRect 1 width is {myRect1.area()}')
area = myRect2.area()
print(f'myRect 2 area is {area}')
print('myRect1 diagonal= ', myRect3.diag())
print(f'myRect 1 volume is {myRect1.volume(5)}')
volume=myRect2.volume(5)
print(volume)
print(myRect1)