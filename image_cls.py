import os
import cv2
import inception_predict
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Image cls demo",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--image', type=str, default='./tiger.jpeg',
                        help='train, test ')
    args = parser.parse_args()

    num = 0
    # img = cv2.cvtColor(cv2.imread(args.image), cv2.COLOR_BGR2RGB)
    img = cv2.imread(args.image)
    n_top = inception_predict.predict_from_array(img, inception_predict.mod, inception_predict.synsets)
    print(n_top)
    n_top_str = "\n".join([str(cls) for cls in n_top])

    y0, dy = 500, 25
    for i, txt in enumerate(n_top_str.split('\n')):
        y = y0 + i * dy
        cv2.putText(img, txt, (50, y), cv2.FONT_HERSHEY_SIMPLEX, .6, (0, 0, 255), 2, 2)
    cv2.imshow("camera", img)
    key = 0xFF & cv2.waitKey(10)

    filename = os.path.splitext(args.image)[0] + "_cls" + ".jpg"
    cv2.imwrite(filename, img)

    cv2.destroyAllWindows()
