from regions import PixCoord, PolygonPixelRegion
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

x, y = [45, 45, 55, 60], [75, 70, 65, 75]
vertices = PixCoord(x=x, y=y)
reg = PolygonPixelRegion(vertices=vertices)
patch = reg.plot(ax=ax, facecolor='none', edgecolor='red', lw=2,
                 label='Polygon')

ax.legend(handles=(patch,), loc='upper center')
ax.set_xlim(30, 80)
ax.set_ylim(50, 80)
ax.set_aspect('equal')