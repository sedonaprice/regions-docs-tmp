from astropy.coordinates import Angle
from regions import PixCoord, RectangleAnnulusPixelRegion
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

reg = RectangleAnnulusPixelRegion(PixCoord(x=6, y=6),
                                  inner_width=5.5,
                                  outer_width=8.5,
                                  inner_height=3.5,
                                  outer_height=6.5,
                                  angle=Angle('45deg'))
patch = reg.plot(ax=ax, facecolor='none', edgecolor='red', lw=2,
                 label='Rectangle Annulus')

ax.legend(handles=(patch,), loc='upper center')
ax.set_xlim(-5, 20)
ax.set_ylim(-5, 20)
ax.set_aspect('equal')