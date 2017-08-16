import cv2
import inception_predict
import time

if __name__ == '__main__':
    num = 0
    while True:
        cmd = raw_input("please input the command!!\n")

        cap = cv2.VideoCapture(0)
        ##default is 640x480
        w, h = (1280, 720)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
        cap.read()
        ret, img = cap.read()
        cap.release()

        n_top = inception_predict.predict_from_array(img, inception_predict.mod, inception_predict.synsets)
        #print(n_top)
        #n_top_str = "\n".join([str(cls) for cls in n_top])
        #font = cv2.FONT_HERSHEY_TRIPLEX
        #cv2.putText(img, n_top_str, (10, 500), font, 1, (0, 0, 0), 1, False)
        cv2.imshow("camera", img)
        key = 0xFF & cv2.waitKey(10)

        if cmd == 's':
            filename = "frames_%s.jpg" % num
            cv2.imwrite(filename, img)
            num += 1
        if cmd == 'q':
            break

    cv2.destroyAllWindows()
