import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math
import operator

from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

fig = plt.figure(figsize=(5,5))
ax = fig.gca(projection='3d')

a = Arrow3D([0,0],[0,0],[-1,1], mutation_scale=20, lw=2, arrowstyle="-|>", color="k")
ax.add_artist(a)
ax.text(0, 0, 1, r"$\Omega$", color='black')

a = Arrow3D([0,0],[-1/math.sqrt(2),1/math.sqrt(2)],[-1/math.sqrt(2),1/math.sqrt(2)], mutation_scale=20, lw=2, arrowstyle="-|>", color="k")
ax.add_artist(a)
ax.text(0, 1/math.sqrt(2), 1/math.sqrt(2), r"$m$", color='black')

a = Arrow3D([0,0],[0,math.cos(20.0/180.0*math.pi)],[0,-math.sin(20.0/180.0*math.pi)], mutation_scale=20, lw=1, arrowstyle="-|>", color="m")
ax.add_artist(a)
ax.text(0,math.cos(20.0/180.0*math.pi),-math.sin(20.0/180.0*math.pi), r"$n$", color='magenta')


a = Arrow3D([0,-math.cos(20.0/180.0*math.pi)*math.sin(-30.0/180.0*math.pi)],[0,math.cos(20.0/180.0*math.pi)*math.cos(-30.0/180.0*math.pi)],[0,-math.sin(20.0/180.0*math.pi)], mutation_scale=20, lw=1, arrowstyle="-|>", color="m")
ax.add_artist(a)


x1=np.zeros(100)
y1=np.zeros(100)
z1=np.zeros(100)

x2=np.zeros(100)
y2=np.zeros(100)
z2=np.zeros(100)

for i in range(0,100):
        y1[i]=math.sin(i/100.*math.pi)**3
        z1[i]=math.sin(i/100.*math.pi)**2*math.cos(i/100.*math.pi)

	x2[i]=x1[i]
	y2[i]=y1[i]*math.cos(-45.0/180.0*math.pi)-z1[i]*math.sin(-45.0/180.0*math.pi)
	z2[i]=y1[i]*math.sin(-45.0/180.0*math.pi)+z1[i]*math.cos(-45.0/180.0*math.pi)
plt.plot(x2,y2,z2,'--',lw=2)




x1=np.zeros(100)
y1=np.zeros(100)
z1=np.zeros(100)

x2=np.zeros(100)
y2=np.zeros(100)
z2=np.zeros(100)
for i in range(0,100):
        y1[i]=math.sin(i/100.*math.pi)**3
        z1[i]=math.sin(i/100.*math.pi)**2*math.cos(i/100.*math.pi)

	x2[i]=x1[i]*math.cos(-30.0/180.0*math.pi)-y1[i]*math.sin(-30.0/180.0*math.pi)
	y2[i]=x1[i]*math.sin(-30.0/180.0*math.pi)+y1[i]*math.cos(-30.0/180.0*math.pi)
	z2[i]=z1[i]

        x1[i]=x2[i]
        y1[i]=y2[i]*math.cos(-45.0/180.0*math.pi)-z2[i]*math.sin(-45.0/180.0*math.pi)
        z1[i]=y2[i]*math.sin(-45.0/180.0*math.pi)+z2[i]*math.cos(-45.0/180.0*math.pi)

plt.plot(x1,y1,z1,'--',lw=2)





plt.gca().patch.set_facecolor('white')
ax.w_xaxis.set_pane_color((0., 0., 0., .0))
ax.w_yaxis.set_pane_color((0., 0., 0., .0))
ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))

ax.w_xaxis.gridlines.set_visible(False)
ax.w_yaxis.gridlines.set_visible(False)
ax.w_zaxis.gridlines.set_visible(False)
ax.w_xaxis.line.set_visible(False)
ax.w_yaxis.line.set_visible(False)
ax.w_zaxis.line.set_visible(False)

for elt in ax.w_xaxis.get_ticklines() + ax.w_xaxis.get_ticklabels():
      elt.set_visible(False)
for elt in ax.w_yaxis.get_ticklines() + ax.w_yaxis.get_ticklabels():
      elt.set_visible(False)
for elt in ax.w_zaxis.get_ticklines() + ax.w_zaxis.get_ticklabels():
      elt.set_visible(False)
ax.view_init(30,20)
ax.set_xlim([0,2])
ax.set_ylim([0,2])
ax.set_zlim([-2,1])

plt.show()
