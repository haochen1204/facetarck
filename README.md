# facetarck
基于python opencv的简单人脸、人眼、笑脸识别脚本，可打开摄像头或者导入视频进行识别

参数说明：-s 视频路径 -d 摄像头 -f 0 人眼 1 微笑 2 人脸 -n 最小识别次数
-s或-d必须输入，其他不输入则默认为人脸识别，最小识别次数为5
eg: python a.py -s /shipin/1.mp4 -f 2 -n 5
    python a.py -d -f 2 -n 5
