import os
from skimage import io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import numpy as np

# file = input("Please enter file name: ")
# pixels = input("Please enter pixels: ")
file = 'mountain.jpg'
pixellation = 10

image = io.imread(os.path.join('mountain.jpg'))

gray_image = rgb2gray(image)

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4),
                               sharex=False, sharey=False)


length = len(gray_image[1])
height = len(gray_image)

nlength = int(length / pixellation)
nheight = int(height / pixellation)
nimage_values = np.ndarray(shape=(nheight, nlength), dtype = float)
nimage = np.ndarray(shape=(nheight, nlength), dtype = str)

for x in range(nlength):
	for y in range(nheight):
		count = 0
		total = 0
		for xx in range((x * pixellation), ((x + 1) * pixellation)):
			for yy in range((y * pixellation), ((y + 1) * pixellation)):
				count = count + 1
				total = total + gray_image[yy][xx]
		nimage_values[y][x] = total / count

def to_ascii(x):
	if x > .9:
		return '█'
	if x > .75:
		return '▓'
	if x > .5:
		return '▒'
	if x > .25:
		return '░'
	return ' '

for y in range(nheight):
	line = ''
	for x in range(nlength):
		line = line + to_ascii(nimage_values[y][x])
	print(line)










# ax1.imshow(gray_image, cmap="gray")
# ax2.imshow(nimage, cmap="gray")

# plt.show()