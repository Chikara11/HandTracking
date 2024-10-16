"""
VolumeControl.py

This script controls the system's volume by using hand gestures, specifically by measuring the distance 
between the thumb and index finger. It uses the `HandDetector` class from `HandTrackingModule.py`.
"""

import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math

from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

###
wCam, hCam = 640,480
###

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(3,hCam)
pTime = 0

detector = htm.HandDetector(detectionConf=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

volRange = volume.GetVolumeRange() 
minVol = volRange[0]
maxVol = volRange[1]
vol=0
volBar=400
volPercentage=0


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    #Added a bounding box
    lmList, bbox = detector.findPosition(img,draw =False)
    if len(lmList) !=0:
        #print(lmList[4],lmList[8])
        x1, y1 = lmList[4][1],lmList[4][2]
        x2, y2 = lmList[8][1],lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2

        cv2.circle(img, (x1,y1), 15, (255,0,255), cv2.FILLED)
        cv2.circle(img, (x2,y2), 15, (255,0,255), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (255,0,255),3)
        cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)

        length = math.hypot(x2-x1,y2-y1)
        #print(length)

        # Hand range 50 - 300
        # Volume range -96 - 0

        vol = np.interp(length,[50,300],[minVol,maxVol])
        volBar = np.interp(length,[50,300],[400,150])
        volPercentage = np.interp(length,[50,300],[0,100])
        volume.SetMasterVolumeLevel(vol, None)

        print(vol)


        if length<50:
            cv2.circle(img, (cx,cy), 15, (0,255,0), cv2.FILLED)
    cv2.rectangle(img, (50,150), (85,400), (255,0,0), 3)
    cv2.rectangle(img, (50,int(volBar)), (85,400), (255,0,0), cv2.FILLED)
    cv2.putText(img,f' {int(volPercentage)}%',(40,450),cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),1)

             


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,f'FPS: {int(fps)}',(20,50),cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),1)

    cv2.imshow("Img", img)
    cv2.waitKey(1)



