import cv2
import numpy as np 


def cartoonizer(filename,d,k,line_size, blur_value):

    img = cv2.imread(filename)

    org_img= np.copy(img)
  

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray_blur=cv2.medianBlur(gray,blur_value)


    edges=cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)

    img = cv2.imread(filename)
                       
    data=np.float32(img).reshape((-1,3))

    criteria= (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,20,0.001)

    ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center= np.uint8(center)

    result = center[label.flatten()]
    result=result.reshape(img.shape)
        
        
    blurred=cv2.bilateralFilter(result, d, sigmaColor=200, sigmaSpace=200)
    c=cv2.bitwise_and(blurred, blurred, mask=edges)
        
    str= "Cartoonized Image {} {} {} {}".format(d,k,line_size, blur_value)

    cv2.imwrite("images\output\Cartoon.png", c)







