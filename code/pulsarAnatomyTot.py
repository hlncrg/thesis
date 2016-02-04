import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math
import operator

fig = plt.figure(figsize=(16,12))
ax = plt.axes()


xsnr=35
ysnr=6

xpwn=110
ypwn=-5

xrvm=64.5
yrvm=-68

xns=-4
yns=-84

xpc=97
ypc=-75

plt.plot([-2+xsnr,-2+xsnr],[-1.5+ysnr,1.5+ysnr],'k')
plt.plot([2+xsnr,2+xsnr],[-1.5+ysnr,1.5+ysnr],'k')
plt.plot([-2+xsnr,2+xsnr],[-1.5+ysnr,-1.5+ysnr],'k')
plt.plot([-2+xsnr,2+xsnr],[1.5+ysnr,1.5+ysnr],'k')

plt.plot([2+xsnr,-28+xpwn],[1.5+ysnr,28+ypwn],'--k')
plt.plot([2+xsnr,-28+xpwn],[-1.5+ysnr,-28+ypwn],'--k')
ax.arrow(2+xsnr,1.5+ysnr, (-28+xpwn-(2+xsnr))*.87, (28+ypwn-(1.5+ysnr))*.87, head_width=1, head_length=6, fc='k', ec='none',linestyle='dotted')
ax.arrow(2+xsnr,-1.5+ysnr, (-28+xpwn-(2+xsnr))*.91, (-28+ypwn-(-1.5+ysnr))*.91, head_width=1, head_length=6, fc='k', ec='none',linestyle='dotted')

plt.plot([-1+xpwn,-1+xpwn],[-1+ypwn,1+ypwn],'k')
plt.plot([1+xpwn,1+xpwn],[-1+ypwn,1+ypwn],'k')
plt.plot([-1+xpwn,1+xpwn],[-1+ypwn,-1+ypwn],'k')
plt.plot([-1+xpwn,1+xpwn],[1+ypwn,1+ypwn],'k')

plt.plot([-28+xpwn,-28+xpwn],[-28+ypwn,28+ypwn],'k')
plt.plot([28+xpwn,28+xpwn],[-28+ypwn,28+ypwn],'k')
plt.plot([-28+xpwn,28+xpwn],[-28+ypwn,-28+ypwn],'k')
plt.plot([-28+xpwn,28+xpwn],[28+ypwn,28+ypwn],'k')

plt.plot([1+xpwn,30+xrvm],[-1+ypwn,30+yrvm],'--k')
#plt.plot([30+xrvm],[30+yrvm],'--k',marker=r'>',ms=10)
plt.plot([-1+xpwn,-30+xrvm],[-1+ypwn,30+yrvm],'--k')
#plt.plot([-30+xrvm],[30+yrvm],'--k',marker=r'>',ms=10)
ax.arrow(1+xpwn,-1+ypwn, (30+xrvm-(1+xpwn))*.84, (30+yrvm-(-1+ypwn))*.84, head_width=1, head_length=6, fc='k', ec='none',linestyle='dotted')
ax.arrow(-1+xpwn,-1+ypwn, (-30+xrvm-(-1+xpwn))*.93, (30+yrvm-(-1+ypwn))*.93, head_width=1, head_length=6, fc='k', ec='none',linestyle='dotted')


plt.plot([17+xrvm,17+xrvm],[-8+yrvm,-5+yrvm],'k')
plt.plot([22+xrvm,22+xrvm],[-8+yrvm,-5+yrvm],'k')
plt.plot([17+xrvm,22+xrvm],[-8+yrvm,-8+yrvm],'k')
plt.plot([17+xrvm,22+xrvm],[-5+yrvm,-5+yrvm],'k')

plt.plot([5+xrvm,0+xpc],[4+yrvm,27+ypc],'--k')
#plt.plot([0+xpc],[27+ypc],'--k',marker=r'>',ms=10)
plt.plot([5+xrvm,0+xpc],[2+yrvm,0+ypc],'--k')
#plt.plot([0+xpc],[0+ypc],'--k',marker=r'>',ms=10)
ax.arrow(5+xrvm,4+yrvm, (0+xpc-(5+xrvm))*.8, (27+ypc-(4+yrvm))*.8, head_width=1, head_length=6, fc='k', ec='none',linestyle='dotted')
ax.arrow(5+xrvm,2+yrvm, (0+xpc-(5+xrvm))*.8, (0+ypc-(2+yrvm))*.8, head_width=1, head_length=6, fc='k', ec='none',linestyle='dotted')


plt.plot([22+xrvm,8.4+xpc],[-5+yrvm,-3+ypc],'--k')
#plt.plot([8.4+xpc],[-3+ypc],'--k',marker=r'>',ms=10)
plt.plot([22+xrvm,8.4+xpc],[-8+yrvm,-29+ypc],'--k')
#plt.plot([8.4+xpc],[-29+ypc],'--k',marker=r'>',ms=10)
ax.arrow(22+xrvm,-5+yrvm, (8.4+xpc-(22+xrvm))*.72, (-3+ypc-(-5+yrvm))*.72, head_width=1, head_length=6, fc='k', ec='none',linestyle='dotted')
ax.arrow(22+xrvm,-8+yrvm, (8.4+xpc-(22+xrvm))*.82, (-29+ypc-(-8+yrvm))*.82, head_width=1, head_length=6, fc='k', ec='none',linestyle='dotted')


plt.plot([-3+xrvm,36+xns],[3+yrvm,33+yns],'--k')
#plt.plot([36+xns],[33+yns],'--k',marker=r'>',ms=10)
plt.plot([-3+xrvm,36+xns],[-3+yrvm,-29+yns],'--k')
#plt.plot([36+xns],[-29+yns],'--k',marker=r'>',ms=10)
ax.arrow(-3+xrvm,3+yrvm, (36+xns-(-3+xrvm))*.81, (33+yns-(3+yrvm))*.81, head_width=1, head_length=6, fc='k', ec='none',linestyle='dotted')
ax.arrow(-3+xrvm,-3+yrvm, (36+xns-(-3+xrvm))*.88, (-29+yns-(-3+yrvm))*.88, head_width=1, head_length=6, fc='k', ec='none',linestyle='dotted')


plt.plot([-37+xns,-37+xns],[-29+yns,33+yns],'k')
plt.plot([36+xns,36+xns],[-29+yns,33+yns],'k')
plt.plot([-37+xns,36+xns],[-29+yns,-29+yns],'k')
plt.plot([-37+xns,36+xns],[33+yns,33+yns],'k')

plt.plot([8.4+xpc,8.4+xpc],[-29+ypc,-3+ypc],'k')
plt.plot([52+xpc,52+xpc],[-29+ypc,-3+ypc],'k')
plt.plot([8.4+xpc,52+xpc],[-29+ypc,-29+ypc],'k')
plt.plot([8.4+xpc,52+xpc],[-3+ypc,-3+ypc],'k')

plt.plot([-0+xpc,-0+xpc],[0+ypc,27+ypc],'k')
plt.plot([45+xpc,45+xpc],[0+ypc,27+ypc],'k')
plt.plot([-0+xpc,45+xpc],[0+ypc,0+ypc],'k')
plt.plot([-0+xpc,45+xpc],[27+ypc,27+ypc],'k')



#***************************************SNR************************************

a=.5
b=1

x=np.zeros(101)
y=np.zeros(101)
x2=np.zeros(101)
y2=np.zeros(101)

for i in range(0,101):
 x[i]=(a+b*i/15.0+math.pi/4.0)*math.cos(i/15.0+math.pi/4.0)
 y[i]=(a+b*i/15.0+math.pi/4.0)*math.sin(i/15.0+math.pi/4.0)


for i in range(0,101):
 x[i]=i/50.0-1
 y[i]=math.sqrt(1-x[i]**2)*2
 x2[i]=x[i]*math.cos(math.pi/2.0)-y[i]*math.sin(math.pi/2.0)
 y2[i]=x[i]*math.sin(math.pi/2.0)+y[i]*math.cos(math.pi/2.0)

#plt.plot(x2,y2)
plt.plot(.5*x2+xsnr,-.5*y2+ysnr,'m')
plt.plot(-.5*x2+xsnr,.5*y2+ysnr,'m')
#plt.plot(-x2,-y2)

for i in range(0,101):
 x[i]=i/50.0-1
 y[i]=math.sqrt(1-x[i]**2)*1


r1=20
r2=19
plt.plot(x*r1+xsnr,-y*r1+ysnr,'r')
plt.plot(-x*r1+xsnr,y*r1+ysnr,'r')
plt.plot(x*r2+xsnr,-y*r2+ysnr,'b')
plt.plot(-x*r2+xsnr,y*r2+ysnr,'b')

plt.plot(x[60:70]*r1+xsnr,-y[60:70]*r1+ysnr,'k',lw=2)
plt.plot(x[60:70]*r2+xsnr,-y[60:70]*r2+ysnr,'k',lw=2)
ax.annotate(r'$\rm{hot}$', xy=(x[65]*r1+xsnr,-y[65]*r1+ysnr), xytext=(2+xsnr,-24+ysnr),
            arrowprops=dict(facecolor='black', shrink=0.05,width=.5,headwidth=0),
            )
ax.annotate(r'$\rm{supernova}$', xy=(x[75]*r1+xsnr,-y[75]*r1+ysnr), xytext=(2+xsnr,-26+ysnr))
ax.annotate(r'$\rm{ejecta}$', xy=(x[75]*r1+xsnr,-y[75]*r1+ysnr), xytext=(2+xsnr,-28+ysnr))

ax.arrow(r1/math.sqrt(2)+xsnr, r1/math.sqrt(2)+ysnr, 2, 2, head_width=1, head_length=1, fc='r', ec='r')
ax.arrow(r1/math.sqrt(2)+xsnr, -r1/math.sqrt(2)+ysnr, 2, -2, head_width=1, head_length=1, fc='r', ec='r')
ax.arrow(-r1/math.sqrt(2)+xsnr, r1/math.sqrt(2)+ysnr, -2, 2, head_width=1, head_length=1, fc='r', ec='r')
ax.arrow(-r1/math.sqrt(2)+xsnr, -r1/math.sqrt(2)+ysnr, -2, -2, head_width=1, head_length=1, fc='r', ec='r')

ax.arrow(0+xsnr, r1+ysnr, 0, math.sqrt(2)*2, head_width=1, head_length=1, fc='r', ec='r')
ax.arrow(0+xsnr, -r1+ysnr, 0, -math.sqrt(2)*2, head_width=1, head_length=1, fc='r', ec='r')
ax.arrow(-r1+xsnr, 0+ysnr, -math.sqrt(2)*2, 0, head_width=1, head_length=1, fc='r', ec='r')
ax.arrow(r1+xsnr, 0+ysnr, math.sqrt(2)*2, 0, head_width=1, head_length=1, fc='r', ec='r')

ax.arrow(-r2/math.sqrt(2)+xsnr, -r2/math.sqrt(2)+ysnr, 1, 1, head_width=1, head_length=1, fc='b', ec='b')
ax.arrow(-r2/math.sqrt(2)+xsnr, r2/math.sqrt(2)+ysnr, 1, -1, head_width=1, head_length=1, fc='b', ec='b')
ax.arrow(r2/math.sqrt(2)+xsnr, -r2/math.sqrt(2)+ysnr, -1, 1, head_width=1, head_length=1, fc='b', ec='b')
ax.arrow(r2/math.sqrt(2)+xsnr, r2/math.sqrt(2)+ysnr, -1, -1, head_width=1, head_length=1, fc='b', ec='b')

ax.arrow(0+xsnr, r2+ysnr, 0, -math.sqrt(2)*1, head_width=1, head_length=1, fc='b', ec='b')
ax.arrow(0+xsnr, -r2+ysnr, 0, math.sqrt(2)*1, head_width=1, head_length=1, fc='b', ec='b')
ax.arrow(-r2+xsnr, 0+ysnr, math.sqrt(2)*1, 0, head_width=1, head_length=1, fc='b', ec='b')
ax.arrow(r2+xsnr, 0+ysnr, -math.sqrt(2)*1, 0, head_width=1, head_length=1, fc='b', ec='b')

for i  in range(0,101):
 x[i]=(a+b*i/15.0+math.pi/4.0)*math.cos(i/15.0+math.pi/4.0)
 y[i]=(a+b*i/15.0+math.pi/4.0)*math.sin(i/15.0+math.pi/4.0)
plt.plot(.2*x+5+xsnr,-.2*y+10+ysnr,'g')
plt.plot(.2*x+12+xsnr,-.2*y+0+ysnr,'g')
plt.plot(.2*x-8+xsnr,-.2*y-13+ysnr,'g')
plt.plot(-.2*x-5+xsnr,-.2*y+10+ysnr,'g')
plt.plot(-.2*x-12+xsnr,-.2*y+0+ysnr,'g')
plt.plot(-.2*x+8+xsnr,-.2*y-13+ysnr,'g')

plt.plot(.2*x-22+xsnr,-.2*y-13+ysnr,'c')
plt.plot(-.2*x-13+xsnr,-.2*y-22+ysnr,'c')

plt.plot(.2*x-29+xsnr,-.2*y-10+ysnr,'c')
plt.plot(-.2*x-32+xsnr,-.2*y+10+ysnr,'c')
plt.plot(-.2*x-45+xsnr,-.2*y+1+ysnr,'c')
plt.plot(-.2*x-46+xsnr,-.2*y+20+ysnr,'c')
plt.plot(.2*x-40+xsnr,-.2*y-20+ysnr,'c')
plt.plot(.2*x-42+xsnr,-.2*y-30+ysnr,'c')
plt.plot(-.2*x-30+xsnr,-.2*y+22+ysnr,'c')
plt.plot(.2*x-48+xsnr,-.2*y-23+ysnr,'c')
plt.plot(.2*x-10+xsnr,-.2*y-36+ysnr,'c')
plt.plot(-.2*x-20+xsnr,-.2*y-31+ysnr,'c')


plt.plot(-.2*x-58+xsnr,-.2*y-20+ysnr,'c')
plt.plot(-.2*x-56+xsnr,-.2*y+21+ysnr,'c')
plt.plot(.2*x-60+xsnr,-.2*y+5+ysnr,'c')
plt.plot(.2*x-65+xsnr,-.2*y-27+ysnr,'c')

plt.plot(-.2*x+38+xsnr,-.2*y-20+ysnr,'c')
plt.plot(-.2*x+36+xsnr,-.2*y+21+ysnr,'c')
plt.plot(.2*x+35+xsnr,-.2*y+5+ysnr,'c')

plt.plot(.2*x-22+xsnr,-.2*y+13+ysnr,'c')
plt.plot(-.2*x-13+xsnr,-.2*y+22+ysnr,'c')

plt.plot(.2*x+22+xsnr,-.2*y+15+ysnr,'c')
plt.plot(-.2*x+22+xsnr,-.2*y-13+ysnr,'c')

plt.gca().axison = False
ax.annotate(r'$\rm{interstellar}$', xy=(0, 12), xytext=(-38+xsnr, -25+ysnr), color='c')
ax.annotate(r'$\rm{medium}$', xy=(0, 12), xytext=(-38+xsnr, -27+ysnr), color='c')
ax.annotate(r'$\rm{cold}$ $\rm{supernova}$', xy=(0, 12), xytext=(-14+xsnr, -8+ysnr), color='g')
ax.annotate(r'$\rm{ejecta}$', xy=(0, 12), xytext=(-14+xsnr, -10+ysnr), color='g')

ax.annotate(r'$\rm{forward}$ $\rm{shock}$', xy=(0, 12), xytext=(2+xsnr, 20.5+ysnr), color='r')
ax.annotate(r'$\rm{reverse}$ $\rm{shock}$', xy=(0, 12), xytext=(-12+xsnr, 13+ysnr), color='b')
ax.annotate(r'$\rm{SUPERNOVA}$ $\rm{REMNANT}$', xy=(0, 12), xytext=(-12+xsnr, 26+ysnr), color='k')

#***************************************pwn************************************

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
plt.plot(r1*x2+xpwn,-r1*y2+ypwn,'m')
plt.plot(-r1*x2+xpwn,r1*y2+ypwn,'m')
#plt.plot(-x2,-y2)

for i  in range(0,101):
 x[i]=i/50.0-1
 y[i]=math.sqrt(1-x[i]**2)*1

r1=20
for i  in range(0,101):
 x2[i]=(x[i]*r1-r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1-r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[90:101]+xpwn,y2[90:101]+ypwn,'b')
ax.arrow(x2[90]+xpwn,y2[90]+ypwn,x2[89]-x2[90],y2[89]-y2[90], head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[90:101]+xpwn,-y2[90:101]+ypwn,'b')
ax.arrow(-x2[90]+xpwn,-y2[90]+ypwn,-x2[89]+x2[90],-y2[89]+y2[90], head_width=1, head_length=1, fc='b', ec='b')

r1=5
for i  in range(0,101):
 x2[i]=(x[i]*r1+r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1+r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[0:50]+xpwn,y2[0:50]+ypwn,'b')
ax.arrow(x2[50]+xpwn,y2[50]+ypwn,x2[51]-x2[50],y2[51]-y2[50], head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[0:50]+xpwn,-y2[0:50]+ypwn,'b')
ax.arrow(-x2[50]+xpwn,-y2[50]+ypwn,-x2[51]+x2[50],-y2[51]+y2[50], head_width=1, head_length=1, fc='b', ec='b')



r1=10
for i  in range(0,101):
 x2[i]=(x[i]*r1-r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1-r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[60:101]+xpwn,y2[60:101]+ypwn,'b')
ax.arrow(x2[60]+xpwn,y2[60]+ypwn,x2[59]-x2[60],y2[59]-y2[60], head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[60:101]+xpwn,-y2[60:101]+ypwn,'b')
ax.arrow(-x2[60]+xpwn,-y2[60]+ypwn,-x2[59]+x2[60],-y2[59]+y2[60], head_width=1, head_length=1, fc='b', ec='b')


r1=50
for i  in range(0,101):
 x2[i]=(x[i]*r1-r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1-r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[100:101]+xpwn,y2[100:101]+ypwn,'b')
ax.arrow(x2[100]+xpwn,y2[100]+ypwn,(x2[99]-x2[100])*1.1,(y2[99]-y2[100])*1.1, head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[100:101]+xpwn,-y2[100:101]+ypwn,'b')
ax.arrow(-x2[100]+xpwn,-y2[100]+ypwn,-(x2[99]-x2[100])*1.1,-(y2[99]-y2[100])*1.1, head_width=1, head_length=1, fc='b', ec='b')


a=1
b=15
r1=.1
delx=20
dely=15
angle=math.pi/4.0*.8
for i  in range(0,101):
 x[i]=(a+b*i/15.0)*math.cos(i/15.0)*math.cos(angle)+(a+b*i/15.0)*math.sin(i/15.0)*math.sin(angle)
 y[i]=(a+b*i/15.0)*math.cos(i/15.0)*math.sin(angle)-(a+b*i/15.0)*math.sin(i/15.0)*math.cos(angle)
plt.plot(r1*x[0:40]+delx+xpwn,r1*y[0:40]+dely+ypwn,'r',lw=2)
for i  in range(0,101):
 x[i]=-(a+b*i/15.0)*math.cos(i/15.0)*math.cos(angle)+(a+b*i/15.0)*math.sin(i/15.0)*math.sin(angle)
 y[i]=-(a+b*i/15.0)*math.cos(i/15.0)*math.sin(angle)-(a+b*i/15.0)*math.sin(i/15.0)*math.cos(angle)
plt.plot(r1*x[0:40]+delx+r1*2+xpwn,r1*y[0:40]+dely+ypwn,'r',lw=1)
ax.arrow(r1*x[39]+delx+r1*2+xpwn,r1*y[39]+dely+ypwn, r1*x[40]+delx+r1*2-(r1*x[39]+delx+r1*2), r1*y[40]+dely-(r1*y[39]+dely), head_width=1, head_length=1, fc='r', ec='r')

delx=-22
dely=-8
angle=math.pi/4.0*.5+math.pi
for i  in range(0,101):
 x[i]=(a+b*i/15.0)*math.cos(i/15.0)*math.cos(angle)+(a+b*i/15.0)*math.sin(i/15.0)*math.sin(angle)
 y[i]=(a+b*i/15.0)*math.cos(i/15.0)*math.sin(angle)-(a+b*i/15.0)*math.sin(i/15.0)*math.cos(angle)
plt.plot(r1*x[0:40]+delx+xpwn,r1*y[0:40]+dely+ypwn,'r',lw=2)
for i  in range(0,101):
 x[i]=-(a+b*i/15.0)*math.cos(i/15.0)*math.cos(angle)+(a+b*i/15.0)*math.sin(i/15.0)*math.sin(angle)
 y[i]=-(a+b*i/15.0)*math.cos(i/15.0)*math.sin(angle)-(a+b*i/15.0)*math.sin(i/15.0)*math.cos(angle)
plt.plot(r1*x[0:40]+delx+r1*2+xpwn,r1*y[0:40]+dely+ypwn,'r',lw=1)
ax.arrow(r1*x[39]+delx+r1*2+xpwn,r1*y[39]+dely+ypwn, r1*x[40]+delx+r1*2-(r1*x[39]+delx+r1*2), r1*y[40]+dely-(r1*y[39]+dely), head_width=1, head_length=1, fc='r', ec='r')



delx=15
dely=-15
angle=math.pi/4.0*2.3+math.pi
for i  in range(0,101):
 x[i]=(a+b*i/15.0)*math.cos(i/15.0)*math.cos(angle)+(a+b*i/15.0)*math.sin(i/15.0)*math.sin(angle)
 y[i]=(a+b*i/15.0)*math.cos(i/15.0)*math.sin(angle)-(a+b*i/15.0)*math.sin(i/15.0)*math.cos(angle)
plt.plot(r1*x[0:40]+delx+xpwn,r1*y[0:40]+dely+ypwn,'r',lw=2)
for i  in range(0,101):
 x[i]=-(a+b*i/15.0)*math.cos(i/15.0)*math.cos(angle)+(a+b*i/15.0)*math.sin(i/15.0)*math.sin(angle)
 y[i]=-(a+b*i/15.0)*math.cos(i/15.0)*math.sin(angle)-(a+b*i/15.0)*math.sin(i/15.0)*math.cos(angle)
plt.plot(r1*x[0:40]+delx+r1*2+xpwn,r1*y[0:40]+dely+ypwn,'r',lw=1)
ax.arrow(r1*x[39]+delx+r1*2+xpwn,r1*y[39]+dely+ypwn, r1*x[40]+delx+r1*2-(r1*x[39]+delx+r1*2), r1*y[40]+dely-(r1*y[39]+dely), head_width=1, head_length=1, fc='r', ec='r')


delx=-10
dely=-15
angle=math.pi/4.0*1.5+math.pi
for i  in range(0,101):
 x[i]=(a+b*i/15.0)*math.cos(i/15.0)*math.cos(angle)+(a+b*i/15.0)*math.sin(i/15.0)*math.sin(angle)
 y[i]=(a+b*i/15.0)*math.cos(i/15.0)*math.sin(angle)-(a+b*i/15.0)*math.sin(i/15.0)*math.cos(angle)
plt.plot(r1*x[0:40]+delx+xpwn,r1*y[0:40]+dely+ypwn,'r',lw=2)
for i  in range(0,101):
 x[i]=-(a+b*i/15.0)*math.cos(i/15.0)*math.cos(angle)+(a+b*i/15.0)*math.sin(i/15.0)*math.sin(angle)
 y[i]=-(a+b*i/15.0)*math.cos(i/15.0)*math.sin(angle)-(a+b*i/15.0)*math.sin(i/15.0)*math.cos(angle)
plt.plot(r1*x[0:40]+delx+r1*2+xpwn,r1*y[0:40]+dely+ypwn,'r',lw=1)
ax.arrow(r1*x[39]+delx+r1*2+xpwn,r1*y[39]+dely+ypwn, r1*x[40]+delx+r1*2-(r1*x[39]+delx+r1*2), r1*y[40]+dely-(r1*y[39]+dely), head_width=1, head_length=1, fc='r', ec='r')

a=.5
b=1
for i  in range(0,101):
 x[i]=(a+b*i/15.0+math.pi/4.0)*math.cos(i/15.0+math.pi/4.0)
 y[i]=(a+b*i/15.0+math.pi/4.0)*math.sin(i/15.0+math.pi/4.0)
plt.plot(.2*x+10+xpwn,-.2*y+25+ypwn,'g')
plt.plot(.2*x+24+xpwn,-.2*y+0+ypwn,'g')
plt.plot(.2*x-20+xpwn,-.2*y-22+ypwn,'g')
plt.plot(-.2*x-10+xpwn,-.2*y+25+ypwn,'g')
plt.plot(-.2*x-24+xpwn,-.2*y+0+ypwn,'g')
plt.plot(-.2*x+20+xpwn,-.2*y-22+ypwn,'g')
plt.plot(.2*x+-22+xpwn,-.2*y+18+ypwn,'g')


plt.gca().axison = False
ax.annotate(r'$\rm{filamentary}$', xy=(0, 12), xytext=(-4+xpwn, -15+ypwn), color='r') 
ax.annotate(r'$\rm{magnetic}$', xy=(0, 12), xytext=(-4+xpwn, -17+ypwn), color='r')
ax.annotate(r'$\rm{field}$', xy=(0, 12), xytext=(-4+xpwn, -19.5+ypwn), color='r')
ax.annotate(r'$\rm{cold}$ $\rm{supernova}$', xy=(0, 12), xytext=(-0+xpwn, -23+ypwn), color='g')
ax.annotate(r'$\rm{ejecta}$', xy=(0, 12), xytext=(-0+xpwn, -25+ypwn), color='g')
ax.annotate(r'$\rm{termination}$ $\rm{shock/}$', xy=(0, 12), xytext=(-10+xpwn, 13+ypwn), color='m')
ax.annotate(r'$\rm{x-ray}$ $\rm{torus}$', xy=(0, 12), xytext=(-10+xpwn, 11+ypwn), color='m')
ax.annotate(r'$\rm{unshocked}$', xy=(0, 12), xytext=(3+xpwn, -3+ypwn), color='b')
ax.annotate(r'$\rm{pulsar}$ $\rm{wind}$', xy=(0, 12), xytext=(3+xpwn, -5+ypwn), color='b')
ax.annotate(r'$\rm{PULSAR}$ $\rm{WIND}$ $\rm{NEBULA}$', xy=(0, 12), xytext=(-14+xpwn, 29+ypwn), color='k')

#***************************************RVM************************************

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
plt.plot(x2+xrvm,y2+yrvm,'r')
plt.plot(-x2+xrvm,-y2+yrvm,'r')

ax.fill_between(x2[60:85]+xrvm,y2[60:85]+yrvm,8.0/29.0*x2[60:85]+yrvm,hatch="\\\\",color="none",edgecolor="c")
ax.fill_between(-x2[60:85]+xrvm,-y2[60:85]+yrvm,-8.0/29.0*x2[60:85]+yrvm,hatch="\\\\",color="none",edgecolor="c")

for i in range(0,101):
 x3[i]=i/50.0-1
 y3[i]=math.sqrt(1-x3[i]**2)*1
plt.plot(x3[67:98]*5+xrvm,y3[67:98]*5+yrvm,'m')
plt.plot(-x3[67:98]*5+xrvm,-y3[67:98]*5+yrvm,'m')
a=.6
plt.plot([.4+xrvm,a+xrvm],[.5+yrvm,-.65*(a-.4)+.5+yrvm],'m')
plt.plot([-.4+xrvm,-a+xrvm],[-.5+yrvm,-(-.65*(a-.4)+.5)+yrvm],'m')
a=1.12
plt.plot([.7+xrvm,a+xrvm],[1+yrvm,-.65*(a-.7)+1+yrvm],'m')
plt.plot([-.7+xrvm,-a+xrvm],[-1+yrvm,-(-.65*(a-.7)+1)+yrvm],'m')
a=1.77
plt.plot([.92+xrvm,a+xrvm],[1.5+yrvm,-.65*(a-.92)+1.5+yrvm],'m')
plt.plot([-.92+xrvm,-a+xrvm],[-1.5+yrvm,-(-.65*(a-.92)+1.5)+yrvm],'m')
a=2.38
plt.plot([1.1+xrvm,a+xrvm],[2+yrvm,-.65*(a-1.1)+2+yrvm],'m')
plt.plot([-1.1+xrvm,-a+xrvm],[-2+yrvm,-(-.65*(a-1.1)+2)+yrvm],'m')
a=3.03
plt.plot([1.23+xrvm,a+xrvm],[2.5+yrvm,-.65*(a-1.23)+2.5+yrvm],'m')
plt.plot([-1.23+xrvm,-a+xrvm],[-2.5+yrvm,-(-.65*(a-1.23)+2.5)+yrvm],'m')
a=3.7
plt.plot([1.35+xrvm,a+xrvm],[3+yrvm,-.65*(a-1.35)+3+yrvm],'m')
plt.plot([-1.35+xrvm,-a+xrvm],[-3+yrvm,-(-.65*(a-1.35)+3)+yrvm],'m')
a=4.47
plt.plot([1.5+xrvm,a+xrvm],[3.5+yrvm,-.65*(a-1.5)+3.5+yrvm],'m')
plt.plot([-1.5+xrvm,-a+xrvm],[-3.5+yrvm,-(-.65*(a-1.5)+3.5)+yrvm],'m')
a=4.5
plt.plot([1.54+xrvm,a+xrvm],[4+yrvm,-.65*(a-1.54)+4+yrvm],'m')
plt.plot([-1.54+xrvm,-a+xrvm],[-4+yrvm,-(-.65*(a-1.54)+4)+yrvm],'m')
a=4.1
plt.plot([1.6+xrvm,a+xrvm],[4.5+yrvm,-.65*(a-1.6)+4.5+yrvm],'m')
plt.plot([-1.6+xrvm,-a+xrvm],[-4.5+yrvm,-(-.65*(a-1.6)+4.5)+yrvm],'m')

r1=12
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2+xrvm,y2+yrvm,'r')
plt.plot(-x2+xrvm,-y2+yrvm,'r')


r1=6
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2+xrvm,y2+yrvm,'r')
plt.plot(-x2+xrvm,-y2+yrvm,'r')


plt.plot([-20.8+xrvm,-20.8+xrvm],[-30+yrvm,30+yrvm],'--g')
plt.plot([20.8+xrvm,20.8+xrvm],[-30+yrvm,30+yrvm],'--g')


r1=10000000
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
ax.arrow(x2[100]+xrvm,y2[100]+yrvm,(x2[99]-x2[100])*.0038,(y2[99]-y2[100])*.0038, head_width=1, head_length=1, fc='b', ec='b')
ax.arrow(-x2[100]+xrvm,-y2[100]+yrvm,-(x2[99]-x2[100])*.0038,-(y2[99]-y2[100])*.0038, head_width=1, head_length=1, fc='b', ec='b')


r1=2000
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[0:5]+xrvm,y2[0:5]+yrvm,'b')
ax.arrow(x2[4]+xrvm,y2[4]+yrvm,(x2[5]-x2[4])*.25,(y2[5]-y2[4])*.25, head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[0:5]+xrvm,-y2[0:5]+yrvm,'b')
ax.arrow(-x2[4]+xrvm,-y2[4]+yrvm,(-x2[5]+x2[4])*.25,(-y2[5]+y2[4])*.25, head_width=1, head_length=1, fc='b', ec='b')

r1=35
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[0:50]+xrvm,y2[0:50]+yrvm,'b')
ax.arrow(x2[49]+xrvm,y2[49]+yrvm,x2[50]-x2[49],y2[50]-y2[49], head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[0:50]+xrvm,-y2[0:50]+yrvm,'b')
ax.arrow(-x2[49]+xrvm,-y2[49]+yrvm,-x2[50]+x2[49],-y2[50]+y2[49], head_width=1, head_length=1, fc='b', ec='b')



r1=300
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[90:101]+xrvm,y2[90:101]+yrvm,'b')
ax.arrow(x2[91]+xrvm,y2[91]+yrvm,(x2[90]-x2[91])*1.4,(y2[90]-y2[91])*1.4, head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[90:101]+xrvm,-y2[90:101]+yrvm,'b')
ax.arrow(-x2[91]+xrvm,-y2[91]+yrvm,-(x2[90]-x2[91])*1.4,-(y2[90]-y2[91])*1.4, head_width=1, head_length=1, fc='b', ec='b')

r1=80
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[80:101]+xrvm,y2[80:101]+yrvm,'b')
ax.arrow(x2[81]+xrvm,y2[81]+yrvm,(x2[80]-x2[81])*1,(y2[80]-y2[81])*1, head_width=1, head_length=1, fc='b', ec='b')
plt.plot(-x2[80:101]+xrvm,-y2[80:101]+yrvm,'b')
ax.arrow(-x2[81]+xrvm,-y2[81]+yrvm,-(x2[80]-x2[81])*1,-(y2[80]-y2[81])*1, head_width=1, head_length=1, fc='b', ec
='b')
plt.plot([-30+xrvm,30+xrvm],[-8.28+yrvm,8.28+yrvm],'k')
plt.plot([-16.5+xrvm,16.5+xrvm],[30+yrvm,-30+yrvm],'k')
plt.plot(0+xrvm,0+yrvm,'oy',ms=20,markeredgecolor='yellow')

ax.arrow(0+xrvm,22+yrvm,0,5,head_width=1, head_length=1, fc='k', ec='k')
ax.annotate(r'$\vec{\Omega}$', xy=(0, 12), xytext=(-3+xrvm, 23+yrvm), color='k')
ax.annotate(r'$\rho<0$', xy=(0, 12), xytext=(23+xrvm, 18+yrvm), color='k')
ax.annotate(r'$\rho>0$', xy=(0, 12), xytext=(-28+xrvm, 18+yrvm), color='k')
ax.annotate(r'$\rho<0$', xy=(0, 12), xytext=(-28+xrvm, -20+yrvm), color='k')
ax.annotate(r'$\rho>0$', xy=(0, 12), xytext=(23+xrvm, -20+yrvm), color='k')
ax.annotate(r'$\vec{B}\cdot\vec{\Omega}=0$', xy=(0, 12), xytext=(20.8+xrvm, 8.5+yrvm), color='k')
ax.annotate(r'$\rm{closed}$ $\rm{magnetic}$', xy=(3, 12), xytext=(2+xrvm, -13+yrvm), color='r')
ax.annotate(r'$\rm{field}$ $\rm{lines}$', xy=(3, 12), xytext=(3+xrvm, -16+yrvm), color='r')
ax.annotate(r'$\rm{light}$ $\rm{cylinder}$', xy=(0, 12), xytext=(-19+xrvm, -29+yrvm), color='g')
ax.annotate(r'$\rm{open}$ $\rm{magnetic}$', xy=(0, 12), xytext=(3+xrvm, 27+yrvm), color='b')
ax.annotate(r'$\rm{field}$ $\rm{lines}$', xy=(0, 12), xytext=(3+xrvm, 24+yrvm), color='b')
ax.annotate(r'$\rm{polar}$', xy=(0, 12), xytext=(2.5+xrvm, 10+yrvm), color='m')
ax.annotate(r'$\rm{cap}$', xy=(0, 12), xytext=(2.5+xrvm, 8+yrvm), color='m')
plt.plot([2.7+xrvm,5+xrvm],[4.3+yrvm,7.5+yrvm],'m')
ax.annotate(r'$\rm{outer}$', xy=(0, 12), xytext=(21+xrvm, 0+yrvm), color='c')
ax.annotate(r'$\rm{gap}$', xy=(0, 12), xytext=(21+xrvm, -2+yrvm), color='c')
ax.annotate(r'$\rm{MAGNETOSPHERE}$', xy=(0, 12), xytext=(-10+xrvm, -34+yrvm), color='k')


#***************************************NS************************************

a=.5
b=1

x=np.zeros(101)
y=np.zeros(101)
x2=np.zeros(101)
y2=np.zeros(101)


for i in range(0,101):
 x[i]=i/50.0-1
 y[i]=math.sqrt(1-x[i]**2)*1


r1=28
r2=19
r3=5

plt.plot(x*r1+xns,-y*r1+yns,'y',lw=4)
plt.plot(-x*r1+xns,y*r1+yns,'y',lw=4)
plt.plot(x*r2+xns,-y*r2+yns,'b')
plt.plot(-x*r2+xns,y*r2+yns,'b')
plt.plot(x*r3+xns,-y*r3+yns,'r')
plt.plot(-x*r3+xns,y*r3+yns,'r')
ax.arrow(r1/math.sqrt(2)+xns, r1/math.sqrt(2)+yns, -4,-4, head_width=3, head_length=3, fc='g', ec='g',lw=3)
ax.fill_between(x*r1+xns,y*r1+yns,-y*r1+yns,hatch="X",color="none",edgecolor="c")
ax.fill_between(x*r2*1.1+xns,y*r2*1.1+yns,-y*r2*1.1+yns,hatch="X",color="b",edgecolor="c")
ax.fill_between(x*r2+xns,y*r2+yns,-y*r2+yns,color="m",edgecolor="none")
ax.fill_between(x*r3+xns,y*r3+yns,-y*r3+yns,color="r",edgecolor="none")

ax.annotate(r'$\rm{increasingly}$', xy=(0, 12), xytext=(22+xns, 24+yns), color='g')
ax.annotate(r'$\rm{heavy}$', xy=(0, 12), xytext=(22+xns, 21+yns), color='g')
ax.annotate(r'$\rm{nuclei}$', xy=(0, 12), xytext=(22+xns, 18+yns), color='g')

#plt.plot(x*r2,-y*r2,'b',lw=3)
#plt.plot(-x*r2,y*r2,'b',lw=3)
#ax.fill_between(x*r1,y*r1,-y*r1,hatch="X",color="b",edgecolor="c")
ax.annotate(r'$\rm{free}$ $\rm{neutrons}$', xy=(0, 12), xytext=(-36.5+xns, 0+yns), color='b')
ax.annotate(r'$\rm{neutron}$ $\rm{drip}$', xy=(0, 12), xytext=(-36.5+xns, 3+yns), color='b')

ax.annotate(r'$\rm{atmosphere}$', xy=(0, 12), xytext=(-10+xns, 30+yns), color='k')
ax.annotate(r'$\rm{lattice}$ $\rm{nuclei}$ $\rm{crust}$', xy=(0, 12), xytext=(-10+xns, 22+yns), color='k')
ax.annotate(r'$\rm{neutron}$ $\rm{superfluid}$', xy=(0, 12), xytext=(-12+xns, 13+yns), color='k')
ax.annotate(r'$95\%$ $\rm{neutrons}$', xy=(0, 12), xytext=(-12+xns, 10+yns), color='k')
ax.annotate(r'$\rm{(proton}$ $\rm{superconductor)}$', xy=(0, 11), xytext=(-12+xns, 7+yns), color='k')
ax.annotate(r'$\rm{inner}$', xy=(0, 12), xytext=(-3+xns, 1+yns), color='k')
ax.annotate(r'$\rm{core}$', xy=(0, 12), xytext=(-3+xns, -1+yns), color='k')
ax.annotate(r'$\rm{NEUTRON}$ $\rm{STAR}$', xy=(0, 12), xytext=(-13+xns, 34+yns), color='k')





#***************************************PC************************************




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
plt.plot(x2[72:81]+xpc,y2[72:81]+ypc,'b',lw=2)
ax.arrow(x2[80]+xpc,y2[80]+ypc,(x2[79]-x2[80])*6,(y2[79]-y2[80])*6,head_width=1, head_length=1, fc='c', ec='c')
ax.arrow(x2[73]+xpc,y2[73]+ypc,(x2[72]-x2[73])*1,(y2[72]-y2[73])*1,head_width=1, head_length=1, fc='b', ec='b')

r1=51
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)+a
plt.plot(x2[64:87]+xpc,y2[64:87]+ypc,'r',lw=2)

for i in range(0,101):
 x2[i]=i/50.0-1
 y2[i]=math.sqrt(1-x2[i]**2)*1
r1=1
plt.plot(x2*r1+19+xpc,-y2*r1+4+a+ypc,'b')
plt.plot(-x2*r1+19+xpc,y2*r1+4+a+ypc,'b')
ax.annotate(r'$\rm{polar}$', xy=(0, 12), xytext=(7+xpc, 17+ypc), color='k')
ax.annotate(r'$\rm{cap}$', xy=(0, 12), xytext=(7+xpc, 15+ypc), color='k')
ax.annotate(r'$\rm{outer}$', xy=(0, 12), xytext=(10+xpc, -8+ypc), color='k')
ax.annotate(r'$\rm{gap}$', xy=(0, 12), xytext=(10+xpc, -10+ypc), color='k')
ax.annotate(r'-', xy=(0, 12), xytext=(18.5+xpc, 3+a+ypc), color='b')
r1=36*2
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)+a
plt.plot(x2[71:81]+xpc,y2[71:81]+ypc,'m',lw=2)
ax.arrow(x2[76]+xpc,y2[76]+ypc,(x2[75]-x2[76])*6,(y2[75]-y2[76])*6,head_width=1, head_length=1, fc='c', ec='c')
ax.arrow(x2[76]+xpc,y2[76]+ypc,-(x2[75]-x2[76])*6,-(y2[75]-y2[76])*6,head_width=1, head_length=1, fc='c', ec='c')
ax.arrow(x2[72]+xpc,y2[72]+ypc,-(x2[72]-x2[71])*1,-(y2[72]-y2[71])*1,head_width=1, head_length=1, fc='m', ec='m')
ax.arrow(x2[79]+xpc,y2[79]+ypc,-(x2[79]-x2[80])*1,-(y2[79]-y2[80])*1,head_width=1, head_length=1, fc='m', ec='m')

ax.annotate(r'$\gamma$', xy=(0, 12), xytext=(26+xpc,5+a+ypc), color='c')
ax.annotate(r'$\gamma$', xy=(0, 12), xytext=(28+xpc,17+ypc), color='c')
ax.annotate(r'$\gamma$', xy=(0, 12), xytext=(13+xpc,12+ypc), color='c')
ax.annotate(r'$\gamma$', xy=(0, 12), xytext=(33+xpc, -1+a+ypc), color='c')
ax.annotate(r'$\gamma$', xy=(0, 12), xytext=(43+xpc, -1+a+ypc), color='c')

r1=230*2
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[90:96]+xpc,y2[90:96]+ypc,'b',lw=2)
ax.arrow(x2[95]+xpc,y2[95]+ypc,-(x2[95]-x2[94])*4,-(y2[95]-y2[94])*4,head_width=1, head_length=1, fc='c', ec='c')
ax.arrow(x2[91]+xpc,y2[91]+ypc,-(x2[91]-x2[90])*1,-(y2[91]-y2[90])*1,head_width=1, head_length=1, fc='b', ec='b')
for i in range(0,101):
 x2[i]=i/50.0-1
 y2[i]=math.sqrt(1-x2[i]**2)*1
r1=1
plt.plot(x2*r1+7.5+xpc,-y2*r1+6+ypc,'b')
plt.plot(-x2*r1+7.5+xpc,y2*r1+6+ypc,'b')
ax.annotate(r'+', xy=(0, 12), xytext=(6.5+xpc, 5.15+ypc), color='b')

r1=400*2
for i  in range(0,101):
 x2[i]=(x[i]*r1)*math.cos(-math.pi/4.0)-(-r1*y[i])*math.sin(-math.pi/4.0)
 y2[i]=(x[i]*r1)*math.sin(-math.pi/4.0)+(-r1*y[i])*math.cos(-math.pi/4.0)
plt.plot(x2[92:96]+xpc,y2[92:96]+ypc,'m',lw=2)
ax.arrow(x2[94]+xpc,y2[94]+ypc,(x2[95]-x2[94])*1.5,(y2[95]-y2[94])*1.5,head_width=1, head_length=1, fc='c', ec='c')
ax.arrow(x2[94]+xpc,y2[94]+ypc,(x2[95]-x2[94])*1,(y2[95]-y2[94])*1,head_width=1, head_length=1, fc='m', ec='m')
ax.arrow(x2[93]+xpc,y2[93]+ypc,-(x2[93]-x2[92])*1.,-(y2[93]-y2[92])*1.,head_width=1, head_length=1, fc='m', ec='m')

for i in range(0,101):
 x2[i]=i/50.0-1
 y2[i]=math.sqrt(1-x2[i]**2)*1
r1=1
plt.plot(x2*r1+24.5+xpc,-y2*r1+18.5+ypc,'m')
plt.plot(-x2*r1+24.5+xpc,y2*r1+18.5+ypc,'m')
ax.annotate(r'-', xy=(0, 12), xytext=(24+xpc, 17.5+ypc), color='m')
plt.plot(x2*r1+26.5+xpc,-y2*r1+19.5+ypc,'m')
plt.plot(-x2*r1+26.5+xpc,y2*r1+19.5+ypc,'m')
ax.annotate(r'+', xy=(0, 12), xytext=(25.5+xpc, 18.5+ypc), color='m')
plt.plot(x2*r1+34+xpc,-y2*r1+3+a+ypc,'m')
plt.plot(-x2*r1+34+xpc,y2*r1+3+a+ypc,'m')
ax.annotate(r'+', xy=(0, 12), xytext=(33.1+xpc, 2+a+ypc), color='m')
plt.plot(x2*r1+36+xpc,-y2*r1+2+a+ypc,'m')
plt.plot(-x2*r1+36+xpc,y2*r1+2+a+ypc,'m')
ax.annotate(r'-', xy=(0, 12), xytext=(35.5+xpc, 1+a+ypc), color='m')

ax.annotate(r'$\gamma$', xy=(0, 12), xytext=(33+xpc, -1+a+ypc), color='c')

#plt.plot(x2[60:90]*20-10,y2[60:90]*20-10,'y')
plt.fill_between(x2[75:94]*20-10+xpc, y2[75:94]*20-10+ypc, y2=0+ypc,color='y')
plt.gca().axison = False
ax.annotate(r'$\rho<0$', xy=(0, 12), xytext=(35+xpc, 5+ypc), color='k')
ax.annotate(r'$\rho>0$', xy=(0, 12), xytext=(44+xpc, -8+ypc), color='k')

ax.annotate(r'$\rm{light}$', xy=(0, 12), xytext=(42+xpc, -25+ypc), color='g')
ax.annotate(r'$\rm{cylinder}$', xy=(0, 12), xytext=(42+xpc, -28+ypc), color='g')
plt.plot([41.5+xpc,41.5+xpc],[-29+ypc,-3+ypc],'--g')

ax.annotate(r'$\rm{pair}$', xy=(0, 12), xytext=(20+xpc, 24+ypc), color='m')
ax.annotate(r'$\rm{production}$', xy=(0, 12), xytext=(20+xpc, 21+ypc), color='m')

ax.annotate(r'$\rm{curvature}$', xy=(0, 12), xytext=(22+xpc, -6+ypc), color='c')
ax.annotate(r'$\rm{radiation}$', xy=(0, 12), xytext=(22+xpc, -8+ypc), color='c')

ax.annotate(r'$\rm{ACCELERATION}$ $\rm{GAPS}$', xy=(0, 12), xytext=(10+xpc, 35+ypc), color='k')


plt.plot([-30+xrvm,-30+xrvm],[-30+yrvm,30+yrvm],'k')
plt.plot([30+xrvm,30+xrvm],[-30+yrvm,30+yrvm],'k')
plt.plot([-30+xrvm,30+xrvm],[-30+yrvm,-30+yrvm],'k')
plt.plot([-30+xrvm,30+xrvm],[30+yrvm,30+yrvm],'k')

plt.plot([-3+xrvm,-3+xrvm],[-3+yrvm,3+yrvm],'k')
plt.plot([3+xrvm,3+xrvm],[-3+yrvm,3+yrvm],'k')
plt.plot([-3+xrvm,3+xrvm],[-3+yrvm,-3+yrvm],'k')
plt.plot([-3+xrvm,3+xrvm],[3+yrvm,3+yrvm],'k')

plt.plot([2+xrvm,2+xrvm],[2+yrvm,4+yrvm],'k')
plt.plot([5+xrvm,5+xrvm],[2+yrvm,4+yrvm],'k')
plt.plot([2+xrvm,5+xrvm],[2+yrvm,2+yrvm],'k')
plt.plot([2+xrvm,5+xrvm],[4+yrvm,4+yrvm],'k')




plt.xlim([-42,150])
plt.ylim([-114,30])
plt.savefig('pulsarAnatomy.eps')

plt.show()
