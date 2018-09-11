import numpy as np 
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt

def simulate(N=int(1e6), r=1, k=2):
    unif = np.random.uniform(0, 1, size=(N, k))

    count = 0
    for i in range(N):
        if euclidean(np.zeros((1,k)), unif[i]) < r:
            count += 1

    area_of_square = (2*r)**k 

    print("Area of square = ", area_of_square)
    print("Fraction of points inside hypersphere = ", ((count / N) * 4) / area_of_square)
    print("-----------------------------------------")

    return ((count / N) * 4) / area_of_square

R = range(1, 10)

lst = []
for r in R:
    frac = simulate(r=r)
    lst.append(frac)

plt.plot(lst)
plt.show()

