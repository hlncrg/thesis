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

a = Arrow3D([-.02,1],[0,0],[0,0], mutation_scale=20, lw=2, arrowstyle="-|>", color="k")
ax.add_artist(a)
ax.text(1, .1, 0, r"$Q$", color='black')

a = Arrow3D([0,0],[-.02,1],[0,0], mutation_scale=20, lw=2, arrowstyle="-|>", color="k")
ax.add_artist(a)
ax.text(0, 1, 0, r"$U$", color='black')

a = Arrow3D([0,0],[0,0],[-.02,1], mutation_scale=20, lw=2, arrowstyle="-|>", color="k")
ax.add_artist(a)
ax.text(0, 0, 1, r"$V$", color='black')

a = Arrow3D([0,1/math.sqrt(2)],[0,1/math.sqrt(2)],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="r")
ax.add_artist(a)
ax.text(1/math.sqrt(2), 1/math.sqrt(2), 0, r"$L$", color='black')


a = Arrow3D([1/math.sqrt(3),1/math.sqrt(3)],[1/math.sqrt(3),1/math.sqrt(3)],[0,1/math.sqrt(3)], mutation_scale=20, lw=1, arrowstyle="-",linestyle="dashed", color="r")
ax.add_artist(a)

a = Arrow3D([0,1/math.sqrt(3)*1.4],[0,1/math.sqrt(3)*1.4],[0,1/math.sqrt(3)*1.4], mutation_scale=20, lw=1, arrowstyle="-|>", color="r")
ax.add_artist(a)
ax.text(1/math.sqrt(3)*1.3-0, 1/math.sqrt(3)*1.3-0, 1/math.sqrt(3)*1.3+.05, r"$I$", color='black')

a = Arrow3D([0,1/math.sqrt(3)],[0,1/math.sqrt(3)],[0,1/math.sqrt(3)], mutation_scale=20, lw=2, arrowstyle="-|>", color="k")
ax.add_artist(a)
ax.text(1/math.sqrt(3)-0.06, 1/math.sqrt(3)-0.06, 1/math.sqrt(3)+.0, r"$Ip$", color='black')

x=np.zeros(100)
y=np.zeros(100)
for i in range(0,100):
	x[i]=.5-float(i)/600.0
	y[i]=math.sqrt(.5**2-x[i]**2)
plt.plot(x,y,'--',lw=2)
ax.text(.7, .2, 0, r"$2\psi$", color='black')


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
ax.set_xlim([0,1])
ax.set_ylim([0,1])
ax.set_zlim([0,1])
plt.savefig('stokesFigure.eps')
#plt.show()
