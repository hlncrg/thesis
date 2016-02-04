import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math
import operator

fig = plt.figure(figsize=(3,3))
ax = plt.axes()


plt.xlabel(r"$\log{P}$")
plt.ylabel(r"$\log{\dot{P}}$")

ax.set_yticks([])
ax.set_yticklabels([r''])
ax.set_xticks([])
ax.set_xticklabels([r''])

ax.text(0.05,.17,r'$\rm{Millisecond}$',color='r')
ax.text(0.05,.1,r'$\rm{Pulsars}$',color='r')

ax.text(.8,.17,r'$\rm{Death}$',color='b')
ax.text(.8,.1,r'$\rm{Zone}$',color='b')

plt.plot([.7,1],[0,.8])


ax.text(0.02,.9,r'$\rm{Lines}$ $\rm{of}$',color='.5')
ax.text(0.02,.83,r'$\rm{Constant}$',color='.5')
ax.text(0.02,.76,r'$\rm{Magnetic}$',color='.5')
ax.text(0.02,.69,r'$\rm{Field}$',color='.5')
ax.text(0.02,.62,r'$\rm{Strength}$',color='.5')

ax.arrow(.2, 1.03, 0.6*1.1, -0.4*1.1, head_width=0.05, head_length=0.05, fc='k', ec='none',linestyle='dotted')
ax.arrow(.22, .74, 0.6*.9, -0.4*.9, head_width=0.05, head_length=0.05, fc='k', ec='none',linestyle='dotted')
ax.arrow(.08, .6, 0.6, -0.4, head_width=0.05, head_length=0.05, fc='k', ec='none',linestyle='dotted')

ax.text(.35,.72,r'$\rm{Young}$',color='g')
ax.text(.4,.65,r'$\rm{Pulsars}$',color='g')

ax.text(.4,.4,r'$\rm{Older}$',color='c')
ax.text(.5,.33,r'$\rm{Pulsars}$',color='c')

ax.text(.6,.9,r'$\rm{Magnetars}$',color='m')

plt.xlim(0,1)
plt.ylim(0,1)



ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
#plt.show()
plt.savefig('ppdot.eps')
