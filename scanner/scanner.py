import urllib.request as req
import cv2 
import numpy as np
import time
from PIL import Image
url=''#attach the url address of the live image from your browser
n=1
while n:
    img=req.urlopen(url)
    img_bytes=bytearray(img.read())
    img_np=np.array(img_bytes,dtype=np.uint8)
    frame=cv2.imdecode(img_np,-1)
    frame_in=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame_blur=cv2.GaussianBlur(frame_in,(5,5),0)
    frame_edge=cv2.Canny(frame_blur,30,50)
    contours,h=cv2.findContours(frame_edge,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        max_contour=max(contours,key= cv2.contourArea)
        if cv2.contourArea(max_contour)>5000:
            x,y,w,h=cv2.boundingRect(max_contour)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            object_size=frame[y:y+h,x:x+w]
    cv2.imshow('my smart scanner',frame)
    if cv2.waitKey(1) == ord('s'):
        img_pil=Image.fromarray(object_size)
        time_mark=time.strftime('%Y-%m-%d-%H-%M-%S')
        img_pil.save(time_mark+'.pdf')
        print(time_mark)
    elif cv2.waitKey(1)==ord('e'):
        n=0