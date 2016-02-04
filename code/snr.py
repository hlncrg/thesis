import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math
import operator

fig = plt.figure(figsize=(5,5))
ax = plt.axes()
a=.5
b=1

x=np.zeros(101)
y=np.zeros(101)
x2=np.zeros(101)
y2=np.zeros(101)

for i in range(0,101):
 x[i]=(a+b*i/15.0+math.pi/4.0)*math.cos(i/15.0+math.pi/4.0)
 y[i]=(a+b*i/15.0+math.pi/4.0)*math.sin(i/15.0+math.pi/4.0)
#plt.plot(x+5,-y+13)
#plt.plot(x+12,-y+0)
#plt.plot(x-8,-y-13)


#plt.plot(-x-5,-y+13)
#plt.plot(-x-12,-y+0)
#plt.plot(-x+8,-y-13)


for i in range(0,101):
 x[i]=i/50.0-1
 y[i]=math.sqrt(1-x[i]**2)*2
 x2[i]=x[i]*math.cos(math.pi/2.0)-y[i]*math.sin(math.pi/2.0)
 y2[i]=x[i]*math.sin(math.pi/2.0)+y[i]*math.cos(math.pi/2.0)

#plt.plot(x2,y2)
plt.plot(.5*x2,-.5*y2,'m')
plt.plot(-.5*x2,.5*y2,'m')
#plt.plot(-x2,-y2)

for i in range(0,101):
 x[i]=i/50.0-1
 y[i]=math.sqrt(1-x[i]**2)*1


r1=20
r2=19
plt.plot(x*r1,-y*r1,'r')
plt.plot(-x*r1,y*r1,'r')
plt.plot(x*r2,-y*r2,'b')
plt.plot(-x*r2,y*r2,'b')

plt.plot(x[70:80]*r1,-y[70:80]*r1,'k',lw=2)
plt.plot(x[70:80]*r2,-y[70:80]*r2,'k',lw=2)
ax.annotate(r'$\rm{hot}$ $\rm{supernova}$ $\rm{ejecta}$', xy=(x[75]*r1,-y[75]*r1), xytext=(2,-24),
            arrowprops=dict(facecolor='black', shrink=0.05,width=.5,headwidth=0),
            )

ax.arrow(r1/math.sqrt(2), r1/math.sqrt(2), 2, 2, head_width=1, head_length=1, fc='r', ec='r')
ax.arrow(r1/math.sqrt(2), -r1/math.sqrt(2), 2, -2, head_width=1, head_length=1, fc='r', ec='r')
ax.arrow(-r1/math.sqrt(2), r1/math.sqrt(2), -2, 2, head_width=1, head_length=1, fc='r', ec='r')
ax.arrow(-r1/math.sqrt(2), -r1/math.sqrt(2), -2, -2, head_width=1, head_length=1, fc='r', ec='r')

ax.arrow(0, r1, 0, math.sqrt(2)*2, head_width=1, head_length=1, fc='r', ec='r')
ax.arrow(0, -r1, 0, -math.sqrt(2)*2, head_width=1, head_length=1, fc='r', ec='r')
ax.arrow(-r1, 0, -math.sqrt(2)*2, 0, head_width=1, head_length=1, fc='r', ec='r')
ax.arrow(r1, 0, math.sqrt(2)*2, 0, head_width=1, head_length=1, fc='r', ec='r')

ax.arrow(-r2/math.sqrt(2), -r2/math.sqrt(2), 1, 1, head_width=1, head_length=1, fc='b', ec='b')
ax.arrow(-r2/math.sqrt(2), r2/math.sqrt(2), 1, -1, head_width=1, head_length=1, fc='b', ec='b')
ax.arrow(r2/math.sqrt(2), -r2/math.sqrt(2), -1, 1, head_width=1, head_length=1, fc='b', ec='b')
ax.arrow(r2/math.sqrt(2), r2/math.sqrt(2), -1, -1, head_width=1, head_length=1, fc='b', ec='b')

ax.arrow(0, r2, 0, -math.sqrt(2)*1, head_width=1, head_length=1, fc='b', ec='b')
ax.arrow(0, -r2, 0, math.sqrt(2)*1, head_width=1, head_length=1, fc='b', ec='b')
ax.arrow(-r2, 0, math.sqrt(2)*1, 0, head_width=1, head_length=1, fc='b', ec='b')
ax.arrow(r2, 0, -math.sqrt(2)*1, 0, head_width=1, head_length=1, fc='b', ec='b')

for i  in range(0,101):
 x[i]=(a+b*i/15.0+math.pi/4.0)*math.cos(i/15.0+math.pi/4.0)
 y[i]=(a+b*i/15.0+math.pi/4.0)*math.sin(i/15.0+math.pi/4.0)
plt.plot(.2*x+5,-.2*y+10,'g')
plt.plot(.2*x+12,-.2*y+0,'g')
plt.plot(.2*x-8,-.2*y-13,'g')
plt.plot(-.2*x-5,-.2*y+10,'g')
plt.plot(-.2*x-12,-.2*y+0,'g')
plt.plot(-.2*x+8,-.2*y-13,'g')

plt.plot(.2*x-22,-.2*y-13,'y')
plt.plot(-.2*x-13,-.2*y-22,'y')

plt.plot(.2*x-22,-.2*y+13,'y')
plt.plot(-.2*x-13,-.2*y+22,'y')

plt.plot(.2*x+22,-.2*y+13,'y')
plt.plot(-.2*x+22,-.2*y-13,'y')

plt.gca().axison = False
ax.annotate(r'$\rm{ISM}$', xy=(0, 12), xytext=(-25, -25), color='y')
ax.annotate(r'$\rm{cold}$ $\rm{supernova}$ $\rm{ejecta}$', xy=(0, 12), xytext=(-14, -10), color='g')
ax.annotate(r'$\rm{forward}$ $\rm{shock}$', xy=(0, 12), xytext=(2, 20.5), color='r')
ax.annotate(r'$\rm{reverse}$ $\rm{shock}$', xy=(0, 12), xytext=(-12, 13), color='b')


plt.plot([-2,-2],[-1.5,1.5],'k')
plt.plot([2,2],[-1.5,1.5],'k')
plt.plot([-2,2],[-1.5,-1.5],'k')
plt.plot([-2,2],[1.5,1.5],'k')

plt.plot([2,30],[1.5,30],'--k')
plt.plot([2,30],[-1.5,-30],'--k')

plt.xlim([-30,30])
plt.ylim([-30,30])
plt.savefig('snr.eps')
plt.show()
