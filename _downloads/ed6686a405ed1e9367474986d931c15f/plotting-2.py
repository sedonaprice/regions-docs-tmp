import numpy as np
import matplotlib.pyplot as plt
from regions import PixCoord, CirclePixelRegion

fig, ax = plt.subplots()
region = CirclePixelRegion(center=PixCoord(x=7, y=5), radius=3)

data = np.arange(10 * 15).reshape((10, 15))
ax.imshow(data, cmap='gray', interpolation='nearest', origin='lower')
region.plot(ax=ax, color='red', lw=2.0)