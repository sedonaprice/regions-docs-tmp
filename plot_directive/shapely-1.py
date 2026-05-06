import matplotlib.pyplot as plt
from regions import PixCoord, CirclePixelRegion
from shapely.geometry import Point

# Make an example region
region = CirclePixelRegion(center=PixCoord(3, 2), radius=2)

# Convert to Shapely
point = Point(region.center.x, region.center.y)
circle = point.buffer(region.radius)

# Actually, this is a polygon approximation of the circle
print(circle)

# Plot the result
x, y = circle.exterior.xy
ax = plt.subplot(1, 1, 1)
ax.set_aspect('equal')
ax.plot(x, y, 'g-')