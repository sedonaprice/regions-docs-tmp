from regions import PixCoord, PointPixelRegion, RegionVisual
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

regs = []
regs.append(PointPixelRegion(PixCoord(2, 2),
            visual=RegionVisual(marker='D')))
regs.append(PointPixelRegion(PixCoord(2, 3),
            visual=RegionVisual(marker='+')))
regs.append(PointPixelRegion(PixCoord(3, 3),
            visual=RegionVisual(marker='^')))
regs.append(PointPixelRegion(PixCoord(3, 2),
            visual=RegionVisual(marker='*')))
regs.append(PointPixelRegion(PixCoord(2, 4),
            visual=RegionVisual(marker='x')))
regs.append(PointPixelRegion(PixCoord(4, 2)))
for reg in regs:
    reg.plot(ax=ax)

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.set_aspect('equal')