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

l = [100*1e3,1e3,32.3*1e3,100*1e3,100*1e3,10*1e3,330*1e3,10*1e3,100*1e-9,9]

# S = (1/(l[8]*l[1]))
S = 1
def dxdt(x,y,z,t):
    return S*(-y-z)
def dydt(x,y,z,t):
    return S*(x+a*y)
def dzdt(x,y,z,t):
    return S*(b/10 + 10*x*z -c*z)

X,Y,Z,T = mb.RK4_coup_dir(dxdt,dydt,dzdt,0,0,0,0,0.001,1e5)



# For a gradient in scatter plot:
# cm = plt.get_cmap('hot')
# col = [cm(float(i)/(len(T)-1)) for i in range(len(T))]
# plt.subplot(111,projection = '3d')
# plt.scatter(X,Y,Z,c = col, cmap=cm)
# plt.show()


cmap = cm.cividis  # Example: viridis for a visually pleasing gradient

# # Create the 3D plot with colormap
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter3D(X, Y, Z,s = 1, c=T, cmap=cmap)  #mapping color to T values
ax.scatter3D(0,0,0,s=20,c='red')
# ax.plot3D(X,Y,Z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('The R$\ddot{o}$ssler Attractor')
plt.savefig('codes/figs/ros_main.png')
plt.show()






