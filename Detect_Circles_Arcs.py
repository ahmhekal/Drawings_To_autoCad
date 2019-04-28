import cv2
import numpy as np



img = cv2.imread('test6.png',0)
#img = cv2.bitwise_not(img)
cv2.imshow("input",img)
img = cv2.medianBlur(img,5)



cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,
            1,100,param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))


for i in circles[0,:1]:

    Find_Right_point = 0
    Find_Left_point = 0
    Find_Up_point = 0
    Find_Down_point = 0

    #Getting The Centre
    x = i[0]
    y = i[1]


    #Getting The Radius
    r = i[2]
    #print(x,y,r)
    h = img[y][x]
    #draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)

    #draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)



    # print(img.shape)  # (y= 784, x= 549)
    for i in range (0,12):
         #print(x,r)
         index = x+r-5+i
         value_1 = img[y+5][index]
         value_2 = img[y-5][index]
         if h != value_1 or h != value_2 :
             Find_Right_point = 1

         index = x - r - 5 + i
         value_1 = img[y+5][index]
         value_2 = img[y-5][index]
         if h != value_1 or h != value_2:
             Find_Left_point = 1

         index = y+r-5+i
         value_1 = img[index][x-5]
         value_2 = img[index][x+5]
         if h != value_1 or h != value_2:
             Find_Down_point = 1

         index = y - r - 5 + i
         value_1 = img[index][x-5]
         value_2 = img[index][x+5]
         if h != value_1 or h != value_2:
             Find_Up_point = 1


    Decision = str(Find_Right_point)+str(Find_Left_point)+str(Find_Up_point)+str(Find_Down_point)
    #print(Decision)
    if Decision == '1011':
        print('right Half Circle')
    elif Decision == '0111':
        print('Left Half Circle')
    elif Decision == '1110':
        print('Up Half circle')
    elif Decision == '1101':
        print('Down Half circle')
    else:
        print('Full circle')





cv2.imshow('detected circles',cimg)
#cv2.imshow('partion',img[x+r-10:x+r][y-2])
cv2.waitKey()


