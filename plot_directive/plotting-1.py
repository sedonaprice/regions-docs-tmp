from regions import PixCoord, CirclePixelRegion
import matplotlib.pyplot as plt

region = CirclePixelRegion(PixCoord(x=0.3, y=0.42), radius=0.5)
artist = region.as_artist()

axes = plt.gca()
axes.set_aspect('equal')
axes.add_artist(artist)
axes.set_xlim([-0.5, 1])
axes.set_ylim([-0.5, 1])