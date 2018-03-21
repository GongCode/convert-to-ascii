import cv2
import imageconvert

def video2ascii(video, pixellation):
	vidcap = cv2.VideoCapture(video)

	success,image = vidcap.read()
	# image is an array of array of [R,G,B] values

	count = 0;
	img_arr = [] 
	while success:
		success,image = vidcap.read()
		img_arr.append(img2ascii(image))
		if cv2.waitKey(10) == 27:
			break
		count += 1




video = 'fortheculture.mp4'
