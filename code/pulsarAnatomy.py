import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math
import operator

fig = plt.figure(figsize=(5,5))
a=.5
b=1

x=np.zeros(101)
y=np.zeros(101)
x2=np.zeros(101)
y2=np.zeros(101)

for i in range(0,101):
 x[i]=(a+b*i/15.0+math.pi/4.0)*math.cos(i/15.0+math.pi/4.0)
 y[i]=(a+b*i/15.0+math.pi/4.0)*math.sin(i/15.0+math.pi/4.0)
plt.plot(x+5,-y+13)
plt.plot(x+12,-y+0)
plt.plot(x-8,-y-13)


plt.plot(-x-5,-y+13)
plt.plot(-x-12,-y+0)
plt.plot(-x+8,-y-13)


for i in range(0,101):
 x[i]=i/50.0-1
 print x[i]
 y[i]=math.sqrt(1-x[i]**2)*3
 x2[i]=x[i]*math.cos(math.pi/4.0)-y[i]*math.sin(math.pi/4.0)
 y2[i]=x[i]*math.sin(math.pi/4.0)+y[i]*math.cos(math.pi/4.0)

#plt.plot(x2,y2)
plt.plot(x2,-y2)
plt.plot(-x2,y2)
#plt.plot(-x2,-y2)

plt.xlim([-30,30])
plt.ylim([-30,30])
plt.show()
