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
    plt.gca().set_aspect('equal')
    return

def draw3d(ea):
    ne = len(ea)
    ax = plt.figure().add_subplot(projection='3d')
    for i in range(ne):
        x = [ea[i][0][0], ea[i][1][0]]
        y = [ea[i][0][1], ea[i][1][1]]
        z = [ea[i][0][2], ea[i][1][2]]
        ax.plot(x,y,z)
    ax.set_aspect('equal')
    #ax.legend()
    return

def unitv(v):
    r = ((v**2).sum())**0.5
    return v/r

def randuv(d):
    return unitv(nr.randn(d))

def dot(v1,v2):
    return (v1*v2).sum()

def rand_2space(d):
    v = np.zeros([2,d])
    v[0] = randuv(d)
    v[1] = randuv(d)
    tmp = v[1] - dot(v[0],v[1])*v[0]
    v[1] = unitv(tmp)
    return v

def rand_subspace(d_in, d_out):
    v = np.zeros([d_out, d_in])
    for i in range(d_out):
        tmp = randuv(d_in)
        for j in range(i):
            tmp = unitv(tmp - dot(tmp,v[j])*v[j])
        v[i] = tmp
    return v

def project_subspace(edges_in, v):
    shape_in = edges_in.shape
    shape_out = (shape_in[0], shape_in[1], v.shape[0])
    edges_out = np.zeros(shape_out)
    for i in range(shape_out[0]):
        for j in range(shape_out[1]):
            for k in range(shape_out[2]):
                edges_out[i][j][k] = dot(edges_in[i][j],v[k])
    return edges_out
