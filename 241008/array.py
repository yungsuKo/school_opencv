import numpy as np
A = np.random.randint(1, 9, (5, 5))
print(A)

row, col = np.where(A==5)
for r,c in zip(row, col):
    print(f'({r}. {c})')