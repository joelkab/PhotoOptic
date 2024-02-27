import cv2
def displayText(image):
    print("I see you want to brighten your image \n")
    brt = input()
    alpha = 1.5 # Contrast control
    beta = int(brt) # Brightness control

    newbrt = cv2.convertScaleAbs(image, alpha=1, beta=beta)
    cv2.imshow('newbrt', newbrt)
    cv2.waitKey(100)
    return newbrt



