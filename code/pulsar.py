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
 x[i]=i/50.0-1
 y[i]=math.sqrt(1-x[i]**2)*1


r1=28
r2=19
r3=5

plt.plot(x*r1,-y*r1,'y',lw=4)
plt.plot(-x*r1,y*r1,'y',lw=4)
plt.plot(x*r2,-y*r2,'b')
plt.plot(-x*r2,y*r2,'b')
plt.plot(x*r3,-y*r3,'r')
plt.plot(-x*r3,y*r3,'r')
ax.arrow(r1/math.sqrt(2), r1/math.sqrt(2), -4,-4, head_width=3, head_length=3, fc='g', ec='g',lw=3)
ax.fill_between(x*r1,y*r1,-y*r1,hatch="X",color="none",edgecolor="c")
ax.fill_between(x*r2*1.1,y*r2*1.1,-y*r2*1.1,hatch="X",color="b",edgecolor="c")
ax.fill_between(x*r2,y*r2,-y*r2,color="m",edgecolor="none")
ax.fill_between(x*r3,y*r3,-y*r3,color="r",edgecolor="none")

ax.annotate(r'$\rm{increasingly}$', xy=(0, 12), xytext=(22, 24), color='g')
ax.annotate(r'$\rm{heavy}$', xy=(0, 12), xytext=(22, 21), color='g')
ax.annotate(r'$\rm{nuclei}$', xy=(0, 12), xytext=(22, 18), color='g')

#plt.plot(x*r2,-y*r2,'b',lw=3)
#plt.plot(-x*r2,y*r2,'b',lw=3)
#ax.fill_between(x*r1,y*r1,-y*r1,hatch="X",color="b",edgecolor="c")
ax.annotate(r'$\rm{free}$ $\rm{neutrons}$', xy=(0, 12), xytext=(-37, 0), color='b')
ax.annotate(r'$\rm{neutron}$ $\rm{drip}$', xy=(0, 12), xytext=(-37, 3), color='b')


plt.gca().axison = False
ax.annotate(r'$\rm{atmosphere}$', xy=(0, 12), xytext=(-10, 30), color='y')
ax.annotate(r'$\rm{lattice}$ $\rm{nuclei}$ $\rm{crust}$', xy=(0, 12), xytext=(-10, 22), color='k')
ax.annotate(r'$\rm{neutron}$ $\rm{superfluid}$', xy=(0, 12), xytext=(-12, 13), color='k')
ax.annotate(r'$95\%$ $\rm{neutrons}$', xy=(0, 12), xytext=(-12, 10), color='k')
ax.annotate(r'$\rm{(proton}$ $\rm{superconductor)}$', xy=(0, 11), xytext=(-12, 7), color='k')
ax.annotate(r'$\rm{inner}$', xy=(0, 12), xytext=(-3, 1), color='k')
ax.annotate(r'$\rm{core}$', xy=(0, 12), xytext=(-3, -1), color='k')
plt.xlim([-30,30])
plt.ylim([-30,30])
plt.savefig('pulsar.eps')
plt.show()
