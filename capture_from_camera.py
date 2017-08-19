import cv2

  
if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    # w, h = (640.0, 480.0)
    w, h = (1280, 720)
    if cv2.__version__[0]=='2':
        cap.set(3, w)
        cap.set(4, h)
    else:
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
    num = 0
    while True:
        ret, img = cap.read()
            
        cv2.imshow("camera", img)
        key = 0xFF & cv2.waitKey(10)
        if key == 27:  
            break  
        if key == ord(' '):  
            num = num+1  
            filename = "frames_%s.jpg" % num
            cv2.imwrite(filename, img)
        if num == 30:
            break

    cv2.destroyAllWindows()
