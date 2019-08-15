
import argparse
import cv2
import numpy as np
import random

refPt=[]
jihe=[]
cropping=False

def ramdom_pixels(frame):
	height = frame.shape[0]
	weight = frame.shape[1]
	for k in range(50000):
		i = random.randint(0,height-1)
		j = random.randint(0,weight-1)
		color = (random.randrange(256),random.randrange(256),random.randrange(256))
		frame[i,j] = color
	
	#cv2.imshow("Noize", frame)
	#cv2.waitKey(0)

def access_pixels(frame):
	print(frame.shape)
	height = frame.shape[0]
	weight = frame.shape[1]
	channels = frame.shape[2]
	print("weight : %s, height : %s, channel : %s" %(weight, height, channels))
	
	for row in range(height):
		for col in range(weight):
			for c in range(channels):
				pv = frame[row, col, c]     
				frame[row, col, c] = 255 - pv
	#cv2.imshow("fanxiang", frame)


def click_and_crop(event,x,y,flags,param):
    global refPt,cropping
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt=[(x,y)]
        print(x,y)
        cropping=True
        
        px=image[10,10]
        print px
        '''blue=clone[10,10,0]
        print blue
        green=clone[10,10,1]
        print green
        red=clone[10,10,2]
        print red'''
        '''h, w, _ = image.shape

        print(h,w)'''
        '''
        for a in range(h):
            for b in range(w):
                print(image[a,b])
                jihe.append(list(image[a,b]))
                #num +=1'''

    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x,y))
        print(x,y)
        cropping=False
        
        cv2.rectangle(image,refPt[0],refPt[1],(0,0,200),2)
        cv2.imshow("huangzhicheng reseach",image)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
clone = image.copy()
cv2.namedWindow("huangzhicheng reseach")
cv2.setMouseCallback("huangzhicheng reseach", click_and_crop)


while True:
	cv2.imshow("huangzhicheng reseach", image)
	key = cv2.waitKey(0) & 0xFF

	if key == ord("r"):
		image = clone.copy()
	elif key == ord("f"):
		access_pixels(image)
	elif key == ord("v"):
		ramdom_pixels(image)
	elif key == ord("c"):
		break

if len(refPt) == 2:
	roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	cv2.imshow("ROI", roi)
	
	h, w, _ = roi.shape
	print("----",h,w,"----")
	for a in range(h):
		for b in range(w):
			#print(roi[a,b])
			jihe.append(list(roi[a,b]))
			#num +=1
	print(jihe)
	cv2.waitKey(0)

cv2.destroyAllWindows()
