import os
from skimage import io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

image = io.imread(os.path.join('mountain.jpg'))

gray_image = rgb2gray(image)

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4),
                               sharex=True, sharey=True)
ax1.imshow(image)
ax2.imshow(gray_image, cmap="gray")

plt.show()