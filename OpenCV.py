# Image Resizing 
import numpy as np  #if u want to use the functions or variables present in the numpy package we use np in this program rather than using the whole word numpy which takes 4 key strokes
import cv2
import matplotlib.pyplot as plt 

#image = cv2.imread("image2.jpg") #if i want to read the image on the disc , currently image1.jpg is in the same directory heirarchy as that of this program
cam = cv2.VideoCapture(0)
result, image = cam.read() 

if result:
    cv2.imshow("captured picure",image)
    cv2.waitKey()
    cv2.imwrite("image.jpg" , image)
else:
    print("no image found")

image = cv2.imread("image.jpg")
new = cv2.resize(image, (1200, 780))
cv2.imshow('old image', image)
cv2.waitKey()
cv2.imshow('new resized image',new )
cv2.waitKey()
# writing the content of new resize image to file 
cv2.imwrite("newimage.jpg", new) #used to write the image to the disc where the method imwrite takes 2 arguments where the first argument is file name along with the format the file will be saved in and the second argument from which the image content is taken from
blurimage = cv2.blur(image, (50,50))  
cv2.imshow('blurred  image', blurimage)
cv2.waitKey()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Lion', gray_image)
cv2.waitKey()

h, w = image.shape[:2]
center = (w / 2, h / 2)


mat = cv2.getRotationMatrix2D(center, 90, 1)

rotating = cv2.warpAffine(image, mat, (h, w))

cv2.imshow('rotated', rotating)


cv2.waitKey()

img_blur = cv2.GaussianBlur(image,(3,3), sigmaX=0, sigmaY=0) 
#sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
#sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis

sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection

cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.waitKey()

src = cv2.imread("image5.jpg", cv2.IMREAD_GRAYSCALE); 
 
# Basic threhold example 

th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY); 
cv2.imshow('grey scale image', dst)
cv2.waitKey()

# cap = cv2.VideoCapture(0) 
# fgbg = cv2.createBackgroundSubtractorMOG2() 
  
# while(1): 
#     ret, frame = cap.read() 
  
#     fgmask = fgbg.apply(frame) 
   
#     cv2.imshow('fgmask', fgmask) 
#     cv2.imshow('frame',frame ) 
  
      
#     k = cv2.waitKey(30) & 0xff
#     if k == 27: 
#         break


# cap.release()

image = cv2.imread("image2.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

eroded = cv2.erode(gray.copy(), None, iterations=2)
cv2.imshow("Eroded 2 times", eroded)
eroded = cv2.erode(gray.copy(), None, iterations=10)
cv2.imshow("Eroded 10 times", eroded)
cv2.waitKey(0)
