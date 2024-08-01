from django.shortcuts import render
from django.http import HttpResponse
import os
import cv2 as cv

# i=0
def test(request):
    i=0
    cap = cv.VideoCapture(0)

    while(True):
        ret,frame = cap.read()
        # cv.imshow('frame',frame)
        # print(frame,i)
        if(ret):
            try:
                suc = cv.imwrite('./image %d.png'%i,frame)
            except(suc):
                print(suc)
            print('success',suc)
        if(cv.waitKey(1) & 0xFF==ord('q')):
            break
        if i==10:
            break
        i+=1
    cap.release()
    cv.destroyAllWindows()
    return HttpResponse('Hello im inside function')