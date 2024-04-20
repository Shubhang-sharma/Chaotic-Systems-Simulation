import matplotlib.pyplot as plt
import numpy as np
'''Lorenz'''
# def dxdt(x,y,z,t,sig=10):
#     return sig*(y-x)

# def dydt(x,y,z,t,rho=28):
#     return x*(rho-z)-y

# def dzdt(x,y,z,t,beta=8/3):
#     return x*y-beta*z

'''Rössler'''
# def dxdt(x,y,z,t):
#     return -(y+z)

# def dydt(x,y,z,t,a=0.2):
#     return x + a*y

# def dzdt(x,y,z,t,b=0.2, c=7):
#     return b+z*(x-c)

'''Langford'''
# def dxdt(x,y,z,t,w=10):
#     return x*z-w*y

# def dydt(x,y,z,t,w=10):
#     return w*x+x*y

# def dzdt(x,y,z,t,p=1.1,q=0.7,e=0.5):
#     return p+z-z**3/3-(x**2+y**2)*(1+q*x+e*x)

'''Jerk'''
def dxdt(x,y,z,t):
    return y/(r[0] * c[0])

def dydt(x,y,z,t):
    return z/(r[1] * c[1])

def dzdt(x,y,z,t,A=1, alpha=0.1):
    return ( -z - (r[4] * x / r[5]) - r[4]*(1.159*10**(-9) * (np.exp(y/alpha) - 1)) ) / (r[4] * c[2])

r = [1e3, 1e3, 1e3, 1e3, 1e3, 1e3]
c = [1e-4, 1e-4, 1e-4]

def coup_ode4(dxdt,dydt,dzdt,x,y,z,t,tup,dt):
    xarr,yarr,zarr,tarr=[],[],[],[]
    i=0
    while t<tup:
        k1x=dt*dxdt(x,y,z,t)
        k1y=dt*dydt(x,y,z,t)
        k1z=dt*dzdt(x,y,z,t)
        
        k2x=dt*dxdt(x+k1x/2,y+k1y/2,z+k1z/2,t+dt/2)
        k2y=dt*dydt(x+k1x/2,y+k1y/2,z+k1z/2,t+dt/2)
        k2z=dt*dzdt(x+k1x/2,y+k1y/2,z+k1z/2,t+dt/2)
        
        k3x=dt*dxdt(x+k2x/2,y+k2y/2,z+k2z/2,t+dt/2)
        k3y=dt*dydt(x+k2x/2,y+k2y/2,z+k2z/2,t+dt/2)
        k3z=dt*dzdt(x+k2x/2,y+k2y/2,z+k2z/2,t+dt/2)
        
        k4x=dt*dxdt(x+k3x,y+k3y,z+k3z,t+dt)
        k4y=dt*dydt(x+k3x,y+k3y,z+k3z,t+dt)
        k4z=dt*dzdt(x+k3x,y+k3y,z+k3z,t+dt)
        
        xarr.append(x)
        yarr.append(y)
        zarr.append(z)
        tarr.append(t)
        
        x+=(k1x+2*k2x+2*k3x+k4x)/6
        y+=(k1y+2*k2y+2*k3y+k4y)/6
        z+=(k1z+2*k2z+2*k3z+k4z)/6
        t+=dt
        i+=1
    return xarr,yarr,zarr,tarr

x,y,z,t=coup_ode4(dxdt,dydt,dzdt,1,0,1,0,20,0.001)

plt.figure(figsize=(10,4))
plt.subplot(131)#,projection='2d')
plt.plot(x,y,linewidth=0.8)
plt.xlabel('X')
plt.ylabel('Y')

plt.subplot(132)
plt.plot(y,z,linewidth=0.8)
plt.xlabel('Y')
plt.ylabel('Z')

plt.subplot(133)
plt.plot(x,z,linewidth=0.8)
plt.xlabel('X')
plt.ylabel('Z')
plt.tight_layout()
plt.savefig('j.png', dpi=300)


# plt.plot(t,x,linewidth=0.8)
# plt.xlabel('T')
# plt.ylabel('X')
# plt.xlim(0,15)
# plt.subplot(312)
# plt.plot(t,y,linewidth=0.8)
# plt.xlabel('T')
# plt.ylabel('Y')
# plt.xlim(0,15)
# plt.subplot(313)
# plt.plot(t,z,linewidth=0.8)
# plt.xlabel('T')
# plt.ylabel('Z')
# plt.xlim(0,15)
# plt.savefig('jtx.png', dpi=300)

# plt.subplot(111,projection='3d')
# # plt.plot(x,y,s=2)
# ax = plt.axes(projection='3d')
# # # ax.plot3D(x,y,z)
# # ax.set_xlabel('x')
# # ax.set_ylabel('y')
# # ax.set_zlabel('z')
# plt.show()
# # plt.plot(t[:4000], x[:4000])
plt.show()
