import math

# a = input('반지름 입력해봐 : ')
# print(int(a)*int(a)*math.pi)

# w, h = [float(s) for s in input('type input width with height : ').split(',')]
# print(math.atan(h/w)*180/math.pi)

# b = input('type binary number : ')
# cnt = 0

# for e in b:
#     if e == 1:
#         cnt += 1

# print(f'1 is {"EVEN" if cnt%2==0 else "ODD" }')


# X = [1.1, 1.7, 2.3, 2.8, 3.2, 3.9]
# Y = []
# for x in X:
#     Y.append(x*math.sin(x)*math.exp(-x))
# for x, y in zip(X,Y):
#     print(f'x is {x} & y is {y}')

# s = "asdfasdf,asdfasdf.xcvsdf,asdfe' asdfsadf,"
# print(s)
# print('------')
# punc = ["'", ".", ","]
# res = ""
# for c in s:
#     if c not in punc:
#         res += c
# print(res)

dd = input('type int : ')
print(bin(int(dd))[2:])