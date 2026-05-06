from regions import PixCoord, CirclePixelRegion
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

reg = CirclePixelRegion(PixCoord(x=8, y=7), radius=3.5)
patch = reg.plot(ax=ax, facecolor='none', edgecolor='red', lw=2,
                 label='Circle')

ax.legend(handles=(patch,), loc='upper center')
ax.set_xlim(0, 15)
ax.set_ylim(0, 15)
ax.set_aspect('equal')