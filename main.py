from ImageOption import *
from Tools import *


# import the required library
import cv2


#display the intro
IntroDisplay()
Menue()

# read the input image
image = cv2.imread('image2.jpeg')

# define the alpha and beta
alpha = 1.5 # Contrast control
beta = 10 # Brightness control

# call convertScaleAbs function
adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# display the output image
cv2.imshow('adjusted', adjusted)
cv2.waitKey(100)

username = input("Enter username:")
print("Username is: " + username)
#cv2.destroyAllWindows()
newimage = displayText(image)
image = newimage 
cv2.imshow('newimage', image)
cv2.waitKey(100)
x = input()


