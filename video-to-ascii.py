import cv2
import time
from imageconvert import img2ascii, print_ascii

def video2ascii(video, pixellation):
	vidcap = cv2.VideoCapture(video)

	success,image = vidcap.read()

	count = 0;
	img_arr = [] 
	while success and count < 5000:
		success,image = vidcap.read()
		if cv2.waitKey(10) == 27:
			break
		count += 1
		try:
			img_arr.append(img2ascii(image, pixellation))
		except:
			continue
	return img_arr



pixellation = 10
video = 'fortheculture.mp4'
ascii_video = video2ascii(video, pixellation)

while True:
	for x in range(len(ascii_video)):
		for y in range(30):
			print()
		print_ascii(ascii_video[x])
		time.sleep(.04)
