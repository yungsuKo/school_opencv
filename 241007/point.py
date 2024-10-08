import math

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def setPos(self, x, y):
        self.x, self.y = x, y
    def getPos(self):
        return self.x, self.y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def distance(self, o):
        return math.sqrt((o.x-self.x)**2 + (o.y-self.y)**2)
p1 = Point(10,20)
print(p1.getPos())
p1.setPos(1,2)
p1.move(10, -10)
print(p1.getPos())

p2 = Point(15, -5)
print(p1.distance(p2))