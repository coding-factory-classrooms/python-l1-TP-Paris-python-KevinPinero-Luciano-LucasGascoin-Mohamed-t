import cv2

def dilate(image, intensity):
    kernel = cv2.numpy.ones((intensity, intensity), 'uint8')
    img_dilate = cv2.dilate(image, kernel, iterations=1)
    return img_dilate







#image = cv2.imread("Data/imgs/img_test.png")
#cv2.imshow('Dilated Image', dilate_img)
#cv2.imwrite('output/test_dilatation.jpg', dilate_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()