# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:50:24 2017

@author: xiex
"""
import os
import cv2 as cv
import json
from struct import pack
#\images
#   \class1
#       c11.jpg
#       c12.jpg
#       ...
#   \class2
#       c21.jpg
#       c22.jpg
#       ...
#   ...
image_path = "./images"
info_file_path = image_path + "/info.json"
feature_file_path = image_path + "/feature.bin"
label_file_path = image_path + "/label.bin"

w = 256
h = 256
c = 3
number = 0

files = os.listdir(image_path)
categories = {}
categorie_id = 0
images = {}
for f in files:
  sub_folder = image_path + '/' + f  
  if(os.path.isdir(sub_folder)): 
    if(f[0] == '.'):  
      pass  
    else:  
      categories[categorie_id] = f
      for i in os.listdir(sub_folder):
        image = sub_folder + '/' + i
        images[image] = categorie_id
        number += 1
      categorie_id += 1
shape = {'weight':w, 'height':h, 'channel':c, 'number':number}
info = {}
info['shape'] = shape
info['categories'] = categories
#info['images'] = images
info_file = open(info_file_path, 'w')
info_file.write(json.dumps(info, sort_keys=False, indent=2, separators=(',', ': ')))
info_file.close()

feature_file = open(feature_file_path, 'wb')
label_file = open(label_file_path, 'wb')
for (image, label) in images.items():
  label_file.write(pack("i",label))
  img = cv.imread(image)
  img = cv.resize(img,(w,h),interpolation=cv.INTER_CUBIC)
  img = img/256.0
  buf = pack('%sf' % img.size, *img.flatten())
  feature_file.write(buf)
  #print(img)

feature_file.close()
label_file.close()
