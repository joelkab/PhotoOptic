import cv2
import urllib.request
from time import sleep

def displayText(image):
    print("I see you want to brighten your image \n")
    brt = input()
    alpha = 1.5 # Contrast control
    beta = int(brt) # Brightness control

    newbrt = cv2.convertScaleAbs(image, alpha=1, beta=beta)
    cv2.imshow('newbrt', newbrt)
    cv2.waitKey(100)
    return newbrt
def get_NewImage():
    num = int(input("Number of images (Integer): "))
    for i in range(num):
        url = "https://source.unsplash.com/random"
        filename = "/home/student/Desktop/test/image{}.png".format(i) # change the directory- this is
        # is for linux
        urllib.request.urlretrieve(url, filename)
        sleep(1.5)
    return "image0.png" # returns the image name. for multiple images its image(i+1).png



