import cv2
import numpy as np

cap = cv2.VideoCapture('rtsp://admin:GG322322@172.18.160.32:554/102')

while True:
    ret, frame = cap.read()
    cv2.imshow('video feed', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()