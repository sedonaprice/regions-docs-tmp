from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
import matplotlib.pyplot as plt
from regions.core import PixCoord
from regions.shapes.circle import CirclePixelRegion

filename = get_pkg_data_filename('photometry/M6707HH.fits')
hdulist = fits.open(filename)
hdu = hdulist[0]
center = PixCoord(158.5, 1053.5)
aperture = CirclePixelRegion(center, 4.)
mask = aperture.to_mask(mode='exact')
data = mask.cutout(hdu.data)
weighted_data = mask.multiply(hdu.data)
plt.subplot(1, 3, 1)
plt.title("Mask", size=9)
plt.imshow(mask.data, cmap=plt.cm.viridis,
           interpolation='nearest', origin='lower',
           extent=mask.bbox.extent)
plt.subplot(1, 3, 2)
plt.title("Data cutout", size=9)
plt.imshow(data, cmap=plt.cm.viridis,
           interpolation='nearest', origin='lower',
           extent=mask.bbox.extent)
plt.subplot(1, 3, 3)
plt.title("Data cutout multiplied by mask", size=9)
plt.imshow(weighted_data, cmap=plt.cm.viridis,
           interpolation='nearest', origin='lower',
           extent=mask.bbox.extent)
hdulist.close()