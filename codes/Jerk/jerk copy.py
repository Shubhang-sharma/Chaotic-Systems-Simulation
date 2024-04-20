import my_lib as mb
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from matplotlib import cm 

'''Jerk'''
def dxdt(x,y,z,t):
    return y/(r[0] * c[0])

def dydt(x,y,z,t):
    return z/(r[1] * c[1])

def dzdt_bif(b):
    def dzdt(x,y,z,t,A=1, alpha=0.1):
        return (-z - ((b*1e3) * x / r[5]) - (b*1e3)*(1.159*10**(-9) * (np.exp(y/alpha) - 1)) ) / ((b*1e3) * c[2])
    return dzdt

r = [1e3, 1e3, 1e3, 1e3, 1e3, 1e3]
c = [1e-4, 1e-4, 1e-4]

b = 0.9
X,Y,Z,T = mb.RK4_coup_dir(dxdt,dydt,dzdt_bif(b),1,0,0,0,0.01,1e4)

def Convert(lst):
    return [ -i for i in lst ]

# b = 0.1
# BIFX,BIFY=[],[]
# while  b < 2:
#     X,Y,Z,T = mb.RK4_coup_dir(dxdt,dydt,dzdt_bif(b),1,0,0,0,0.01,0.5e5)
#     # R=[]
#     # for i in range(len(X)):
#     #     R.append(b)
#     BIFY.append(max(X))
#     BIFX.append(b)
#     b+=0.001
# plt.scatter(BIFX,BIFY,s=0.2)
# plt.savefig('jerk_bif.png')
# plt.close()
    
    



# Create the 3D plot with colormap

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # ax.scatter3D(X, Y, Z,s = 0.3, c=T, cmap=cmap)  #mapping color to T values
# ax.plot3D(X, Y, Z, lw = 0.1)
# # ax.scatter3D(0,0,0,s=20,c='red')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('The Jerk System')
# plt.savefig('codes/figs/ros_res.png')



plt.plot(Convert(Y),Z,lw=0.2)
plt.xlabel("-Y")
plt.ylabel("Z")
# plt.show()

# fig, ax = plt.subplots(3)
 
# Accessing each axes object to plot the data through returned array
# ax[0].plot(T[6000:6500],X[6000:6500])
# ax[1].plot(T[6000:6500],Convert(Y)[6000:6500])
# ax[2].plot(T[6000:6500],Z[6000:6500])

# ax[2].set_xlabel("T")
# ax[0].set_ylabel("X")
# ax[1].set_ylabel("Y")
# ax[2].set_ylabel("Z")

plt.savefig('../data/SJERKS/NYZ.png')










