import matplotlib as mpl
mpl.use('Agg')
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math
import operator

fig = plt.figure(figsize=(5,5))
ax = plt.axes()
numpts=101
x=np.zeros(101)
y=np.zeros(101)
x2=np.zeros(101)
y2=np.zeros(101)

for i  in range(0,101):
 x[i]=i/500.0-1
 y[i]=math.sqrt(1-x[i]**2)*1

r1=150
for i  in range(0,101):
 x2[i]=(x[i]*r1+r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1+r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)



for i  in range(0,101):
 x[i]=i/50.0-1
 y[i]=math.sqrt(1-x[i]**2)*1

r1=12
for i  in range(0,101):
 x2[i]=(x[i]*r1-r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1-r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2,y2,'r')
plt.plot(-x2,-y2,'r')

r1=12
for i  in range(0,101):
 x2[i]=(x[i]*r1+r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1+r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2,y2,'r')
plt.plot(-x2,-y2,'r')

r1=5
for i  in range(0,101):
 x2[i]=(x[i]*r1-r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1-r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2,y2,'r')
plt.plot(-x2,-y2,'r')

r1=5
for i  in range(0,101):
 x2[i]=(x[i]*r1+r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1+r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2,y2,'r')
plt.plot(-x2,-y2,'r')


r1=2
for i  in range(0,101):
 x2[i]=(x[i]*r1-r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1-r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2,y2,'r')
plt.plot(-x2,-y2,'r')

r1=2
for i  in range(0,101):
 x2[i]=(x[i]*r1+r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1+r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2,y2,'r')
plt.plot(-x2,-y2,'r')



r1=20
for i  in range(0,101):
 x2[i]=(x[i]*r1-r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1-r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)


r1=17
for i  in range(0,101):
 x2[i]=(x[i]*r1+r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1+r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)



r1=30
for i  in range(0,101):
 x2[i]=(x[i]*r1-r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1-r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)


r1=50
for i  in range(0,101):
 x2[i]=(x[i]*r1-r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1-r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(0,0,'oy',ms=20,markeredgecolor='yellow')

plt.gca().axison = False
plt.xlim([-40,40])
plt.ylim([-40,40])

plt.plot([0,0],[-22,38],'k')
ax.arrow(0,-22,0,60,head_width=1, head_length=1, fc='k', ec='k')
ax.annotate(r'$\vec{\Omega}$', xy=(0, 12), xytext=(-4, 35), color='k')

plt.plot([-22,30],[-22,30],'k')
ax.arrow(-22,-22,52,52,head_width=1, head_length=1, fc='k', ec='k')
ax.annotate(r'$\vec{m}$', xy=(0, 12), xytext=(30, 27), color='k')

plt.plot([0,15],[0,35],'k')
ax.arrow(0,0,15,35,head_width=1, head_length=1, fc='k', ec='k')
ax.annotate(r'$\rm{line}$ $\rm{of}$', xy=(0, 12), xytext=(10, 40), color='k')
ax.annotate(r'$\rm{sight}$', xy=(0, 12), xytext=(10, 37), color='k')

for i  in range(0,101):
 x2[i]=i/100.0
 y2[i]=math.sqrt(1-x2[i]**2)
plt.plot(30*x2[0:71],30*y2[0:71],'c')
plt.plot(32*x2[0:40],32*y2[0:40],'m')

ax.annotate(r'$\zeta$', xy=(0, 12), xytext=(6, 33), color='m')
ax.annotate(r'$\alpha$', xy=(0, 12), xytext=(15, 27), color='c')


plt.savefig('magnetosphere.eps')
plt.show()
