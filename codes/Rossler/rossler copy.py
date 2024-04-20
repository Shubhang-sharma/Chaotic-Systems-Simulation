import my_lib as mb
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from matplotlib import cm 
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from moviepy.editor import VideoClip  # Import moviepy for video creation
from matplotlib.animation import FuncAnimation


#Rossler 

a = 0.2 #parameters
b = 0.2
c = 7.0

def dxdt(x,y,z,t):
    return -y-z
def dydt(x,y,z,t):
    return x+(a*y)
def dzdt(x,y,z,t):
    return (b/10) + (10*x*z) - (c*z)

X,Y,Z,T = mb.RK4_coup_dir(dxdt,dydt,dzdt,0,0,0.2,0,0.01)

data = list(zip(X, Y, Z))

def animate(frame_num):
  # Clear the plot for each frame
  plt.cla()

  # Get points to visualize up to current frame
  points_to_plot = data[:frame_num + 1]

  # Extract X, Y, and Z coordinates from points
  x, y, z = zip(*points_to_plot)

  # Plot the points
  plt.scatter(x, y, z,s=2)

  # Set plot limits (optional)
  # ...

  # Set labels (optional)
  # ...

  # Set title (optional)
  # ...

# Create figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize animation with FuncAnimation
animation = FuncAnimation(fig, animate, frames=len(data), interval=10)  # Adjust interval for speed

plt.show()


