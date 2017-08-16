import cv2
  
import time  
  
if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
   
    num = 0
    while True:  
        ret, img = cap.read()
        cv2.imshow("camera",img)

        key = 0xFF & cv2.waitKey(10)
        if key == 27:  
            break  
        if key == ord(' '):  
            num = num+1  
            filename = "frames_%s.jpg" % num
            cv2.imwrite(filename,img)
        if num == 30:
            break

    cv2.destroyAllWindows()
