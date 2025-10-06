from astropy.coordinates import Angle
from regions import PixCoord, RectanglePixelRegion
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

reg = RectanglePixelRegion(PixCoord(x=15, y=10), width=8,
                           height=5, angle=Angle(30, 'deg'))
patch = reg.plot(ax=ax, facecolor='none', edgecolor='red', lw=2,
                 label='Rectangle')

ax.legend(handles=(patch,), loc='upper center')
ax.set_xlim(0, 30)
ax.set_ylim(0, 20)
ax.set_aspect('equal')