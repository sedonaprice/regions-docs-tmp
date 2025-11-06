import astropy.units as u
import matplotlib.pyplot as plt
from regions import PixCoord, RegularPolygonPixelRegion

fig, ax = plt.subplots(1, 1)
center = PixCoord(x=50, y=50)
reg1 = RegularPolygonPixelRegion(center, 6, 15)
reg1.plot(edgecolor='red', lw=2)

center = PixCoord(x=25, y=25)
reg2 = RegularPolygonPixelRegion(center, 3, 15)
reg2.plot(edgecolor='green', lw=2)

center = PixCoord(x=25, y=75)
reg3 = RegularPolygonPixelRegion(center, 3, 15, angle=25*u.deg)
reg3.plot(edgecolor='orange', lw=2)

center = PixCoord(x=75, y=75)
reg4 = RegularPolygonPixelRegion(center, 8, 15)
reg4.plot(edgecolor='blue', lw=2)

center = PixCoord(x=75, y=25)
reg5 = RegularPolygonPixelRegion(center, 5, 15)
reg5.plot(edgecolor='magenta', lw=2)

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_aspect('equal')