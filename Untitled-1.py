import numpy as np

a = np.zeros(15)
b = np.array([3,0,1,2,3,4,5,5,6,9,0,0,0,0,0])

c = np.array(a==b)
d = np.array(a==b)


print(np.sum(d))