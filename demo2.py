import cv2
import numpy as np

dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)

data = []
while True:
    ret, img = capture.read()
    if ret:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray,1.3)
        for x,y,w,h in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h),(255,0,0), 5)
            myFace = img[y:y+h, x:x+w, :]
            myFace = cv2.resize(myFace, (50,50))

            if len(data) < 100:
                data.append(myFace)
                print(len(data))

        cv2.imshow('result', img)
        if cv2.waitKey(1) & 0xFF == 27 or len(data) >= 100:
            break
    else:
        print("Camera not working")

data = np.asarray(data)
np.save('Ashish.npy', data)
capture.release()
cv2.destroyAllWindows()













