import numpy as np

mat = np.arange(1,26).reshape(5,5)

res = mat.sum(1)

print(res)