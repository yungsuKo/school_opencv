import random as r

class Yut:
    def __init__(self):
        self.data = [0] * 4
        self.ev = {0: "윷", 1: "걸", 2:"개", 3:"도", 4:"모"}
    def play(self):
        self.data = [r.randint(0,1) for _ in range(4)]
    def show(self):
        res = ['X' if d else 'O' for d in self.data]
        return res
    def evaluate(self):
        return self.ev[sum(self.data)]

y = Yut()
for _ in range(10):
    y.play()
    print(y.show(), y.evaluate())