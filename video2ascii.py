import cv2
import time
from tqdm import tqdm
from image2ascii import img2ascii, print_ascii

#video is video to convert
#pixellation is square width of how many pixels of original should be in one pixel of output
def video2ascii(video, pixellation=10):
	vidcap = cv2.VideoCapture(video)
	vidlength = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

	#used in printing
	wait = 1.0/vidcap.get(cv2.CAP_PROP_FPS)

	success,image = vidcap.read()
	img_arr = [] 

	#tqdm makes a status bar
	for count in tqdm(range(vidlength - 1)):
		success,image = vidcap.read()
		img_arr.append(img2ascii(image, pixellation))
	#return tuple of array of frames and wait time between frames to print
	return (img_arr, wait)

#video is array of images. wait is time to wait between printing each image
#default wait will make the video 24 fps
def print_video(video, wait=.04166):
	for x in range(len(video)):
		print_ascii(video[x])
		time.sleep(wait)