import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# matplotlib.use('gt')

X = np.random.geometric(0.25)
print(X)
N = 100 # number of times to perform experiment
k = 1
resolution = 50
out = np.zeros((resolution,resolution))
for i, p in enumerate(np.linspace(0.01,0.99,resolution)):
    for j, q in enumerate(np.linspace(0.01,0.99,resolution)):
        out_P, out_Q, mins = [], [], []
        for n in range(0,N):
            P = 1 # initialize the P-counter
            Q = 1 # initialize Geom(Q)
            X_p = np.random.sample()
            X_q = np.random.sample()
            while X_p > p:
                P += 1
                X_p = np.random.sample()
            while X_q > q:
                Q += 1
                X_q = np.random.sample()
            out_P.append(P)
            out_Q.append(Q)
            if min(P,Q) == k:
                mins.append(min(P,Q))
        out[i,j] = len(mins)/N

plt.imshow(out, origin='lower')
plt.colorbar()
plt.clim(0,1)
ax2 = plt.gca()
ticks = np.linspace(0,50,11)
labels = np.linspace(0,1,11)
# What those pixel locations correspond to in data coordinates.
# Also set the float format here
ticklabels = [f"{i:6.2f}" for i in labels]
ax2.set_xticks(ticks)
ax2.set_yticks(ticks)
ax2.set_xticklabels(ticklabels)
ax2.set_yticklabels(ticklabels)
plt.grid()
plt.ioff()
plt.show(block=False)
