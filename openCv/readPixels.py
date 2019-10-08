
import argparse
import cv2
import numpy as np
import random
from PIL import Image
import glob, os

refPt=[]
jihe=[]
cropping=False

'''
size = 128, 128
for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(file + ".thumbnail", "JPEG")
'''

def ramdom_pixels(frame):
	height = frame.shape[0]
	weight = frame.shape[1]
	for k in range(50000):
		i = random.randint(0,height-1)
		j = random.randint(0,weight-1)
		color = (random.randrange(256),random.randrange(256),random.randrange(256))
		frame[i,j] = color
	print("ramdom ok")
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
	print("reverse ok")

def record_pixels(frame):

	height = frame.shape[0]
	weight = frame.shape[1]
	channels = frame.shape[2]
	f = open('output.txt',mode='w+')
	for row in range(height):
		for col in range(weight):
			#if col%8 == 0:
			#	f.write('\n')
			jihe.append(list(frame[row, col]))
			#for ii in jihe1:

	f.write('['+','.join(str(i) for i in jihe)+']')
	#s = " ".join(jihe)
	f.close()
	print("record ok")

def getImagePix(strlist,pixelX = 1,pixelY = 1):

	data = strlist[pixelX,pixelY]
	img_src.close()
	return data
	
def convertImagePix():
	
	size = 32
	pageTotal = 52
	for a in range(pageTotal):
		#print(a)
		imgName = "image/image-%d%s"%(a,'.jpg')
		outputName = "eplos/o-%d%s"%(a,'.txt')
		print(imgName,outputName)
		f = open(outputName,mode='w+')
		
		img_src = Image.open(imgName)
		#img_src = img_src.convert('L')#white light only
		img_src = img_src.convert('RGB')#RGBA  R G B A Yes OK!
		img_src = img_src.resize((size,size),0)
		#img_src.show()
		strlist = img_src.load()
		
		listAll = []
		for x in range(size):
			for y in range(size):
				pixel = []
				#print("x=%d,y=%d"%(x,y))
				pixel = strlist[y,x]
				pixelHex = ((pixel[0]<<16)|(pixel[1]<<8)|(pixel[2]))
				
				#print "%d %d 0x%x"%(y,x,pixelHex)
				#listAll.append(list(strlist[y, x]))
				#listAll.append(pixelHex)
				if(pixelHex>=0xF7F9F6):
					if y==size-1:
						listAll.append('0,\n')
					else:
						listAll.append('0,')
				else:
					if y==size-1:
						listAll.append('1,\n')
					else:
						listAll.append('1,')

		#f.write('{'+','.join(str(i) for i in listAll)+'}')
		#f.write(','.join(str(i) for i in listAll))
		f.write(''.join(str(i) for i in listAll))
		f.close()


def convertImagePixHex():
	
	row = 24
	col = 48
	pageTotal = 52
	for a in range(pageTotal):
		#print(a)
		imgName = "image/image-%d%s"%(a,'.jpg')
		outputName = "ws2801/o-%d%s"%(a,'.txt')
		print(imgName,outputName)
		f = open(outputName,mode='w+')
		
		img_src = Image.open(imgName)
		#img_src = img_src.convert('L')#white light only
		img_src = img_src.convert('RGB')#RGBA  R G B A Yes OK!
		img_src = img_src.resize((col,row),0)
		#img_src.show()
		strlist = img_src.load()
		
		listAll = []
		for x in range(row):
			for y in range(col):
				pixel = []
				#print("x=%d,y=%d"%(x,y))
				pixel = strlist[y,x]
				pixelHex = ((pixel[0]<<16)|(pixel[1]<<8)|(pixel[2]))
				
				#print "%d %d 0x%x"%(y,x,pixelHex)
				#listAll.append(list(strlist[y, x]))
				listAll.append(pixelHex)
				if y==col-1:
					listAll.append(',\n')
				else:
					listAll.append(',')

				'''
				if(pixelHex>=0xF7F9F6):
					if y==size-1:
						listAll.append('0,\n')
					else:
						listAll.append('0,')
				else:
					if y==size-1:
						listAll.append('1,\n')
					else:
						listAll.append('1,')
				'''
		#f.write('{'+','.join(str(i) for i in listAll)+'}')
		#f.write(','.join(str(i) for i in listAll))
		f.write(''.join(str(i) for i in listAll))
		f.close()

def cutVideo(videoPath):

	vc = cv2.VideoCapture(videoPath)
	c=0

	if vc.isOpened():
		rval , frame = vc.read()
	else:
		rval = False

	timeF = 100
	while rval:
		rval, frame = vc.read()
		if(c%timeF == 0): #1000 frame per cut
			print "image-%d.jpg"%c
			cv2.imwrite('image/image-'+str(c/100) + '.jpg',frame) #save
		c = c + 1
		cv2.waitKey(1)

	vc.release()

def click_and_crop(event,x,y,flags,param):

    global refPt,cropping
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt=[(x,y)]
        print(x,y)
        cropping=True
        #px=image[x,y]
        px = str_strlist[x,y]
        print px
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x,y))
        print(x,y)
        cropping=False
        cv2.rectangle(image,refPt[0],refPt[1],(0,0,200),2)
        cv2.imshow("huangzhicheng reseach",image)

ap = argparse.ArgumentParser()
ap.add_argument("--image", required=True, help="Path to the image")
ap.add_argument("--video", required=True, help="Path to the video")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
clone = image.copy()
cv2.namedWindow("huangzhicheng reseach")
cv2.setMouseCallback("huangzhicheng reseach", click_and_crop)
img_src = Image.open(args["image"])
img_src = img_src.convert('RGBA')# R G B A Yes OK!
str_strlist = img_src.load()

while True:
	cv2.imshow("huangzhicheng reseach", image)
	key = cv2.waitKey(0) & 0xFF

	if key == ord("r"):
		image = clone.copy()
	elif key == ord("f"):
		access_pixels(image)
	elif key == ord("v"):
		ramdom_pixels(image)
	elif key == ord("d"):
		record_pixels(image)
	elif key == ord("g"):
		print(getImagePix(str_strlist,10,10))
	elif key == ord("e"):
		print(convertImagePix())
	elif key == ord("w"):
		print(convertImagePixHex())
	elif key == ord("c"):
		cutVideo(args["video"])
	elif key == ord("q"):
		break

if len(refPt) == 2 and refPt[0] != refPt[1]:
	roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	cv2.imshow("ROI", roi)
	
	h, w, _ = roi.shape
	print "----",h,w,'----'
	for a in range(h):
		for b in range(w):
			#print(roi[a,b])
			jihe.append(list(roi[a,b]))
			#num +=1
	print(jihe)
	cv2.waitKey(0)

cv2.destroyAllWindows()
