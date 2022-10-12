
import requests
import cv2
import os


# downloading file
numer_ark = input("wpisz numer arksza") # str(210)
response = requests.get("http://bazadata.pgi.gov.pl/data/smgp/arkusze_skany/smgp0" + numer_ark + ".jpg")

file = open(numer_ark + ".png", "wb")
file.write(response.content)
file.close()

# splitting SMGP into 4 pieces (not currently used)

cwd = os.getcwd()
path = os.path.join(cwd, numer_ark)+".png"
image = cv2.imread(path)
# (h, w) = image.shape[:2]
# centerX, centerY = (w//2), (h//2)

# topLeft = image[0:centerY, 0:centerX]
# topRight = image[0:centerY, centerX:w]
# #bottomLeft = image[]
# #bottomRight = image[]
# #cv2.imshow("TopRight", topLeft)
# #cv2.waitKey(0)

corner_names = {
    "lt": (1,1),
    "rt": (0, 1),
    "lb": (1, 0),
    "rb": (0, 0)
}

corner_cords = []
large_image = cv2.imread(path)

for corner, flags in corner_names.items():
    path1 = os.path.join(cwd, (corner + "rog.jpg"))
    method = cv2.TM_SQDIFF_NORMED # one of six possible methods

    # Read the images from the file
    small_image = cv2.imread(path1)

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

    x_mult, y_mult = flags
    temp_corner = (MPx+tcols*x_mult, MPy+trows*y_mult)
    corner_cords.append(temp_corner)

for corner in corner_cords:
    cv2.circle(large_image, corner, 20, (255,0, 255), 28)

print(corner_cords)

lt, rt, lb, rb = corner_cords
# this doesn't work
min_x, min_y = lt
max_x, max_y = rb

cropped_image = large_image[min_y:max_y, min_x:max_x]

w = max_x - min_x 
h = max_y - min_y 

# Display the original image with the rectangle around the match.

cv2.imshow('output', cropped_image)
# cv2.imshow('output',large_image[min_x:min_x+w, min_y:min_y+h])

# The image is only displayed if we call this
cv2.waitKey(0)

