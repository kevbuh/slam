import cv2 as cv
import sys

if __name__ == "__main__":
    print("Hello, World!")

    img = cv.imread(cv.samples.findFile("starry-night.jpeg"))

    if img is None:
        sys.exit("Could not read the image.")

    cv.imshow("Display window", img)
    k = cv.waitKey(0)  # will keep screen up until you press a key
