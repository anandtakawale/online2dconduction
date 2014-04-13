import numpy as np

def solveConduct2d(**kwargs):
    Tup = kwargs['Tup']
    Tdown = kwargs['Tdown']
    Tright = kwargs['Tright']
    Tleft = kwargs['Tleft']
    nx = 30
    ny = 30
    Tinitial = 0.25 * (Tup + Tdown + Tleft + Tright)
    T = np.ones((nx,ny)) * Tinitial
    T[0,:] = Tdown
    T[nx - 1, :] = Tup
    T[:,0] = Tleft
    T[:,ny-1] = Tright
    e = np.zeros(T.shape)
    error = 10
    acc = 0.1
    count = 0
    while error >= acc:
        count += 1
        for i in range(1,nx-1):
            for j in range(1, ny-1):
                T_old = T[i,j]
                T[i,j] = 0.25 * (T[i+1,j] + T[i-1,j] + T[i,j+1] + T[i,j-1])
                e[i,j] = abs(T[i,j] - T_old)
        error = np.linalg.norm(e)
    return T
