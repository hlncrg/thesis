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
 theta=float(i)/100.0*math.pi
 x[i]=math.sin(theta)**3
 y[i]=math.cos(theta)*math.sin(theta)**2
a=-15


r1=30*2
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)+a
plt.plot(x2[72:81],y2[72:81],'b',lw=2)
ax.arrow(x2[80],y2[80],(x2[79]-x2[80])*6,(y2[79]-y2[80])*6,head_width=1, head_length=1, fc='c', ec='c')
ax.arrow(x2[73],y2[73],(x2[72]-x2[73])*1,(y2[72]-y2[73])*1,head_width=1, head_length=1, fc='b', ec='b')


for i in range(0,101):
 x2[i]=i/50.0-1
 y2[i]=math.sqrt(1-x2[i]**2)*1
r1=1
plt.plot(x2*r1+19,-y2*r1+4+a,'b')
plt.plot(-x2*r1+19,y2*r1+4+a,'b')
ax.annotate(r'$\rm{polar}$', xy=(0, 12), xytext=(7, 17), color='k')
ax.annotate(r'$\rm{cap}$', xy=(0, 12), xytext=(7, 15), color='k')
ax.annotate(r'$\rm{outer}$', xy=(0, 12), xytext=(7, -10), color='k')
ax.annotate(r'$\rm{gap}$', xy=(0, 12), xytext=(7, -12), color='k')
ax.annotate(r'-', xy=(0, 12), xytext=(18.5, 3+a), color='b')
r1=36*2
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)+a
plt.plot(x2[71:81],y2[71:81],'m',lw=2)
ax.arrow(x2[76],y2[76],(x2[75]-x2[76])*6,(y2[75]-y2[76])*6,head_width=1, head_length=1, fc='c', ec='c')
ax.arrow(x2[76],y2[76],-(x2[75]-x2[76])*6,-(y2[75]-y2[76])*6,head_width=1, head_length=1, fc='c', ec='c')
ax.arrow(x2[72],y2[72],-(x2[72]-x2[71])*1,-(y2[72]-y2[71])*1,head_width=1, head_length=1, fc='m', ec='m')
ax.arrow(x2[79],y2[79],-(x2[79]-x2[80])*1,-(y2[79]-y2[80])*1,head_width=1, head_length=1, fc='m', ec='m')

ax.annotate(r'$\gamma$', xy=(0, 12), xytext=(26,5+a), color='c')
ax.annotate(r'$\gamma$', xy=(0, 12), xytext=(28,17), color='c')
ax.annotate(r'$\gamma$', xy=(0, 12), xytext=(13,12), color='c')
ax.annotate(r'$\gamma$', xy=(0, 12), xytext=(33, -1+a), color='c')
ax.annotate(r'$\gamma$', xy=(0, 12), xytext=(43, -1+a), color='c')

r1=230*2
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[90:96],y2[90:96],'b',lw=2)
ax.arrow(x2[95],y2[95],-(x2[95]-x2[94])*4,-(y2[95]-y2[94])*4,head_width=1, head_length=1, fc='c', ec='c')
ax.arrow(x2[91],y2[91],-(x2[91]-x2[90])*1,-(y2[91]-y2[90])*1,head_width=1, head_length=1, fc='b', ec='b')
for i in range(0,101):
 x2[i]=i/50.0-1
 y2[i]=math.sqrt(1-x2[i]**2)*1
r1=1
plt.plot(x2*r1+7.5,-y2*r1+6,'b')
plt.plot(-x2*r1+7.5,y2*r1+6,'b')
ax.annotate(r'+', xy=(0, 12), xytext=(6.5, 5.15), color='b')

r1=400*2
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[92:96],y2[92:96],'m',lw=2)
ax.arrow(x2[94],y2[94],(x2[95]-x2[94])*1.5,(y2[95]-y2[94])*1.5,head_width=1, head_length=1, fc='c', ec='c')
ax.arrow(x2[94],y2[94],(x2[95]-x2[94])*1,(y2[95]-y2[94])*1,head_width=1, head_length=1, fc='m', ec='m')
ax.arrow(x2[93],y2[93],-(x2[93]-x2[92])*1.,-(y2[93]-y2[92])*1.,head_width=1, head_length=1, fc='m', ec='m')

for i in range(0,101):
 x2[i]=i/50.0-1
 y2[i]=math.sqrt(1-x2[i]**2)*1
r1=1
plt.plot(x2*r1+24.5,-y2*r1+18.5,'m')
plt.plot(-x2*r1+24.5,y2*r1+18.5,'m')
ax.annotate(r'-', xy=(0, 12), xytext=(24, 17.5), color='m')
plt.plot(x2*r1+26.5,-y2*r1+19.5,'m')
plt.plot(-x2*r1+26.5,y2*r1+19.5,'m')
ax.annotate(r'+', xy=(0, 12), xytext=(25.5, 18.5), color='m')
plt.plot(x2*r1+34,-y2*r1+3+a,'m')
plt.plot(-x2*r1+34,y2*r1+3+a,'m')
ax.annotate(r'+', xy=(0, 12), xytext=(33.1, 2+a), color='m')
plt.plot(x2*r1+36,-y2*r1+2+a,'m')
plt.plot(-x2*r1+36,y2*r1+2+a,'m')
ax.annotate(r'-', xy=(0, 12), xytext=(35.5, 1+a), color='m')

ax.annotate(r'$\gamma$', xy=(0, 12), xytext=(33, -1+a), color='c')
plt.plot([0,290],[0,0],'k')

#plt.plot(x2[60:90]*20-10,y2[60:90]*20-10,'y')
plt.fill_between(x2[75:94]*20-10, y2[75:94]*20-10, y2=0,color='y')
plt.gca().axison = False
ax.annotate(r'$\rho<0$', xy=(0, 12), xytext=(44, 5), color='k')
ax.annotate(r'$\rho>0$', xy=(0, 12), xytext=(44, -5), color='k')

ax.annotate(r'$\rm{light}$', xy=(0, 12), xytext=(42, -25), color='g')
ax.annotate(r'$\rm{cylinder}$', xy=(0, 12), xytext=(42, -28), color='g')
plt.plot([41.5,41.5],[-50,0],'--g')

ax.annotate(r'$\rm{pair}$', xy=(0, 12), xytext=(24, 25), color='m')
ax.annotate(r'$\rm{production}$', xy=(0, 12), xytext=(24, 23), color='m')

ax.annotate(r'$\rm{curvature}$', xy=(0, 12), xytext=(22, -4), color='c')
ax.annotate(r'$\rm{radiation}$', xy=(0, 12), xytext=(22, -6), color='c')

plt.xlim([-30+30,30+30])
plt.ylim([-30,30])
plt.savefig('magnetosphere.eps')
plt.draw()
plt.show()
