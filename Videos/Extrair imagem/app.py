import cv2
import os
import shutil

print(cv2.__version__)
nome = input("carregar video: ")
arq_video = nome+".mp4"
dir = nome
os.mkdir(dir)
vidcap = cv2.VideoCapture(arq_video)
success, image = vidcap.read()
count = 0
success = True
while success:
    tag = nome+"_"+str(count)+".jpg"
    # save frame as JPEG file
    cv2.imwrite(tag, image)
    success, image = vidcap.read()
    print('Read a new frame: ', success)
    shutil.move(tag, dir)
    count += 1