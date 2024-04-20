import my_lib as mb
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from matplotlib import cm 

#Rossler 

a = 0.2 #parameters
b = 0.2
c = 7.0

l = [98*1e3,1e3,32.3*1e3,74.7*1e3,100*1e3,10*1e3,450*1e3,9.8*1e3,100*1e-6,9]

S = (1/(l[8]*l[1]))
def dxdt(x,y,z,t):
    return S*(-y-z)
def dydt(x,y,z,t):
    return S*(x+((l[0]/l[3])-1)*(y))
def dzdt(x,y,z,t):
    return (S)*((l[1]*l[-1]/(l[1]+l[6])) + (l[0]/l[5])*(x*z) - ((l[4]/l[5]) - 1)*(z))

X,Y,Z,T = mb.RK4_coup_dir(dxdt,dydt,dzdt,0,0,0,0,0.001,0.8e5)



# For a gradient in scatter plot:
# cm = plt.get_cmap('hot')
# col = [cm(float(i)/(len(T)-1)) for i in range(len(T))]
# plt.subplot(111,projection = '3d')
# plt.scatter(X,Y,Z,c = col, cmap=cm)
# plt.show()


# cmap = cm.cividis  # Example: viridis for a visually pleasing gradient

# # Create the 3D plot with colormap
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# ax.scatter3D(X, Y, Z,s = 0.3, c=T, cmap=cmap)  #mapping color to T values
ax.plot3D(X, Y, Z, lw = 0.6)
# ax.scatter3D(0,0,0,s=20,c='red')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('The R$\ddot{o}$ssler Attractor')
# ax.grid(False)
# plt.savefig('codes/figs/ros_res.png')
plt.show()

# plt.plot(X,Z)
# plt.xlabel("X")
# plt.ylabel("Z")
# plt.show()

# fig, ax = plt.subplots(3)
 
# Accessing each axes object to plot the data through returned array
# ax[0].plot(T[6000:10000],X[6000:10000])
# ax[1].plot(T[6000:10000],Y[6000:10000])
# ax[2].plot(T[6000:10000],Z[6000:10000])

# ax[2].set_xlabel("T")
# ax[0].set_ylabel("X")
# ax[1].set_ylabel("Y")
# ax[2].set_ylabel("Z")

# plt.savefig('../data/Rossler/main/RTX.png')








