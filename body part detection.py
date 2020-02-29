import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
leftear_cascade = cv2.CascadeClassifier('haarcascade_mcs_leftear.xml')
rightear_cascade = cv2.CascadeClassifier('haarcascade_mcs_rightear.xml')
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        leftear = leftear_cascade.detectMultiScale(roi_gray)
        for (mx,my,mw,mh) in leftear:
             cv2.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(0,255,255),2)

        rightear = rightear_cascade.detectMultiScale(roi_gray)
        for (mx,my,mw,mh) in rightear:
             cv2.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(0,255,255),2)

                
        mouth = mouth_cascade.detectMultiScale(roi_gray)
        for (mx,my,mw,mh) in mouth:
             my = int(my - 0.15*mh)
             cv2.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(255,40,255),0)
            
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
