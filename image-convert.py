import os
from skimage import io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import numpy as np

#file is name of file you want to convert
#pixellation is square width of how many pixels of original should be in one pixel of output
def img2ascii(image, pixellation):
	#defining array that stores the value of each pixel in the new image array
	ascii_length = int(len(gray_image[1]) / pixellation)
	ascii_height = int(len(gray_image) / pixellation / 2)
	ascii_image_values = np.ndarray(shape=(ascii_height, ascii_length), dtype = float)
	#x and y are the position in the new ascii image
	for x in range(ascii_length):
		for y in range(2 * ascii_height):
			#find the average value of the pixe in the grayscale original image
			count = 0
			total = 0
			#gray_x and gray_y are the x and y position in the original grayscale image
			for gray_x in range((x * pixellation), ((x + 1) * pixellation)):
				for gray_y in range((y * pixellation), ((y + 1) * pixellation)):
					count = count + 1
					total = total + gray_image[gray_y][gray_x]
			ascii_image_values[int(y / 2)][x] = total / count

	for y in range(ascii_height):
		line = ''
		for x in range(ascii_length):
			line = line + to_ascii(ascii_image_values[y][x])
		print(line)

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

def print_ascii(ascii_image):
	for x in range(len(ascii_image)):
		line = ''
		for y in range(len(ascii_image[0])):
			line = line + ascii_image[x][y]
		print(line)



#name of file you want to convert
file = 'mountain.jpg'
#square width of how many pixels of original should be in one pixel of output
pixellation = 10
#opening then converting image to grayscale
gray_image = rgb2gray(io.imread(os.path.join('mountain.jpg')))

img2ascii(gray_image, pixellation)