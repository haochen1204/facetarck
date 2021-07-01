#coding:utf-8
# made by haochen
import cv2 as cv
import sys
import getopt

def main():

    i=0             # 判断是读取视频还是打开摄像头
    facenum=2       # 判断是识别笑脸还是人脸还是人眼，默认为人脸识别
    minnum=5        # 输入的最少识别次数，该值影响识别率，默认为5
    text=''         # 输入的视频的路径

    if not len(sys.argv[1:]):
        # 如果没有输入参数
        print("请输入参数 -s 视频路径 -d 摄像头 -f 0 人眼 1 微笑 2 人脸 -n 最小识别次数")
    else:
        opts,args = getopt.getopt(sys.argv[1:], "s:df:n:",[])
        
        # 对输入的参数进行判断
        for o,a in opts:
            if o in ("-s"):         
                i=1
                text = a
            elif o in ("-d"):
                i=2
            elif o in ("-f"):
                facenum = int(a)
            elif o in ("-n"):
                minnum=int(a)

        # 通过输入的参数调用人脸识别的函数并播放视频
        track(i,text,facenum,minnum)
    
            

def track(i,text,facenum,minnum):
    
    face=''

    if(i ==1): 
        # 读取视频
        cap = cv.VideoCapture(text)
    elif(i == 2):
        # 开启摄像头
        cap = cv.VideoCapture(0)

    if(facenum == 0): 
        #人眼 - haarcascade_eye.xm
        face = 'haarcascade_eye.xml'
    elif(facenum == 1): 
        # 微笑 - haarcascade_smile.xml
        face =  'haarcascade_smile.xml'
    else: 
        # 人脸 - haarcascade_frontalface_default.xml
        face = 'haarcascade_frontalface_default.xml'

    # 调用熟悉的人脸分类器 识别特征类型,是opencv中的一个人脸检测的级联分类器，
    # 可以使用Harr，也可以使用LBP特征，本次使用的是harr特征分类器。
    # harr特征分类器是基于机器学习且使用大量的正负样本训练得到的分类器。
    face_detect = cv.CascadeClassifier(face)

    while True:
        # 读取视频片段
        flag, frame = cap.read()
        if flag == False:
            # 如果没有读取到则证明视频播放完成，可以退出
            break

        # 灰度处理
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        #cv.imshow('video', gray)  # 测试灰度化效果
        
        # 检查人脸 按照1.5倍放大 周围最小像素默认为5
        # 1、输入的图像
        # 2、每次图像尺寸减小的比例
        # 3、每一个目标至少要被监测到多少次才算是
        face_zone = face_detect.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = minnum)

        # 绘制矩形和圆形检测人脸
        for x, y, w, h in face_zone:
            # 绘制矩形人脸区域 thickness表示线的粗细
            cv.rectangle(frame, pt1 = (x, y), pt2 = (x+w, y+h), color = [0,0,255], thickness=2)
            # 绘制圆形人脸区域 radius表示半径
            cv.circle(frame, center = (x + w//2, y + h//2), radius = w//2, color = [0,255,0], thickness = 2)

        # 显示图片
        cv.imshow('video', frame)
        
        # 设置退出键和展示频率
        if ord('q') == cv.waitKey(25):
            break

    # 释放资源
    cv.destroyAllWindows()
    cap.release()

main()