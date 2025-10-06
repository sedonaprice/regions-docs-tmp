from astropy.coordinates import Angle, SkyCoord
import matplotlib.pyplot as plt

from regions import CircleSphericalSkyRegion, make_example_dataset

dataset = make_example_dataset(data='simulated')
wcs = dataset.wcs

sph_sky_center = SkyCoord(42, 30, unit='deg', frame='galactic')
sph_sky_radius = Angle(12, 'deg')
sph_sky_region = CircleSphericalSkyRegion(sph_sky_center, sph_sky_radius)

fig, ax = plt.subplots(subplot_kw=dict(projection=wcs))
ax.grid(True)
ax.set_xlabel(r"Galactic $\ell$")
ax.set_ylabel(r"Galactic $b$")

sph_sky_region.to_pixel(
   wcs=wcs,
   include_boundary_distortions=True,
   discretize_kwargs={"n_points":1000}
).plot(ax=ax, color='tab:red', lw=3)

sph_sky_center2 = SkyCoord(42, 43, unit='deg', frame='galactic')
sph_sky_radius2 = Angle(25, 'deg')
sph_sky_region2 = CircleSphericalSkyRegion(sph_sky_center2, sph_sky_radius2)
poly_sph_sky2 = sph_sky_region2.discretize_boundary(n_points=1000)
ax.plot(
    poly_sph_sky2.vertices.l,
    poly_sph_sky2.vertices.b,
    lw=2, color="tab:blue",
    transform=ax.get_transform('galactic'),
)