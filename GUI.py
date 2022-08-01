# !/usr/bin/python
# develop Under Python3.7
# -*- coding: UTF-8 -*-
import datetime
import time
print(datetime.date.today())
date = datetime.date(2024,2,1)
if date.__gt__(datetime.date.today()):
    from tkinter import *
    import tkinter as tk
    from tkinter import filedialog
    import cv2
    import numpy as np

def countfrompicture(picture):
    img=cv2.imread(picture,1) #读取图片
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #将图片变为灰度图片
    gray[gray<0.3*255] = 0

    kernel=np.ones((2,2),np.uint8) #进行腐蚀膨胀操作
    erosion=cv2.erode(gray,kernel,iterations=1) #膨胀
    dilation=cv2.dilate(erosion,kernel,iterations=1) #腐蚀
    ret, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY) # 阈值处理 二值法
    contours,hirearchy=cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)# 找出连通域

    area=[] #建立空数组，放连通域面积
    contours1=[]   #建立空数组，放减去最小面积的数
    for i in contours:
        # area.append(cv2.contourArea(i))
        # print(area)
        if cv2.contourArea(i)>3:  # 计算面积 去除面积小的 连通域
            contours1.append(i)

    print(len(contours1)-1) #计算连通域个数
    draw=cv2.drawContours(img,contours1,-1,(0,255,0),1) #描绘连通域
    draw=cv2.putText(draw, str(len(contours1)), (20, 20), 1,1, (255, 0, 255), 1)
    #展示图片
    cv2.imshow("draw",draw)
    cv2.waitKey()
    cv2.destroyWindow()

def GetInputFile_path():
    global InputFile_path
    InputFile_path = filedialog.askopenfilename()
    print(InputFile_path)
    ChooseInputFile_pathT['text']=':'.join(["所选文件",InputFile_path])
    countfrompicture(InputFile_path)

timetag = time.strftime("%Y-%m-%d.%H.%M.%S", time.localtime())
top = tk.Tk()
top.title('菌落图计数小工具@20220801 Power by @Ben-Air')
top.geometry('800x200')  #初始化窗口大小
InputFile_path=''
path = StringVar()
color_base=['#F0F8FF','#FAEBD7','#00FFFF','#7FFFD4','#F0FFFF','#F5F5DC','#FFE4C4','#000000','#FFEBCD','#0000FF','#8A2BE2','#A52A2A','#DEB887','#5F9EA0','#7FFF00','#D2691E','#FF7F50','#6495ED','#FFF8DC','#DC143C','#00FFFF','#00008B','#008B8B','#B8860B','#A9A9A9','#006400','#BDB76B','#8B008B','#556B2F','#FF8C00','#9932CC','#8B0000','#E9967A','#8FBC8F','#483D8B','#2F4F4F','#00CED1','#9400D3','#FF1493','#00BFFF','#696969','#1E90FF','#B22222','#FFFAF0','#228B22','#FF00FF','#DCDCDC','#F8F8FF','#FFD700','#DAA520','#808080','#008000','#ADFF2F','#F0FFF0','#FF69B4','#CD5C5C','#4B0082','#FFFFF0','#F0E68C','#E6E6FA','#FFF0F5','#7CFC00','#FFFACD','#ADD8E6','#F08080','#E0FFFF','#FAFAD2','#90EE90','#D3D3D3','#FFB6C1','#FFA07A','#20B2AA','#87CEFA','#778899','#B0C4DE','#FFFFE0','#00FF00','#32CD32','#FAF0E6','#FF00FF','#800000','#66CDAA','#0000CD','#BA55D3','#9370DB','#3CB371','#7B68EE','#00FA9A','#48D1CC','#C71585','#191970','#F5FFFA','#FFE4E1','#FFE4B5','#FFDEAD','#000080','#FDF5E6','#808000','#6B8E23','#FFA500','#FF4500','#DA70D6','#EEE8AA','#98FB98','#AFEEEE','#DB7093','#FFEFD5','#FFDAB9','#CD853F','#FFC0CB','#DDA0DD','#B0E0E6','#800080','#FF0000','#BC8F8F','#4169E1','#8B4513','#FA8072','#FAA460','#2E8B57','#FFF5EE','#A0522D','#C0C0C0','#87CEEB','#6A5ACD','#708090','#FFFAFA','#00FF7F','#4682B4','#D2B48C','#008080','#D8BFD8','#FF6347','#40E0D0','#EE82EE','#F5DEB3','#FFFFFF','#F5F5F5','#FFFF00','#9ACD32']


ChooseInputFile = tk.Button(top, text="选择输入文件", command=GetInputFile_path)
ChooseInputFile.pack(side = LEFT,anchor='nw')


ChooseInputFile_pathT=Label(top, text='所选输入文件:')
ChooseInputFile_pathT.pack(side=LEFT)


logo = Label(text='''v20220801: 菌落图计数
''')
logo.pack(side="bottom",anchor="se")
top.mainloop()
