import cv2
from config import *

def blur(filename):
	nameOfFile = filename.split('.')[0]
	saveName = f'{nameOfFile}.{save_format}'

	image = cv2.imread(filename)
	blurred_image = cv2.GaussianBlur(image, (blur_stength, blur_stength), 0)

	cv2.imwrite(saveName, blurred_image)
	return saveName