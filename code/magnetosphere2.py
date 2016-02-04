import matplotlib as mpl
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
plt.plot(x2[0:14],y2[0:14],'b')
ax.arrow(x2[13],y2[13],x2[14]-x2[13],y2[14]-y2[13], head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[0:14],-y2[0:14],'b')
ax.arrow(-x2[13],-y2[13],-x2[14]+x2[13],-y2[14]+y2[13], head_width=1, head_length=1, fc='b', ec='b')



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

r1=6
for i  in range(0,101):
 x2[i]=(x[i]*r1-r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1-r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2,y2,'r')
plt.plot(-x2,-y2,'r')

r1=6
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

plt.plot([-20.8,-20.8],[-40,40],'--g')
plt.plot([20.8,20.8],[-40,40],'--g')


r1=20
for i  in range(0,101):
 x2[i]=(x[i]*r1-r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1-r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[60:101],y2[60:101],'b')
ax.arrow(x2[60],y2[60],x2[59]-x2[60],y2[59]-y2[60], head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[60:101],-y2[60:101],'b')
ax.arrow(-x2[60],-y2[60],-x2[59]+x2[60],-y2[59]+y2[60], head_width=1, head_length=1, fc='b', ec='b')


r1=17
for i  in range(0,101):
 x2[i]=(x[i]*r1+r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1+r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2,y2,'b')
ax.arrow(x2[100],y2[100],x2[100]-x2[99],y2[100]-y2[99], head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2,-y2,'b')
ax.arrow(-x2[100],-y2[100],-x2[100]+x2[99],-y2[100]+y2[99], head_width=1, head_length=1, fc='b', ec='b')



r1=30
for i  in range(0,101):
 x2[i]=(x[i]*r1-r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1-r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[80:101],y2[80:101],'b')
ax.arrow(x2[80],y2[80],x2[79]-x2[80],y2[79]-y2[80], head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[80:101],-y2[80:101],'b')
ax.arrow(-x2[80],-y2[80],-x2[79]+x2[80],-y2[79]+y2[80], head_width=1, head_length=1, fc='b', ec='b')


r1=50
for i  in range(0,101):
 x2[i]=(x[i]*r1-r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1-r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[100:101],y2[100:101],'b')
ax.arrow(x2[100],y2[100],(x2[99]-x2[100])*3.5,(y2[99]-y2[100])*3.5, head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[100:101],-y2[100:101],'b')
ax.arrow(-x2[100],-y2[100],-(x2[99]-x2[100])*3.5,-(y2[99]-y2[100])*3.5, head_width=1, head_length=1, fc='b', ec='b')

plt.plot(0,0,'oy',ms=20,markeredgecolor='yellow')

plt.gca().axison = False
ax.annotate(r'$\rm{closed}$ $\rm{magnetic}$', xy=(0, 12), xytext=(0, -13), color='r')
ax.annotate(r'$\rm{field}$ $\rm{lines}$', xy=(0, 12), xytext=(0, -16), color='r')
ax.annotate(r'$\rm{light}$ $\rm{cylinder}$', xy=(0, 12), xytext=(-19, -29), color='g')
ax.annotate(r'$\rm{open}$ $\rm{magnetic}$', xy=(0, 12), xytext=(3, 27), color='b')
ax.annotate(r'$\rm{field}$ $\rm{lines}$', xy=(0, 12), xytext=(3, 24), color='b')
plt.xlim([-30,30])
plt.ylim([-30,30])
#plt.savefig('magnetosphere.eps')
plt.show()
