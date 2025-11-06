import matplotlib.pyplot as plt
from regions.core import PixCoord
from regions.shapes.circle import CirclePixelRegion

center = PixCoord(26.6, 27.2)
reg = CirclePixelRegion(center, 5.2)

mask = reg.to_mask(mode='exact')
plt.figure(figsize=(4, 4))
shape = (50, 50)
plt.imshow(mask.to_image(shape), cmap=plt.cm.viridis,
           interpolation='nearest', origin='lower')