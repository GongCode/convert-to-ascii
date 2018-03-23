import cv2
import time
from tqdm import tqdm
from imageconvert import img2ascii, print_ascii

def video2ascii(video, pixellation):
	vidcap = cv2.VideoCapture(video)
	vidlength = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

	success,image = vidcap.read()
	img_arr = [] 

	for count in tqdm(range(vidlength - 1)):
		success,image = vidcap.read()
		if cv2.waitKey(10) == 27:
			break
		img_arr.append(img2ascii(image, pixellation))
	return img_arr



pixellation = 10
video = 'fortheculture.mp4'
ascii_video = video2ascii(video, pixellation)

while True:
	for x in range(len(ascii_video)):
		for y in range(30):
			print(flush=True)
		print_ascii(ascii_video[x])
		time.sleep(.04)
