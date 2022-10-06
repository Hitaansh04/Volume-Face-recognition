import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
prevTime = 0
currTime = 0
cap = cv2.VideoCapture(0)
detector=htm.handDetector()
while True:
      success, img = cap.read()
      img=detector.findHands(img,draw=True)
      lmlist=detector.findPosition(img,draw=False)
      if len(lmlist)!=0:
            print(lmlist[4])
      currTime = time.time()
      fps = 1 / (currTime - prevTime)
      prevTime = currTime
      cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0,255, 255), 3)

      cv2.imshow("Image", img)
      cv2.waitKey(1)


