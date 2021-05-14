

import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')   # to load the cascade
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
capture = cv2.VideoCapture(0)
while True:
    flag , image = capture.read()

    grayScale = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayScale,1.1,4) #detect faces
    for (x,y,w,h) in faces :
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        face_gray = grayScale[y:y+h , x:x+w]
        face_colour = image[y:y+h , x:x+h]

        eyes=eye_cascade.detectMultiScale(face_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(face_colour,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('Face and eye detection',image)


    key=cv2.waitKey(30) & 0xff
    if key == 27:
        break

capture.release()



