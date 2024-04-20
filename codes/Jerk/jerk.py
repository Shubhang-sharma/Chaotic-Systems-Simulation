import my_lib as mb
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from matplotlib import cm 

#Jerk 

A = 1
a = 0.026

def dxdt(x,y,z,t):
    return y
def dydt(x,y,z,t):
    return z
# def dzdt(x,y,z,t):
#     return -z -A*x -(1e-9*(np.exp(y/a)-1)) 


def dzdt_bif(r):
    def dzdt(x,y,z,t):
        return (-z - r*x - (1e-9*(np.exp(y/a)-1)))
    return dzdt


r=0
while r < 2:
    X,Y,Z,T = mb.RK4_coup_dir(dxdt,dydt,dzdt_bif(r),1,0,0,0,0.01,1e4)
    R=[]
    for i in range(len(X)):
        R.append(r)
    plt.scatter(R,X, s = 0.2)
    r+=0.01
plt.show()
    
    



# # Create the 3D plot with colormap

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # ax.scatter3D(X, Y, Z,s = 0.3, c=T, cmap=cmap)  #mapping color to T values
# ax.plot3D(X, Y, Z, lw = 0.09, c = 'grey')
# # ax.scatter3D(0,0,0,s=20,c='red')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('The Jerk System')
# # plt.savefig('codes/figs/ros_res.png')
# plt.show()

# plt.plot(T[0:2000],Z[0:2000])
# plt.savefig('codes/figs/TZ.png')








