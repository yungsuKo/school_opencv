import random

number = random.randint(0, 2**10-1)
print(bin(number))

for e in range(10):
    # print(random.randint(1, 10))
    # print(random.choice(['@', 'O']), end='')
    mask = 1<<e
    
    if number&mask !=0:
        print("@")
    else:
        print("O")
    
print('')
