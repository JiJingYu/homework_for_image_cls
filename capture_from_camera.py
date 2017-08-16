import cv2.cv as cv  
  
import time  
  
if __name__ == '__main__':  
  
    cv.NamedWindow("camera",1)  
    capture = cv.CaptureFromCAM(0)
   
    num = 0;  
    while True:  
        img = cv.QueryFrame(capture)  
        cv.ShowImage("camera",img)  
  
        key = cv.WaitKey(10)  
        if key == 27:  
            break  
        if key == ord(' '):  
            num = num+1  
            filename = "frmaes_%s.jpg" % num  
            cv.SaveImage(filename,img)
        if num == 30:
            break
  
  
    del(capture)  
    cv.DestroyWindow("camera")
