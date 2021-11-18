import cv2
import logger as f

def blur(image, intensity ):
    img_blur = cv2.GaussianBlur(image, ((intensity,intensity)), cv2.BORDER_DEFAULT) # à voir si si cela fonctionne intensity
    f.filter_log("blur")
    return img_blur





#image = cv2.imread("Data/imgs/img_test.png")
#dst = cv2.GaussianBlur(image,(35,35),cv2.BORDER_DEFAULT)
#cv2.imshow('blur image', dst)
#cv2.imwrite('output/test_blur.jpg', dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows()