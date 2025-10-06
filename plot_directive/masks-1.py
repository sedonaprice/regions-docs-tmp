import matplotlib.pyplot as plt
from regions.core import PixCoord
from regions.shapes.circle import CirclePixelRegion

center = PixCoord(26.6, 27.2)
reg = CirclePixelRegion(center, 5.2)

plt.figure(figsize=(6, 6))

mask1 = reg.to_mask(mode='center')
plt.subplot(2, 2, 1)
plt.title("mode='center'", size=9)
plt.imshow(mask1.data, cmap=plt.cm.viridis,
           interpolation='nearest', origin='lower')

mask2 = reg.to_mask(mode='exact')
plt.subplot(2, 2, 2)
plt.title("mode='exact'", size=9)
plt.imshow(mask2.data, cmap=plt.cm.viridis,
           interpolation='nearest', origin='lower')

mask3 = reg.to_mask(mode='subpixels', subpixels=3)
plt.subplot(2, 2, 3)
plt.title("mode='subpixels', subpixels=3", size=9)
plt.imshow(mask3.data, cmap=plt.cm.viridis,
           interpolation='nearest', origin='lower')

mask4 = reg.to_mask(mode='subpixels', subpixels=20)
plt.subplot(2, 2, 4)
plt.title("mode='subpixels', subpixels=20", size=9)
plt.imshow(mask4.data, cmap=plt.cm.viridis,
           interpolation='nearest', origin='lower')