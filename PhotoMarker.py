# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 19:27:55 2017

@author: xiex
"""
from geopy.geocoders import Nominatim
#from geopy.geocoders import GoogleV3
import exifread
from PIL import Image, ImageDraw, ImageFont
import os

#==============================================================================
# geo = {i:tags[i] for i in tags.keys() if i.startswith('GPS')}
# for tag in tags.keys():
#     if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
#         print("Key: %s, value %s" % (tag, tags[tag]))
#==============================================================================
#==============================================================================
# def ratio_to_degress(r):
#     d = float(str(r[0]))
# 
#     m = float(str(r[1]))
#     
#     s0 = str(r[2]).split('/')
#     s = float(s0[0])/float(s0[1])
#     
#     return d + (m / 60.0) + (s / 3600.0)
#==============================================================================
def AddTxtOnImg(root, file, x_offset=16, y_offset=16):
    print(os.path.join(root,file))
    tags = exifread.process_file(open(os.path.join(root,file), 'rb'))
    
    img_time = tags['EXIF DateTimeOriginal']
    img_time = "%s"%img_time
    img_time = img_time[:10]
    
    img_width = int('%s'%tags['EXIF ExifImageWidth'])
    img_length = int('%s'%tags['EXIF ExifImageLength'])
    print(img_width,img_length)
    try:
        img_orientation = '%s'%tags['Image Orientation']
        #print('%s'%tags['Image Orientation'])
    except:
        img_orientation = 'Horizontal (normal)'
        #print("no key named 'Image Orientation'")
        
    print(img_orientation)
    
    '''
    1: 'Horizontal (normal)',
    2: 'Mirrored horizontal',
    3: 'Rotated 180',
    4: 'Mirrored vertical',
    5: 'Mirrored horizontal then rotated 90 CCW',
    6: 'Rotated 90 CW',
    7: 'Mirrored horizontal then rotated 90 CW',
    8: 'Rotated 90 CCW'
    '''
    txt = root[2:]+" "+img_time
    im = Image.open( os.path.join(root,file) )  
    if(img_orientation=='Mirrored horizontal'):
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
    elif(img_orientation=='Rotated 180'):
        pass
    elif(img_orientation=='Mirrored vertical'):
        im = im.transpose(Image.FLIP_TOP_BOTTOM)
    elif(img_orientation=='Mirrored horizontal then rotated 90 CCW'):
        pass
    elif(img_orientation=='Rotated 90 CW'):
        im = im.transpose(Image.ROTATE_270)
        b = img_width
        img_width = img_length
        img_length = b
    elif(img_orientation=='Mirrored horizontal then rotated 90 CW'):
        pass
    elif(img_orientation=='Rotated 90 CCW'):
        im = im.transpose(Image.ROTATE_90)
        b = img_width
        img_width = img_length
        img_length = b
        
    #exif = im.info['exif']
    draw = ImageDraw.Draw(im)  
    #print(im.size())
    font_size = int(img_length/32)
    ttfront = ImageFont.truetype('simsun.ttc', font_size)  
    draw.text((x_offset, img_length-font_size-y_offset), txt, fill=(255,0,0), font=ttfront)  
    file = "txt_"+file
    im.save( os.path.join(root,file))#,'JPEG', exif=exif) 

delete_txt = False
dir="."
for root,dirs,files in os.walk(dir):
    for file in files:
        if delete_txt:
            if file[:3]=='txt':
                targetFile = os.path.join(root,  file)
                if os.path.isfile(targetFile):
                    print('remove file:', os.path.join(root,file))
                    os.remove(targetFile)
        else:
            if file[-2:]!='py' and file[-3:]!='csv':
                #print(os.path.join(root,file))
                AddTxtOnImg(root, file)
            
#==============================================================================
#             tags = exifread.process_file(open(os.path.join(root,file), 'rb'))
#             geo = {i:tags[i] for i in tags.keys() if i.startswith('GPS')}
#             print(len(geo))
#             for tag in tags.keys():
#                 if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
#                     print("Key: %s, value %s" % (tag, tags[tag]))
#==============================================================================
                    
#==============================================================================
#             GPSlatitude = tags['GPS GPSLatitude'].values
#             GPSLongitude = tags['GPS GPSLongitude'].values
#             DateTime = tags['Image DateTime'].values
#             ll = '%.6f, %.6f' % (ratio_to_degress(GPSlatitude),ratio_to_degress(GPSLongitude))
#==============================================================================

            
