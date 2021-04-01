import numpy as np
import copy
x = np.array([1, 2, 3])
y = x
z = copy.deepcopy(x)
y[0] = 10
print (z)
print (y)
print(x)
print (x[0] == y[0])
print (x[0] == z[0])