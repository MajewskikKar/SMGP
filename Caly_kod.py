
import requests
import cv2
import os


#d ownloading file
numer_ark =input("wpisz numer arksza") #str(250)
response = requests.get("http://bazadata.pgi.gov.pl/data/smgp/arkusze_skany/smgp0" + numer_ark + ".jpg")

file = open(numer_ark + ".png", "wb")
file.write(response.content)
file.close()


#splitting SMGP into 4 pieces

now = os.getcwd()
path = os.path.join(now, numer_ark)+".png"
image = cv2.imread(path)
(h, w) = image.shape[:2]
centerX, centerY = (w//2), (h//2)

topLeft = image[0:centerY, 0:centerX]
topRight = image[0:centerY, centerX:w]
#bottomLeft = image[]
#bottomRight = image[]
#cv2.imshow("TopRight", topLeft)
#cv2.waitKey(0)



#wyszukiwanie rogów
path1 = os.path.join(now, "rog.jpg")
method = cv2.TM_SQDIFF_NORMED

# Read the images from the file
small_image = cv2.imread(path1)
large_image = cv2.imread(path)

result = cv2.matchTemplate(small_image, large_image, method)

# We want the minimum squared difference
mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = small_image.shape[:2]

# Step 3: Draw the rectangle on large_image
cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# Display the original image with the rectangle around the match.

cv2.imshow('output',large_image)

# The image is only displayed if we call this
cv2.waitKey(0)

