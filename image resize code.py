
import image as Image
import cv2
import os, sys


def resize(original, new):
    counter=0
    for item in original:
        if os.path.isfile(path+item):
            im = cv2.imread(path+item)
            f, e = os.path.splitext(path+item)
            # imResize = im.resize((720,480))
            imResize=cv2.resize(im,(1920,1080))
            # imResize.save(f+'resized.jpg','JPG',quality=90)
            cv2.imwrite(new+''+str(counter)+'_resized.jpg',imResize)
            counter+=1


# path = r"C:/Users/syed/PycharmProjects/hello/original/"
path=r'C:\Users\syed\PycharmProjects\hello\original\test//'
newpath=r'C:\Users\syed\PycharmProjects\hello\resized\\'
dirs = os.listdir(path)
resize(dirs,newpath)