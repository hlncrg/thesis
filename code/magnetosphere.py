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
x3=np.zeros(101)
y3=np.zeros(101)
for i  in range(0,101):
 theta=float(i)/100.0*math.pi
 x[i]=math.sin(theta)**3
 y[i]=math.cos(theta)*math.sin(theta)**2





r1=25.5
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2,y2,'r')
plt.plot(-x2,-y2,'r')

ax.fill_between(x2[60:85],y2[60:85],8.0/29.0*x2[60:85],hatch="\\\\",color="none",edgecolor="c")
ax.fill_between(-x2[60:85],-y2[60:85],-8.0/29.0*x2[60:85],hatch="\\\\",color="none",edgecolor="c")

#ax.fill_between(x3[0:50],y3[0:50]*10,y3[0:50]*20,hatch="\\\\",color="none",edgecolor="c")
for i in range(0,101):
 x3[i]=i/50.0-1
 y3[i]=math.sqrt(1-x3[i]**2)*1
plt.plot(x3[67:98]*5,y3[67:98]*5,'m')
plt.plot(-x3[67:98]*5,-y3[67:98]*5,'m')
a=.6
plt.plot([.4,a],[.5,-.65*(a-.4)+.5],'m')
plt.plot([-.4,-a],[-.5,-(-.65*(a-.4)+.5)],'m')
a=1.12
plt.plot([.7,a],[1,-.65*(a-.7)+1],'m')
plt.plot([-.7,-a],[-1,-(-.65*(a-.7)+1)],'m')
a=1.77
plt.plot([.92,a],[1.5,-.65*(a-.92)+1.5],'m')
plt.plot([-.92,-a],[-1.5,-(-.65*(a-.92)+1.5)],'m')
a=2.38
plt.plot([1.1,a],[2,-.65*(a-1.1)+2],'m')
plt.plot([-1.1,-a],[-2,-(-.65*(a-1.1)+2)],'m')
a=3.03
plt.plot([1.23,a],[2.5,-.65*(a-1.23)+2.5],'m')
plt.plot([-1.23,-a],[-2.5,-(-.65*(a-1.23)+2.5)],'m')
a=3.7
plt.plot([1.35,a],[3,-.65*(a-1.35)+3],'m')
plt.plot([-1.35,-a],[-3,-(-.65*(a-1.35)+3)],'m')
a=4.47
plt.plot([1.5,a],[3.5,-.65*(a-1.5)+3.5],'m')
plt.plot([-1.5,-a],[-3.5,-(-.65*(a-1.5)+3.5)],'m')
a=4.5
plt.plot([1.54,a],[4,-.65*(a-1.54)+4],'m')
plt.plot([-1.54,-a],[-4,-(-.65*(a-1.54)+4)],'m')
a=4.1
plt.plot([1.6,a],[4.5,-.65*(a-1.6)+4.5],'m')
plt.plot([-1.6,-a],[-4.5,-(-.65*(a-1.6)+4.5)],'m')

#ax.fill_between(x3[70:101]*5,y3[70:101]*5,y3[70:101]*0,hatch="\\\\\\\\\\",color="none",edgecolor="m")
r1=12
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2,y2,'r')
plt.plot(-x2,-y2,'r')


r1=6
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2,y2,'r')
plt.plot(-x2,-y2,'r')


plt.plot([-20.8,-20.8],[-40,40],'--g')
plt.plot([20.8,20.8],[-40,40],'--g')


r1=10000000
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
ax.arrow(x2[100],y2[100],(x2[99]-x2[100])*.0038,(y2[99]-y2[100])*.0038, head_width=1, head_length=1, fc='b', ec='b')
ax.arrow(-x2[100],-y2[100],-(x2[99]-x2[100])*.0038,-(y2[99]-y2[100])*.0038, head_width=1, head_length=1, fc='b', ec='b')


r1=2000
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[0:5],y2[0:5],'b')
ax.arrow(x2[4],y2[4],(x2[5]-x2[4])*.25,(y2[5]-y2[4])*.25, head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[0:5],-y2[0:5],'b')
ax.arrow(-x2[4],-y2[4],(-x2[5]+x2[4])*.25,(-y2[5]+y2[4])*.25, head_width=1, head_length=1, fc='b', ec='b')


r1=35
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[0:50],y2[0:50],'b')
ax.arrow(x2[49],y2[49],x2[50]-x2[49],y2[50]-y2[49], head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[0:50],-y2[0:50],'b')
ax.arrow(-x2[49],-y2[49],-x2[50]+x2[49],-y2[50]+y2[49], head_width=1, head_length=1, fc='b', ec='b')



r1=300
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[90:101],y2[90:101],'b')
ax.arrow(x2[91],y2[91],(x2[90]-x2[91])*1.4,(y2[90]-y2[91])*1.4, head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[90:101],-y2[90:101],'b')
ax.arrow(-x2[91],-y2[91],-(x2[90]-x2[91])*1.4,-(y2[90]-y2[91])*1.4, head_width=1, head_length=1, fc='b', ec='b')

r1=80
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[80:101],y2[80:101],'b')
ax.arrow(x2[81],y2[81],(x2[80]-x2[81])*1,(y2[80]-y2[81])*1, head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[80:101],-y2[80:101],'b')
ax.arrow(-x2[81],-y2[81],-(x2[80]-x2[81])*1,-(y2[80]-y2[81])*1, head_width=1, head_length=1, fc='b', ec
='b')
plt.plot([-290,290],[-80,80],'k')
plt.plot([-110,110],[200,-200],'k')
plt.plot(0,0,'oy',ms=20,markeredgecolor='yellow')


plt.gca().axison = False
ax.arrow(0,22,0,5,head_width=1, head_length=1, fc='k', ec='k')
ax.annotate(r'$\vec{\Omega}$', xy=(0, 12), xytext=(-3, 23), color='k')
ax.annotate(r'$\rho<0$', xy=(0, 12), xytext=(23, 18), color='k')
ax.annotate(r'$\rho>0$', xy=(0, 12), xytext=(-28, 18), color='k')
ax.annotate(r'$\rho<0$', xy=(0, 12), xytext=(-28, -18), color='k')
ax.annotate(r'$\rho>0$', xy=(0, 12), xytext=(23, -18), color='k')
ax.annotate(r'$\vec{B}\cdot\vec{\Omega}=0$', xy=(0, 12), xytext=(21, 8.5), color='k')
ax.annotate(r'$\rm{closed}$ $\rm{magnetic}$', xy=(3, 12), xytext=(2, -13), color='r')
ax.annotate(r'$\rm{field}$ $\rm{lines}$', xy=(3, 12), xytext=(3, -16), color='r')
ax.annotate(r'$\rm{light}$ $\rm{cylinder}$', xy=(0, 12), xytext=(-19, -29), color='g')
ax.annotate(r'$\rm{open}$ $\rm{magnetic}$', xy=(0, 12), xytext=(3, 27), color='b')
ax.annotate(r'$\rm{field}$ $\rm{lines}$', xy=(0, 12), xytext=(3, 24), color='b')
ax.annotate(r'$\rm{polar}$', xy=(0, 12), xytext=(2.5, 10), color='m')
ax.annotate(r'$\rm{cap}$', xy=(0, 12), xytext=(2.5, 8), color='m')
plt.plot([2.7,5],[4.3,7.5],'m')
ax.annotate(r'$\rm{outer}$', xy=(0, 12), xytext=(21, -0), color='c')
ax.annotate(r'$\rm{gap}$', xy=(0, 12), xytext=(21, -2), color='c')

plt.xlim([-30,30])
plt.ylim([-30,30])
#plt.xlim([0,5])
#plt.ylim([0,5])
#plt.savefig('magnetosphere.eps')
plt.show()
