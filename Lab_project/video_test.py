import cv2
import numpy as np

cap = cv2.VideoCapture('rtsp://admin:admin@192.168.31.235:554/live1.sdp')

while True:
    ret, frame = cap.read()
    cv2.imshow('video feed', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()