# coding=gbk
import urllib
from urllib import unquote
import codecs
#import re
import os
#def ASCII2Str(o):
    
f = codecs.open('00_list.txt','r','UTF-8')
s = f.read()
f.close()

parts = s.split('<tr>')
i=1
for part in parts:
    #if part[0:6]=='<td><a':
    b = part.find('src="//upload.wikimedia.org/')+7
    t = 'jpeg'
    e = part.find('jpeg',b)
    if e==-1:
        e = part.find('jpg',b)
        t = 'jpg'
    if e==-1:
        e = part.find('JPG',b)
        t = 'JPG'
    if e==-1:
        e = part.find('png',b)
        t = 'png'
    if e==-1:
        continue
    e = e+len(t)
    fileurl = part[b:e]
    fileurl = fileurl.replace('thumb/','')
    #fn=fileurl.rfind('/')
    #print fn
    fnASCII = fileurl[fileurl.rfind('/')+1:len(fileurl)]
    fn = unquote(fnASCII)
    #print(fn)
    fileurl = 'http://'+fileurl+'?download'
    if os.path.exists(fn):
        print('find file: '+fn)
        if fnASCII <> fn:
            if os.path.exists(fnASCII):
                #delete file
                print(str(i)+' delete file: '+fnASCII)
                try:
                    os.remove(fnASCII)
                except Exception as e:
                    print e
    elif os.path.exists(fnASCII):
        #change file name
        print(str(i)+' rename file "'+fnASCII+'" to "'+fn+'"')
        try:
            os.rename(fnASCII,fn)
        except Exception as e:
            print e
    else:
        print(str(i)+' download file: '+fileurl)
        try:
            urllib.urlretrieve(fileurl, fn)
        except Exception as e:
            urllib.urlretrieve(fileurl, fnASCII)
    i=i+1
    
        #print(b,e)
    #subparts = part.split(',')
    #for subpart in subparts:
    #    subsubparts = subpart.split('":')        
    #    pn=subsubparts[0].replace('"','')
    #    pv=subsubparts[1].replace('"','')
    #    #print(pn, pv)
    #    if pn == 'downLoadUrl':
    #        url = pv
    #        print(pn, pv)
    #    if pn == 'albumName':
    #        album = pv
    #        if not os.path.exists(album):
    #            os.makedirs(album)
    #    if pn == 'title':
    #        fn = album+'/'+pv+'.m4a'
    #        if os.path.exists(fn):
    #            break
    #        else:
    #            print(pn, fn)
    #            urllib.request.urlretrieve(url, fn)
    #            break
            
            
