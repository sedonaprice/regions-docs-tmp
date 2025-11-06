import numpy as np
import matplotlib.pyplot as plt
from regions import RegionBoundingBox
bbox = RegionBoundingBox(2, 7, 3, 8)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
rng = np.random.default_rng(0)
ax.imshow(rng.random((10, 10)), interpolation='nearest',
          cmap='viridis')
ax.add_patch(bbox.as_artist(facecolor='none', edgecolor='white',
             lw=2.))