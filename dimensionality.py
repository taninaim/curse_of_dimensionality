import numpy as np 
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt

def simulate(N=int(1e6), r=1, k=2):
    unif = np.random.uniform(0, 1, size=(N, k))

    count = 0
    for i in range(N):
        if euclidean(np.zeros((1,k)), unif[i]) < r:
            count += 1

    hypercube_volume = (2*r)**k 

    print("Volume of hypercube = {}".format(hypercube_volume))
    print("Fraction of points inside hypersphere = {}".format(count / float(N)))
    print("-----------------------------------------")

    return count / float(N)

K = range(1, 20)

lst = []
for k in K:
    print("k = {}".format(k))
    frac = simulate(k=k)
    lst.append(frac)

plt.plot(lst)
plt.xlabel("Dimension k")
plt.ylabel("Fraction of points in hypersphere")
plt.show()
