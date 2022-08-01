import cv2
import numpy as  np

img=cv2.imread(r'D:/github/Personal-TestDemo/openCV/testInputData/1.png',1) #读取图片
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #将图片变为灰度图片
gray[gray<0.3*255] = 0
#gray = cv2.blur(gray, (3, 3))
#cv2.imshow("gray",gray)
#cv2.waitKey()

# mask = np.zeros_like(gray)
# mask = cv2.circle(mask, (cv2.CENTER_X, cv2.CENTER_Y), gray.RADIUS, (255, 255, 255), -1)
# mask = mask // 255
# gray = mask * gray


kernel=np.ones((2,2),np.uint8) #进行腐蚀膨胀操作
erosion=cv2.erode(gray,kernel,iterations=1) #膨胀
dilation=cv2.dilate(erosion,kernel,iterations=1) #腐蚀
# thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1) # 自适应阈值
ret, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY) # 阈值处理 二值法
# thresh1 = cv2.GaussianBlur(thresh,(3,3),0)# 高斯滤波
contours,hirearchy=cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)# 找出连通域
#对连通域面积进行比较
cv2.imshow("thresh1",thresh)
cv2.waitKey()

area=[] #建立空数组，放连通域面积
contours1=[]   #建立空数组，放减去最小面积的数
for i in contours:
      # area.append(cv2.contourArea(i))
      # print(area)
     if cv2.contourArea(i)>3:  # 计算面积 去除面积小的 连通域
        contours1.append(i)

## 尝试寻找最大圆形，进行切割
# contour_index = np.concatenate([en for en in contours1],axis=0)
# (x, y), radius = cv2.minEnclosingCircle(contour_index)
# (x, y, radius) = np.int0((x, y, radius))
# img_tmp=np.ones(img.shape,np.uint8)
# cv2.circle(img_tmp, (x, y), radius, (0, 0, 255), 2)
# cv2.imshow('img_tmp',img_tmp)
# cv2.waitKey(0)

print(len(contours1)-1) #计算连通域个数
draw=cv2.drawContours(img,contours1,-1,(0,255,0),1) #描绘连通域
#求连通域重心 以及 在重心坐标点描绘数字
# for i,j in zip(contours1,range(len(contours1))):
#     M = cv2.moments(i)
#     cX=int(M["m10"]/M["m00"])
#     cY=int(M["m01"]/M["m00"])
#     draw=cv2.putText(draw, str(j), (cX, cY), 1,1, (255, 0, 255), 1) #在中心坐标点上描绘数字
draw=cv2.putText(draw, str(len(contours1)), (20, 20), 1,1, (255, 0, 255), 1)
#展示图片
cv2.imshow("draw",draw)
cv2.imshow("thresh1",thresh)
cv2.waitKey()
cv2.destroyWindow()
