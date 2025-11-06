from astropy.coordinates import SkyCoord, Angle
from astropy.visualization.wcsaxes.frame import EllipticalFrame
from astropy import units as u

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from regions import (CircleSphericalSkyRegion,
                     RangeSphericalSkyRegion,
                     make_example_dataset)


dataset = make_example_dataset(data='simulated')
wcs = dataset.wcs

dataset_icrs = make_example_dataset(data='simulated', config={'ctype':
                                                         ('RA---AIT',
                                                          'DEC--AIT')})
wcs_icrs = dataset_icrs.wcs

sph_circ = CircleSphericalSkyRegion(SkyCoord(100,-40,
                                             unit=u.deg,
                                             frame="galactic"),
                                    30*u.deg)
sph_range = RangeSphericalSkyRegion(frame="galactic",
                                    longitude_range=[-45,45]*u.deg,
                                    latitude_range=[0,45]*u.deg)
sph_circ_transf = sph_circ.transform_to("icrs")
sph_range_transf = sph_range.transform_to("icrs")


fig = plt.figure()
fig.set_size_inches(7,7)

axes = []
axes.append(fig.add_axes([0.15, 0.575, 0.8, 0.425],
                         projection=wcs,
                         frame_class=EllipticalFrame))
axes.append(fig.add_axes([0.15, 0.05, 0.8, 0.425],
                         projection=wcs_icrs,
                         frame_class=EllipticalFrame))

ax = axes[0]
ax.coords.grid(color='gray')
ax.set_xlabel(r"Galactic $\ell$", labelpad=10)
ax.set_ylabel(r"Galactic $b$")
ax.set_title("Galactic coordinates", pad=5)

patch = sph_circ.to_pixel(
   wcs=wcs,
   include_boundary_distortions=True,
   discretize_kwargs={"n_points":1000}
).plot(ax=ax, color='tab:blue', lw=3)

sph_range.to_pixel(
   wcs=wcs,
   include_boundary_distortions=True,
   discretize_kwargs={"n_points":250}
).plot(ax=ax, color='tab:red', lw=3)

bound_color = 'tab:blue'
bound_lw = 0.75
bound_zord = 2
bound_lon, bound_lat = sph_circ.bounding_lonlat
for i in range(2):
    # Need to manually "super sample" to get correct distortion.
    # Unfortunately axv/hline works for just "aitoff" projection,
    # not doing a WCS it seems.
    npt = 250
    xarr = np.repeat(bound_lon[i].degree, npt)
    yarr = np.linspace(-90,90,num=npt,endpoint=True)
    l1 = Line2D(xarr, yarr, ls='--', color=bound_color,
                lw=bound_lw, zorder=bound_zord,
                transform=ax.get_transform('galactic'))
    xarr = np.linspace(-180,180,num=npt,endpoint=True)
    yarr = np.repeat(bound_lat[i].degree, npt)
    l2 = Line2D(xarr, yarr, ls='--', color=bound_color,
                lw=bound_lw, zorder=bound_zord,
                transform=ax.get_transform('galactic'))
    ax.add_artist(l1)
    ax.add_artist(l2)


bound_color = 'tab:red'
sph_range.bounding_circle.to_pixel(
   wcs=wcs,
   include_boundary_distortions=True,
   discretize_kwargs={"n_points":1000}
).plot(ax=ax, color='tab:red', lw=bound_lw, ls='--', zorder=bound_zord)

patch.set_clip_path(ax.coords.frame.patch)

ax.set_xlim(20,340)
ax.set_ylim(10,170)

ax = axes[1]
ax.coords.grid(color='gray')
ax.set_xlabel("RA", labelpad=10)
ax.set_ylabel("Dec")
ax.set_title("ICRS coordinates", pad=5)

patch = sph_circ_transf.to_pixel(
   wcs=wcs_icrs,
   include_boundary_distortions=True,
   discretize_kwargs={"n_points":1000}
).plot(ax=ax, color='tab:blue', lw=3)

sph_range_transf.to_pixel(
   wcs=wcs_icrs,
   include_boundary_distortions=True,
   discretize_kwargs={"n_points":250}
).plot(ax=ax, color='tab:red', lw=3)


bound_color = 'tab:blue'
bound_lw = 0.75
bound_zord = 2
bound_lon, bound_lat = sph_circ_transf.bounding_lonlat
for i in range(2):
    # Need to manually "super sample" to get correct distortion.
    # Unfortunately axv/hline works for just "aitoff" projection,
    # not doing a WCS it seems.
    npt = 250
    xarr = np.repeat(bound_lon[i].degree, npt)
    yarr = np.linspace(-90,90,num=npt,endpoint=True)
    l1 = Line2D(xarr, yarr, ls='--', color=bound_color,
                lw=bound_lw, zorder=bound_zord,
                transform=ax.get_transform('icrs'))
    xarr = np.linspace(-180,180,num=npt,endpoint=True)
    yarr = np.repeat(bound_lat[i].degree, npt)
    l2 = Line2D(xarr, yarr, ls='--', color=bound_color,
                lw=bound_lw, zorder=bound_zord,
                transform=ax.get_transform('icrs'))
    ax.add_artist(l1)
    ax.add_artist(l2)


bound_color = 'tab:red'
bound_lon, bound_lat = sph_range_transf.bounding_lonlat
for i in range(2):
    # Need to manually "super sample" to get correct distortion.
    # Unfortunately axv/hline works for just "aitoff" projection,
    # not doing a WCS it seems.
    npt = 250
    xarr = np.repeat(bound_lon[i].degree, npt)
    yarr = np.linspace(-90,90,num=npt,endpoint=True)
    l1 = Line2D(xarr, yarr, ls='--', color=bound_color,
                lw=bound_lw, zorder=bound_zord,
                transform=ax.get_transform('icrs'))
    xarr = np.linspace(-180,180,num=npt,endpoint=True)
    yarr = np.repeat(bound_lat[i].degree, npt)
    l2 = Line2D(xarr, yarr, ls='--', color=bound_color,
                lw=bound_lw, zorder=bound_zord,
                transform=ax.get_transform('icrs'))
    ax.add_artist(l1)
    ax.add_artist(l2)
sph_range_transf.bounding_circle.to_pixel(
   wcs=wcs_icrs,
   include_boundary_distortions=True,
   discretize_kwargs={"n_points":1000}
).plot(ax=ax, color='tab:red', lw=bound_lw, ls='--', zorder=bound_zord)


patch.set_clip_path(ax.coords.frame.patch)

ax.set_xlim(20,340)
ax.set_ylim(10,170)
ax.coords[0].set_format_unit(u.deg)