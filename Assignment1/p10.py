import numpy as np

a = np.array([1, 2, 3, 4, 5], dtype=int)

x = np.asfarray(a)

print("Original Integer Array:")
print(a)
print("Converted Floating-Point Array:")
print(x)
