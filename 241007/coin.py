import random as rand

class Coin:
    __side = '@'# 프라이빗 속성이라는 뜻, 외부에서 수정이 불가함.
    def flip(self):
        __side = rand.choice(['@', 'O'])
        return __side
    
coins = [Coin() for _ in range(10)]

for c in coins:
    print(c.flip())