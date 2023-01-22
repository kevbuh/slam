import numpy as np
import cv2
import sys
import os
from display import Display2D, Display3D

W = 640
H = 360

if __name__ == "__main__":
    cap = cv2.VideoCapture('test_countryroad.mp4')

    W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    disp2d, disp3d = None, None

    # print("display", os.getenv("2D"))

    if os.getenv("display2d") is not None:
        # print("got display env")
        disp2d = Display2D(W, H)

    if os.getenv("display3d") is not None:
        # print("got display env")
        disp3d = Display3D(W, H)

    # print(W, H)

    # if os.getenv("ENV") is None:
    #     print("got env env")

    while(cap.isOpened()):
        ret, frame = cap.read()
        # frame = cv2.resize(frame, (W//3, H//3))
        # print(f"r ----- frame:{frame.shape}")

        # Initiate STAR detector
        orb = cv2.ORB_create()

        # find the keypoints with ORB
        kp = orb.detect(frame, None)

        # compute the descriptors with ORB
        kp, des = orb.compute(frame, kp)

        # draw only keypoints location,not size and orientation
        final_frame = cv2.drawKeypoints(
            frame, kp, outImage=None, color=(255, 0, 255), flags=0)

        cv2.imshow('final', final_frame)

        if disp2d is not None:
            print("2d display")

            # img = slam.mapp.frames[-1].annotate(frame)
            disp2d.paint(final_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
