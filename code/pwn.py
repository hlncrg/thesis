import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math
import operator

fig = plt.figure(figsize=(5,5))
ax = plt.axes()

x=np.zeros(101)
y=np.zeros(101)
x2=np.zeros(101)
y2=np.zeros(101)


r1=10
for i in range(0,101):
 x[i]=i/50.0-1
 y[i]=math.sqrt(1-x[i]**2)*2
 x2[i]=x[i]*math.cos(math.pi/2.0)-y[i]*math.sin(math.pi/2.0)
 y2[i]=x[i]*math.sin(math.pi/2.0)+y[i]*math.cos(math.pi/2.0)

#plt.plot(x2,y2)
plt.plot(r1*x2,-r1*y2,'m')
plt.plot(-r1*x2,r1*y2,'m')
#plt.plot(-x2,-y2)

for i  in range(0,101):
 x[i]=i/50.0-1
 y[i]=math.sqrt(1-x[i]**2)*1

r1=20
for i  in range(0,101):
 x2[i]=(x[i]*r1-r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1-r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[90:101],y2[90:101],'b')
ax.arrow(x2[90],y2[90],x2[89]-x2[90],y2[89]-y2[90], head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[90:101],-y2[90:101],'b')
ax.arrow(-x2[90],-y2[90],-x2[89]+x2[90],-y2[89]+y2[90], head_width=1, head_length=1, fc='b', ec='b')

r1=5
for i  in range(0,101):
 x2[i]=(x[i]*r1+r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1+r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[0:50],y2[0:50],'b')
ax.arrow(x2[50],y2[50],x2[51]-x2[50],y2[51]-y2[50], head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[0:50],-y2[0:50],'b')
ax.arrow(-x2[50],-y2[50],-x2[51]+x2[50],-y2[51]+y2[50], head_width=1, head_length=1, fc='b', ec='b')


r1=10
for i  in range(0,101):
 x2[i]=(x[i]*r1-r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1-r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[60:101],y2[60:101],'b')
ax.arrow(x2[60],y2[60],x2[59]-x2[60],y2[59]-y2[60], head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[60:101],-y2[60:101],'b')
ax.arrow(-x2[60],-y2[60],-x2[59]+x2[60],-y2[59]+y2[60], head_width=1, head_length=1, fc='b', ec='b')


r1=50
for i  in range(0,101):
 x2[i]=(x[i]*r1-r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1-r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[100:101],y2[100:101],'b')
ax.arrow(x2[100],y2[100],(x2[99]-x2[100])*1.1,(y2[99]-y2[100])*1.1, head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[100:101],-y2[100:101],'b')
ax.arrow(-x2[100],-y2[100],-(x2[99]-x2[100])*1.1,-(y2[99]-y2[100])*1.1, head_width=1, head_length=1, fc='b', ec='b')


a=1
b=15
r1=.1
delx=20
dely=15
angle=math.pi/4.0*.8
for i  in range(0,101):
 x[i]=(a+b*i/15.0)*math.cos(i/15.0)*math.cos(angle)+(a+b*i/15.0)*math.sin(i/15.0)*math.sin(angle)
 y[i]=(a+b*i/15.0)*math.cos(i/15.0)*math.sin(angle)-(a+b*i/15.0)*math.sin(i/15.0)*math.cos(angle)
plt.plot(r1*x[0:40]+delx,r1*y[0:40]+dely,'r',lw=2)
for i  in range(0,101):
 x[i]=-(a+b*i/15.0)*math.cos(i/15.0)*math.cos(angle)+(a+b*i/15.0)*math.sin(i/15.0)*math.sin(angle)
 y[i]=-(a+b*i/15.0)*math.cos(i/15.0)*math.sin(angle)-(a+b*i/15.0)*math.sin(i/15.0)*math.cos(angle)
plt.plot(r1*x[0:40]+delx+r1*2,r1*y[0:40]+dely,'r',lw=1)
ax.arrow(r1*x[39]+delx+r1*2,r1*y[39]+dely, r1*x[40]+delx+r1*2-(r1*x[39]+delx+r1*2), r1*y[40]+dely-(r1*y[39]+dely), head_width=1, head_length=1, fc='r', ec='r')


delx=-20
dely=-10
angle=math.pi/4.0*.5+math.pi
for i  in range(0,101):
 x[i]=(a+b*i/15.0)*math.cos(i/15.0)*math.cos(angle)+(a+b*i/15.0)*math.sin(i/15.0)*math.sin(angle)
 y[i]=(a+b*i/15.0)*math.cos(i/15.0)*math.sin(angle)-(a+b*i/15.0)*math.sin(i/15.0)*math.cos(angle)
plt.plot(r1*x[0:40]+delx,r1*y[0:40]+dely,'r',lw=2)
for i  in range(0,101):
 x[i]=-(a+b*i/15.0)*math.cos(i/15.0)*math.cos(angle)+(a+b*i/15.0)*math.sin(i/15.0)*math.sin(angle)
 y[i]=-(a+b*i/15.0)*math.cos(i/15.0)*math.sin(angle)-(a+b*i/15.0)*math.sin(i/15.0)*math.cos(angle)
plt.plot(r1*x[0:40]+delx+r1*2,r1*y[0:40]+dely,'r',lw=1)
ax.arrow(r1*x[39]+delx+r1*2,r1*y[39]+dely, r1*x[40]+delx+r1*2-(r1*x[39]+delx+r1*2), r1*y[40]+dely-(r1*y[39]+dely), head_width=1, head_length=1, fc='r', ec='r')


delx=-10
dely=-15
angle=math.pi/4.0*1.5+math.pi
for i  in range(0,101):
 x[i]=(a+b*i/15.0)*math.cos(i/15.0)*math.cos(angle)+(a+b*i/15.0)*math.sin(i/15.0)*math.sin(angle)
 y[i]=(a+b*i/15.0)*math.cos(i/15.0)*math.sin(angle)-(a+b*i/15.0)*math.sin(i/15.0)*math.cos(angle)
plt.plot(r1*x[0:40]+delx,r1*y[0:40]+dely,'r',lw=2)
for i  in range(0,101):
 x[i]=-(a+b*i/15.0)*math.cos(i/15.0)*math.cos(angle)+(a+b*i/15.0)*math.sin(i/15.0)*math.sin(angle)
 y[i]=-(a+b*i/15.0)*math.cos(i/15.0)*math.sin(angle)-(a+b*i/15.0)*math.sin(i/15.0)*math.cos(angle)
plt.plot(r1*x[0:40]+delx+r1*2,r1*y[0:40]+dely,'r',lw=1)
ax.arrow(r1*x[39]+delx+r1*2,r1*y[39]+dely, r1*x[40]+delx+r1*2-(r1*x[39]+delx+r1*2), r1*y[40]+dely-(r1*y[39]+dely), head_width=1, head_length=1, fc='r', ec='r')





a=.5
b=1
for i  in range(0,101):
 x[i]=(a+b*i/15.0+math.pi/4.0)*math.cos(i/15.0+math.pi/4.0)
 y[i]=(a+b*i/15.0+math.pi/4.0)*math.sin(i/15.0+math.pi/4.0)
plt.plot(.2*x+10,-.2*y+25,'g')
plt.plot(.2*x+24,-.2*y+0,'g')
plt.plot(.2*x-20,-.2*y-22,'g')
plt.plot(-.2*x-10,-.2*y+25,'g')
plt.plot(-.2*x-24,-.2*y+0,'g')
plt.plot(-.2*x+20,-.2*y-22,'g')
plt.plot(.2*x+-22,-.2*y+18,'g')


plt.gca().axison = False
ax.annotate(r'$\rm{filamentary}$ $\rm{magnetic}$ $\rm{field}$', xy=(0, 12), xytext=(-8, -15), color='r')
ax.annotate(r'$\rm{cold}$ $\rm{supernova}$ $\rm{ejecta}$', xy=(0, 12), xytext=(-17, -25), color='g')
ax.annotate(r'$\rm{termination}$ $\rm{shock/}$', xy=(0, 12), xytext=(-10, 13), color='m')
ax.annotate(r'$\rm{x-ray}$ $\rm{torus}$', xy=(0, 12), xytext=(-10, 11), color='m')
ax.annotate(r'$\rm{unshocked}$', xy=(0, 12), xytext=(3, -3), color='b')
ax.annotate(r'$\rm{pulsar}$ $\rm{wind}$', xy=(0, 12), xytext=(3, -5), color='b')
plt.xlim([-30,30])
plt.ylim([-30,30])


plt.savefig('pwn.eps')
plt.show()
