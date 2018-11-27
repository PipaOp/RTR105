# -*- coding: utf-8 -*-

import sys
sys.path.append("/usr/local/anaconda3/lib/pithon3.6/site-packages")

from numpy import random, sin

N=10000

x = random.uniform(0,4,N)
y = random.uniform(0,4,N)

N1 = 0
from matplotlib import pyplot as plt
plt.grid()
for i in range(N):
    #plt.plot(x[i],y[i],"ko")
    if x[i] > 0 and x[i] < 4:
        if y[i] > 0 and y[i] < sin(x/2)[i]:
            plt.plot(x[i],y[i],"go")
            N1 = N1 + 1
        else:
            plt.plot(x[i],y[i],"ro")
plt.show()
S_zinaamais = 4 * 4
S_nezinaamais = 1. * S_zinaamais *N1/N
print(S_nezinaamais)
