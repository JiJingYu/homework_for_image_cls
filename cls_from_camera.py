import cv2
import inception_predict
import time  
  
if __name__ == '__main__':
    """
    cap = cv2.VideoCapture(0)
    # w, h = (640.0, 480.0)
    w, h = (1280, 720)
    if cv2.__version__[0]=='2':
        cap.set(3, w)
        cap.set(4, h)
    else:
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
    """
    num = 0
    while True:
        cap = cv2.VideoCapture(0)
        # w, h = (640.0, 480.0)
        w, h = (1280, 720)
        if cv2.__version__[0]=='2':
            cap.set(3, w)
            cap.set(4, h)
        else:
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
        for i in range(20):
            cap.read()
        ret, img = cap.read()
        cap.release()
	
        n_top = inception_predict.predict_from_array(img, inception_predict.mod, inception_predict.synsets)
        print(n_top)
        n_top_str = "\n".join([str(cls) for cls in n_top])
    
        y0, dy = 500, 25
        for i, txt in enumerate(n_top_str.split('\n')):
            y = y0 + i * dy
            cv2.putText(img, txt, (50, y), cv2.FONT_HERSHEY_SIMPLEX, .6, (0, 0, 255), 2, 2)
            
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
