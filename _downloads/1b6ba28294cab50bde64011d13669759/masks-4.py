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

ax = plt.subplot(1, 1, 1)
ax.imshow(hdu.data, cmap=plt.cm.viridis,
          interpolation='nearest', origin='lower')
ax.add_artist(mask.bbox.as_artist(facecolor='none', edgecolor='white'))
ax.add_artist(aperture.as_artist(facecolor='none', edgecolor='orange'))
ax.set_xlim(120, 180)
ax.set_ylim(1000, 1059)
hdulist.close()