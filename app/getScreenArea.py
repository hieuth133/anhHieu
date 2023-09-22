from PIL import ImageGrab
import numpy as np
import cv2

def getScreenArea(area, save=False):
    screen = np.array(ImageGrab.grab(bbox=area))
    if save:
        cv2.imwrite("test.png", screen)
    return screen


if __name__ == "__main__":
    getScreenArea([0,0,800,600], save=True)

