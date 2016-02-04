import numpy as np
import matplotlib.pyplot as plt

fig,ax=plt.subplots(figsize=(6, 3))

x=np.arange(5,10,.1)
y=[3-((i-5)/1)**2 for i in x]
plt.plot(x,y,'g')
x=np.arange(-1,5.1,.1)
y=[3-((i-5)/3)**2 for i in x]
plt.plot(x,y,'g')

x=np.arange(11,19,.1)
y=[2.5-((i-11)/(1*.8))**2 for i in x]
plt.plot(x,y,'m')
x=np.arange(0,11.1,.1)
y=[2.5-((i-11)/(3*.8))**2 for i in x]
plt.plot(x,y,'m')

plt.ylabel(r"$\rm{Spectal}$ $\rm{Energy}$")

plt.xlim(-.5,12.5)
plt.ylim(0,3.5)

ax.set_xticks([1,3,5,8.5,11])
ax.set_xticklabels([r'$\rm{Radio}$',r'$\rm{Optical}$',r'$\rm{X-Ray}$',r'$\gamma\rm{-Ray}$',r'           $\rm{Very}$ $\rm{High}$ $\rm{Energy}$'])
ax.set_yticks([])
ax.set_yticklabels([r''])

ax.text(3,3.1,r'$\rm{Synchrotron}$',color='g')
ax.text(8,2.6,r'$\rm{Inverse}$ $\rm{Compton}$',color='m')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
plt.show()
plt.savefig('spec.eps')
