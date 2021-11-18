import cv2
import logger as f

def gray(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    f.filter_log("grayscale")
    return img_gray





#image = cv2.imread("Data/imgs/img_test.png")
#kernel = cv2.numpy.ones((5, 5), 'uint8')
#dst = cv2.GaussianBlur(gray,(35,35),cv2.BORDER_DEFAULT)
#dilate_img = cv2.dilate(image, kernel, iterations=1)
#cv2.imshow('Gray image', gray)
#cv2.imwrite('output/Test_gray.jpg', gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
