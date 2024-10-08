import numpy as np
A = np.arange(1, 101, dtype=np.uint8).reshape(10, 10)
print(A)
B = np.array(range(1, 101), dtype=np.uint8).reshape(10,10)
b_2x2 = [e for h in np.vsplit(A,5) for e in np.hsplit(h, 5)]
np.random.shuffle(b_2x2)



print('---------------------')

res = np.block([[b_2x2[5*i+j] for j in range(5)] for i in range(5)])
print(res)