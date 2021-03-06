# -*- coding: utf-8 -*-

from PIL import Image

from pylab import *
from os import walk
import copy

CameraZOOM_path = "./CameraZOOM/"
LightroomCamera_path = "./LightroomCamera/"
OpenCamera_path = "./OpenCamera/"

CameraZOOM_list = []
LightroomCamera_list = []
OpenCamera_list = []
for (dir_path, dirnames, filenames) in walk(CameraZOOM_path):
    CameraZOOM_list.extend(filenames) 

for (dir_path, dirnames, filenames) in walk(LightroomCamera_path):
    LightroomCamera_list.extend(filenames) 

for (dir_path, dirnames, filenames) in walk(OpenCamera_path):
    OpenCamera_list.extend(filenames)

print CameraZOOM_list
print LightroomCamera_list
print OpenCamera_list

im_CameraZOOM = array(Image.open("./CameraZOOM/" + CameraZOOM_list[4]))
im_LightroomCamera = array(Image.open("./LightroomCamera/" + LightroomCamera_list[4]))
im_OpenCamera = array(Image.open("./OpenCamera/" + OpenCamera_list[4]))

r = im_CameraZOOM[:,:,0]

g = im_CameraZOOM[:,:,1]

b = im_CameraZOOM[:,:,2]

figure()

#计算各通道直方图
imhist_r,bins_r = histogram(r,256,normed=True)
imhist_g,bins_g = histogram(g,256,normed=True)
imhist_b,bins_b = histogram(b,256,normed=True)

subplot(331)

hist(r.flatten(),256,color='red')

subplot(332)

hist(g.flatten(),256,color='green')

subplot(333)

hist(b.flatten(),256,color='blue')

#获取通道
r = im_LightroomCamera[:,:,0]

g = im_LightroomCamera[:,:,1]

b = im_LightroomCamera[:,:,2]

imhist_r,bins_r = histogram(r,256,normed=True)
imhist_g,bins_g = histogram(g,256,normed=True)
imhist_b,bins_b = histogram(b,256,normed=True)

subplot(334)

hist(r.flatten(), 256, color='red')

subplot(335)

hist(g.flatten(),256, color='green')

subplot(336)

hist(b.flatten(),256, color='blue')

r = im_OpenCamera[:,:,0]

g = im_OpenCamera[:,:,1]

b = im_OpenCamera[:,:,2]

imhist_r,bins_r = histogram(r,256,normed=True)
imhist_g,bins_g = histogram(g,256,normed=True)
imhist_b,bins_b = histogram(b,256,normed=True)

subplot(337)

hist(r.flatten(), 256, color='red')

subplot(338)

hist(g.flatten(),256, color='green')

subplot(339)

hist(b.flatten(),256, color='blue')


show()
