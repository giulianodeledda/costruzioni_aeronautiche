from math import *
import matplotlib.pyplot as plt
from pandas import *
import numpy as np

def version():
    return "1.0"


def getAeroData(cd0, k, clmin, clmax, pcl):
    cls = np.linspace(clmin,clmax, pcl, endpoint=True)
    cds = []
    Es = []
    for i in range(len(cls)):
        cds.append(cd0+k*cls[i]**2)
        Es.append(cls[i]/cds[i])
    data = {"CL":cls,"CD":cds, "E":Es}
    df = DataFrame(data)
    print(df)
    return df
def plotIt(x, y):
    plt.clf()
    plt.plot(x, y)
    plt.xlim(0, max(x))
    plt.ylim(0, max(y)*1.1)
    plt.grid()
    plt.savefig("plot.png")
    plt.show(block=False)
    return 0
# Test area
##DragPolar(0.01, 0.02, 0, 2.1, 10)