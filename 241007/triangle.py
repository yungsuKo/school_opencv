import math as m
class Triangle:
    def __init__(self, a=1, b=1, c=1):
        self.a, self.b, self.c = a, b, c
    def peri(self):
        return self.a + self.b + self.c
    def area(self):
        s = self.peri()/2
        return m.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

class Prism(Triangle):
    def __init__(self,a =1 ,b=1,c=1,h = 1):
        self.h = h
        Triangle.__init__(self, a, b, c)
    def volume(self):
        return self.area()*self.h
    def surface(self):
        return self.area()*2 + self.peri()*self.h
    def edges(self):
        return self.peri()*2 + 3*self.h


tr = Triangle(10,10,10)
print(tr.peri())
print(tr.area())

pr = Prism(10,10,10, 10)
print(pr.volume())
print(pr.surface())
print(pr.edges())