import matplotlib.pyplot as plt
import numpy as np
from astropy.coordinates import Angle, SkyCoord

from regions import (CircleSkyRegion, CircleSphericalSkyRegion,
                    make_example_dataset, PixCoord)

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
# define skycoords, pixcoords grids
lon = np.arange(-180, 181, 10)
lat = np.arange(-90, 91, 10)
coords = np.array(np.meshgrid(lon, lat)).T.reshape(-1, 2)
skycoords = SkyCoord(coords, unit='deg', frame='galactic')
pixcoords = PixCoord.from_sky(skycoords, wcs)


#----------------------------------------
# define spherical & planar sky circles
sph_circle = CircleSphericalSkyRegion(
    center=SkyCoord(50, 45, unit='deg', frame='galactic'),
    radius=Angle('30 deg'))
circle = CircleSkyRegion(
    center=SkyCoord(50, 45, unit='deg', frame='galactic'),
    radius=Angle('30 deg'))
# Note: circle is equivalent to transforming from sph_circle
# with sph_circle.to_sky(wcs, include_boundary_distortions=False)


#----------------------------------------
# define transformed-to pixel regions
pix_circ_distort = sph_circle.to_pixel(wcs=wcs,
                    include_boundary_distortions=True,
                    n_points=1000)
pix_circ_nodistort = circle.to_pixel(wcs=wcs)


#----------------------------------------
# get contained points:
distort_mask = sph_circle.contains(skycoords)
nodistort_mask = pix_circ_nodistort.contains(pixcoords)

both_skycoords = skycoords[distort_mask & nodistort_mask]
distort_only_skycoords = skycoords[distort_mask & ~nodistort_mask]
nodistort_only_skycoords = skycoords[~distort_mask & nodistort_mask]

# plot
fig = plt.figure()
fig.set_size_inches(7,3.5)
ax = fig.add_axes([0.15, 0.1, 0.8, 0.8], projection=wcs, aspect='equal')

ax.scatter(skycoords.l.value, skycoords.b.value, label='All',
           transform=ax.get_transform('galactic'), color='lightgrey')
ax.scatter(distort_only_skycoords.l.value, distort_only_skycoords.b.value,
           color='magenta', label='Only within spherical circle',
           transform=ax.get_transform('galactic'))
ax.scatter(nodistort_only_skycoords.l.value, nodistort_only_skycoords.b.value,
           color='lime', label='Only within planar circle',
           transform=ax.get_transform('galactic'))
ax.scatter(both_skycoords.l.value, both_skycoords.b.value, color='orange',
           label='Within both', transform=ax.get_transform('galactic'))

pix_circ_distort.plot(ax=ax, edgecolor='red', facecolor='none',
                    alpha=0.8, lw=3)

pix_circ_nodistort.plot(ax=ax, edgecolor='green', facecolor='none',
                        alpha=0.8, lw=3)

ax.legend(loc='lower right')

ax.set_xlim(-0.5, dataset.config['shape'][1] - 0.5)
ax.set_ylim(-0.5, dataset.config['shape'][0] - 0.5)
ax.set_title("Spherical vs. Planar circle: Center=(50deg,45deg), radius=30deg")