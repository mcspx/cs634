# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 11:24:12 2014

@author: Wasit
"""

import numpy as np
import cv2

def calHough(event,x,y,flags,param):
    imgc=img[y-50:y+50, x-50:x+50]
    gray = cv2.cvtColor(imgc,cv2.COLOR_BGR2GRAY)
    if event == cv2.EVENT_MOUSEMOVE:
        edges = cv2.Canny(gray,50,150,apertureSize = 3)
        lines = cv2.HoughLinesP(edges,1,np.pi/180,80,30,10)
        for x1,y1,x2,y2 in lines[0]:
            cv2.line(imgc,(x1,y1),(x2,y2),(0,255,0),2)
            print("angle: %.3f"%(np.arctan2(y1-y2,x2-x1)*180/np.pi))
        cv2.imshow('HoughLines',imgc)

# Load an color image in grayscale
img =cv2.imread('../img/left01.jpg',1)

cv2.namedWindow('image')
cv2.setMouseCallback('image',calHough)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()