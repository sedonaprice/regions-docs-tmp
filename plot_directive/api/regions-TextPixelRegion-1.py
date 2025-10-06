from regions import PixCoord, TextPixelRegion, RegionVisual
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

center = PixCoord(x=15, y=10)
visual = RegionVisual({'textangle': 30})
reg = TextPixelRegion(center=center, text="Hello World!",
                      visual=visual)
reg.plot(ax=ax)

ax.set_xlim(10, 30)
ax.set_ylim(2.5, 20)
ax.set_aspect('equal')