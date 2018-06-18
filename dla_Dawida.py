import numpy as np
import random
import time

A_1 = np.random.random((2000, 2000))
A_2 = np.random.random((2000, 2000))
A = A_1 + 1j*A_2

b_1 = np.random.random((2000, 1))
b_2 = np.random.random((2000, 1))
b = b_1 + 1j*b_2

start = time.time()
x = np.linalg.solve(A, b)
end = time.time()
print(start)
print(end)
print(end-start)