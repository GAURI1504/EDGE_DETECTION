# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 18:30:06 2021

@author: gauri
"""

import cv2
video_capture = cv2.VideoCapture(0)
while(1):
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    edge_canny = cv2.Canny(frame,100,200)
    # Display the resulting frame
    cv2.imshow('Video', frame)
    cv2.imshow('Edge', edge_canny)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()