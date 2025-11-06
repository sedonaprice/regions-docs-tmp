# spherical

import matplotlib.pyplot as plt
import numpy as np
from astropy.coordinates import Angle, SkyCoord

from regions import CircleSphericalSkyRegion, make_example_dataset

# load example dataset to get skymap
config = dict(crval=(0, 0),
            crpix=(180, 90),
            cdelt=(-1, 1),
            shape=(180, 360))

dataset = make_example_dataset(data='simulated', config=config)
wcs = dataset.wcs

# remove sources
dataset.image.data = np.zeros_like(dataset.image.data)

#----------------------------------------
# define 2 spherical sky circles
sph_circle1 = CircleSphericalSkyRegion(
    center=SkyCoord(20, 0, unit='deg', frame='galactic'),
    radius=Angle('30 deg'))

sph_circle2 = CircleSphericalSkyRegion(
    center=SkyCoord(50, 45, unit='deg', frame='galactic'),
    radius=Angle('30 deg'))

# define skycoords
lon = np.arange(-180, 181, 10)
lat = np.arange(-90, 91, 10)
coords = np.array(np.meshgrid(lon, lat)).T.reshape(-1, 2)
skycoords = SkyCoord(coords, unit='deg', frame='galactic')

#----------------------------------------
# get events in AND and XOR
sph_compound_and = sph_circle1 & sph_circle2
sph_compound_xor = sph_circle1 ^ sph_circle2

sph_mask_and = sph_compound_and.contains(skycoords)
sph_skycoords_and = skycoords[sph_mask_and]
sph_mask_xor = sph_compound_xor.contains(skycoords)
sph_skycoords_xor = skycoords[sph_mask_xor]

# plot
fig = plt.figure()
fig.set_size_inches(7,3.5)
ax = fig.add_axes([0.15, 0.1, 0.8, 0.8], projection=wcs, aspect='equal')

ax.scatter(skycoords.l.value, skycoords.b.value, label='all',
        transform=ax.get_transform('galactic'))
ax.scatter(sph_skycoords_xor.l.value, sph_skycoords_xor.b.value, color='orange',
        label='xor', transform=ax.get_transform('galactic'))
ax.scatter(sph_skycoords_and.l.value, sph_skycoords_and.b.value, color='magenta',
        label='and', transform=ax.get_transform('galactic'))

boundary_kwargs = dict(
    include_boundary_distortions=True, discretize_kwargs={"n_points":1000}
)
sph_circle1.to_pixel(wcs=wcs,**boundary_kwargs).plot(ax=ax, edgecolor='green', facecolor='none',
                            alpha=0.8, lw=3)
sph_circle2.to_pixel(wcs=wcs,**boundary_kwargs).plot(ax=ax, edgecolor='red', facecolor='none',
                            alpha=0.8, lw=3)

ax.legend(loc='lower right')

ax.set_xlim(-0.5, dataset.config['shape'][1] - 0.5)
ax.set_ylim(-0.5, dataset.config['shape'][0] - 0.5)
ax.set_title("Spherical SkyRegions")