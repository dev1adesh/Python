import cv2
img = cv2.imread('bugatti.jpg',cv2.IMREAD_UNCHANGED)
 
# The function cv2.imshow() is used to display an image in a window.
cv2.imshow('graycsale image',img)
cv2.waitKey(0)

scalepercent =50

width = int(img.shape[1] * scalepercent/100)
height = int(img.shape[0]* scalepercent*100)

output = cv2.resize(img, (width,height))

cv2.imwrite('newImage.png',output)
cv2.waitKey(0)
