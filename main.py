import cv2
import inception_predict
import time

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    num = 0
    while True:
        ret, img = cap.read()

        # w, h = (1080, 720)
        # cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
        # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

        cv2.imshow("camera", img)

        key = 0xFF & cv2.waitKey(10)
        inception_predict.predict_from_array(img, inception_predict.mod, inception_predict.synsets)
        time.sleep(5)
        if key == 27:
            break
        if key == ord(' '):
            num = num + 1
            filename = "frames_%s.jpg" % num
            cv2.imwrite(filename, img)
        if num == 30:
            break

    cv2.destroyAllWindows()
