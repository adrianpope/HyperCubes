import numpy as np
import numpy.random as nr
import matplotlib.pylab as plt

def vertices(d):
    nv = 2**d
    va = np.zeros([nv,d])
    for i in range(nv):
        for j in range(d):
            b = 2**j
            va[i][j] = (i & b)/b
    return va - 0.5

def distsq(p1,p2):
    return ((p1-p2)**2).sum()

def edges(d):
    va = vertices(d)
    nv = len(va)
    ne = d*2**(d-1)
    ea = np.zeros([ne,2,d])
    indx = 0
    for i in range(nv):
        vi = va[i]
        for j in range(i+1,nv):
            vj = va[j]
            if distsq(vi,vj) <= 1.0:
                ea[indx][0] = vi
                ea[indx][1] = vj
                indx += 1
    return ea

def draw2d(ea):
    ne = len(ea)
    for i in range(ne):
        x = [ea[i][0][0], ea[i][1][0]]
        y = [ea[i][0][1], ea[i][1][1]]
        plt.plot(x,y)
    return

def draw3d(ea):
    ne = len(ea)
    ax = plt.figure().add_subplot(projection='3d')
    for i in range(ne):
        x = [ea[i][0][0], ea[i][1][0]]
        y = [ea[i][0][1], ea[i][1][1]]
        z = [ea[i][0][2], ea[i][1][2]]
        ax.plot(x,y,z)
    ax.legend()
    return

def randv(d):
    v = nr.randn(d)
    r = ((v**2).sum())**0.5
    return v/r

def random_2space(d):
    v1 = randv(d)
    v2 = randv(d)
    
