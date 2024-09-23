# 자릿수의 합이 7인거
# for n in range(2000, 3001):
#     hap = n%10 + (n//10)%10 + (n//100)%10 + (n//1000)%10
#     if hap == 7:
#         print(n)

for n in range(2000, 3001):
    hap = 0
    for x in range(4):
        hap += (n//10**x)%10

    if hap == 7:
        print(n)