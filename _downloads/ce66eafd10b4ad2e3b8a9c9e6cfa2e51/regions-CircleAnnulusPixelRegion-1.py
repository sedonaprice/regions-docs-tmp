from regions import PixCoord, CircleAnnulusPixelRegion
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

reg = CircleAnnulusPixelRegion(PixCoord(x=6, y=6),
                               inner_radius=5.5,
                               outer_radius=8.0)
patch = reg.plot(ax=ax, facecolor='none', edgecolor='red', lw=2,
                 label='Circle Annulus')

ax.legend(handles=(patch,), loc='upper center')
ax.set_xlim(-5, 20)
ax.set_ylim(-5, 20)
ax.set_aspect('equal')