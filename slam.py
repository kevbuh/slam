import numpy as np
import cv2
import sys
import os

W = 640
H = 360

if __name__ == "__main__":
    cap = cv2.VideoCapture('test_countryroad.mp4')

    W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # print(W, H)

    # if os.getenv("ENV") is None:
    #     print("got env env")

    while(cap.isOpened()):
        ret, frame = cap.read()
        frame = cv2.resize(frame, (W//3, H//3))
        # print(f"r ----- frame:{frame.shape}")

        # Initiate STAR detector
        orb = cv2.ORB_create()

        # find the keypoints with ORB
        kp = orb.detect(frame, None)

        # compute the descriptors with ORB
        kp, des = orb.compute(frame, kp)

        # draw only keypoints location,not size and orientation
        final_frame = cv2.drawKeypoints(
            frame, kp, outImage=None, color=(0, 255, 0), flags=0)

        cv2.imshow('final', final_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
