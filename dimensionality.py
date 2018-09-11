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

    print("Volume of hypercube = ", hypercube_volume)
    print("Fraction of points inside hypersphere = ", ((count / N) * 4) / hypercube_volume)
    print("-----------------------------------------")

    return ((count / N) * 4) / hypercube_volume

R = range(1, 100)

lst = []
for r in R:
    frac = simulate(r=r)
    lst.append(frac)

plt.plot(lst)
plt.show()

