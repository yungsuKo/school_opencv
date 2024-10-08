import numpy as np
# A = np.arange(1, 13, dtype=np.uint8).reshape(2,3,2)
# print(A)
# B = A.flatten('C')
# print(B)
# B = A.flatten('F')
# print(B)
# C = A.reshape(-1)
# print(C)

LUT = np.array([2,4,5,7,8,12,15],dtype=np.uint8)
A = np.array([[0,1,5], [4,3,2], [2,0,6]])
print(A)


newA = LUT[A]
print(newA)