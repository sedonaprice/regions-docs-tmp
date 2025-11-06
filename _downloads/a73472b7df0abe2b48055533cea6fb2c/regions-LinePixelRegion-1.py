from regions import PixCoord, LinePixelRegion
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

start = PixCoord(x=15, y=10)
end = PixCoord(x=20, y=25)
reg = LinePixelRegion(start=start, end=end)
patch = reg.plot(ax=ax, edgecolor='red', lw=2, label='Line')

ax.legend(handles=(patch,), loc='upper center')
ax.set_xlim(0, 30)
ax.set_ylim(0, 30)
ax.set_aspect('equal')