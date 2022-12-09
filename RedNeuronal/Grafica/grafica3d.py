import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

if __name__ == "__main__":
    manzana = pd.read_csv('Naranjas.csv', header = None, sep = ',')
    x = manzana.iloc[:,0:1]
    y = manzana.iloc[:,1:2]
    z = manzana.iloc[:,2:3]
    limon = pd.read_csv('Limones.csv', header = None, sep = ',')
    x2 = limon.iloc[:,0:1]
    y2 = limon.iloc[:,1:2]
    z2 = limon.iloc[:,2:3]
    #dibujando el plano
    '''
    x3 = np.linspace(150, 150, num=100)
    y3 = np.arange(80, 180)
    z3 = np.linspace(150, 150,num=100)
    '''
    x3 = np.linspace(100, 200, num=100)
    y3 = np.arange(100, 200)
    z3 = np.linspace(150, 150, num=100)

    fig = plt.figure()
    axl = fig.add_subplot(111, projection="3d")
    axl.set_xlabel("X")
    axl.set_ylabel("Y")
    axl.set_zlabel("Z")
    axl.scatter(x, y, z, c = 'r', marker='o')
    axl.scatter(x2, y2, z2, c = 'g', marker='o')
    axl.scatter(x3, y3, z3)
    plt.show()
