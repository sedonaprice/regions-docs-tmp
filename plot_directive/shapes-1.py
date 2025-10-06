import matplotlib.pyplot as plt
import numpy as np
from regions import PixCoord, RectanglePixelRegion

x, y = np.mgrid[-15:16, -10:21]
z = np.exp(-(x / 4)**2 - (y / 6)**2)
ax = plt.subplot()
img = ax.imshow(z)

rectangle = RectanglePixelRegion(center=PixCoord(x=12, y=15), width=14, height=10)
selector = rectangle.as_mpl_selector(ax)