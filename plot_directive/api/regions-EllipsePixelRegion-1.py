from astropy.coordinates import Angle
from regions import PixCoord, EllipsePixelRegion
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

reg = EllipsePixelRegion(PixCoord(15, 10), width=16, height=10,
                         angle=Angle(30, 'deg'))
patch = reg.plot(ax=ax, facecolor='none', edgecolor='red', lw=2,
                 label='Ellipse')

ax.legend(handles=(patch,), loc='upper center')
ax.set_xlim(0, 30)
ax.set_ylim(0, 20)
ax.set_aspect('equal')