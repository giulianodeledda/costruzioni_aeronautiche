from math import *
import matplotlib.pyplot as plt
import numpy as np
def Shear(z,q0,l0):
    V = q0 * l0 - z * q0
    return V
def Bending(z,q0,l0):
    M = q0 * z ** 2 / 2 - q0 * l0 * z + q0 * l0 ** 2 / 2
    return M
##
g0 = 9.81
m = 1300.0
W = m*g0 ## Peso dell'aeroplano
l0 = 5.0 ## lunghezza semiala
q0 = W/(2*l0)
##
V = []
M = []
zs = np.linspace(0,l0,101)
for i in range(len(zs)):
    V.append(Shear(zs[i],q0,l0))
    M.append(Bending(zs[i],q0,l0))
##
plt.figure()
plt.suptitle("W = "+str(m)+" kg - $l_0$ = "+str(l0)+" m")
plt.subplots_adjust(wspace=0.4)
##
plt.subplot(1,2,1)
plt.title("Taglio")
plt.xlim(0,l0)
plt.plot(zs,V)
plt.xlim(0,l0)
plt.xlabel("z[m]\nFigura 1")
plt.ylabel("V[N]")
plt.grid()
plt.subplot(1,2,2)
plt.title("Momento Flettente")
plt.plot(zs,M)
plt.xlim(0,l0)
plt.xlabel("z[m]\nFigura 2")
plt.ylabel("M[Nm]")
plt.grid()
plt.show()