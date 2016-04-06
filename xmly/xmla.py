# coding=gbk
import urllib.request
import codecs
#import re
import os

f = codecs.open('b158d32410774379682683568da17d8c','r','UTF-8')
s = f.read()
f.close()
#s='[{"actualAlbumId":0,"albumCoverPath":"http://fdfs.xmcdn.com/group5/M09/4A/32/wKgDtlS4cZeCzmE2AAHjHCQ8i2g083_mobile_small.jpg","albumId":239463,"albumName":"罗辑思维 全集","anchorType":0,"category":0,"comments_counts":0,"coverLarge":"http://fdfs.xmcdn.com/group11/M02/36/33/wKgDa1WVdFCBiI1nAAHjHCQ8i2g167_mobile_large.jpg","coverSmall":"http://fdfs.xmcdn.com/group11/M02/36/33/wKgDa1WVdFCBiI1nAAHjHCQ8i2g167_mobile_small.jpg","create_at":1450381219000,"downLoadUrl":"http://audio.xmcdn.com/group14/M07/CF/01/wKgDZFZzDuXxgvmJAKAKnb3-Nzo489.m4a","downloadId":0,"downloadLocation":"/storage/emulated/0/ting/download","downloadPercent":100,"downloadStatus":4,"downloadType":0,"downloaded":10488477,"duration":3398,"favorites_counts":3613,"filesize":10488477,"history_duration":0,"history_listener":0,"id":10874224,"isPublic":false,"isRelay":false,"isRunning":false,"is_favorited":false,"is_playing":false,"liked":false,"new":false,"nickname":"罗辑思维脱口秀","opType":0,"orderNum":0,"orderPositon":0,"playType":0,"playUrl32":"http://fdfs.xmcdn.com/group14/M07/CF/00/wKgDZFZzDtfiNSwSAM9owBaDcbU725.mp3","playUrl64":"http://fdfs.xmcdn.com/group14/M07/CF/37/wKgDY1ZzDt3S8k0uAZ7Qq8hT7k4825.mp3","playlistType":0,"plays_counts":768317,"processState":0,"programId":0,"programScheduleId":0,"radioId":0,"realAlubmId":239463,"sequnceId":"260bf8a0a2c1401096568dffd6d6d41a","shares_counts":0,"sortKeyword":0,"status":1,"title":"走错路的日本人[罗辑思维]No.152","trackId":10874224,"uid":1412917,"userCoverPath":"http://fdfs.xmcdn.com/group5/M07/4A/35/wKgDtlS4cmeAM8R4AAC2jG7vGBo443_mobile_small.jpg","user_source":0},{"actualAlbumId":0,"albumCoverPath":"http://fdfs.xmcdn.com/group5/M09/1F/56/wKgDtVSoz8LhdYJKAAGif-bG3eY023_mobile_small.jpg","albumId":321701,"albumName":"晓松奇谈 2015","anchorType":0,"category":0,"comments_counts":0,"coverLarge":"http://fdfs.xmcdn.com/group10/M09/36/2B/wKgDaVWVv6zh6sFBAAGif-bG3eY741_mobile_large.jpg","coverSmall":"http://fdfs.xmcdn.com/group10/M09/36/2B/wKgDaVWVv6zh6sFBAAGif-bG3eY741_mobile_small.jpg","create_at":1450982271000,"downLoadUrl":"http://audio.xmcdn.com/group9/M00/D5/6B/wKgDYlZ8O0iAMthcAHoBxFDZ3mw919.m4a","downloadId":0,"downloadLocation":"/storage/emulated/0/ting/download","downloadPercent":100,"downloadStatus":4,"downloadType":0,"downloaded":7995844,"duration":2590,"favorites_counts":58,"filesize":7995844,"history_duration":0,"history_listener":0,"id":11053128,"isPublic":false,"isRelay":false,"isRunning":false,"is_favorited":false,"is_playing":false,"liked":false,"new":false,"nickname":"晓松奇谈","opType":0,"orderNum":0,"orderPositon":0,"playType":0,"playUrl32":"http://fdfs.xmcdn.com/group11/M01/E0/92/wKgDbVZ8OyHwi4n-AJ4eRTJwNoU385.mp3","playUrl64":"http://fdfs.xmcdn.com/group11/M01/E0/93/wKgDbVZ8OynTo7phATw6mN_zBAo393.mp3","playlistType":0,"plays_counts":8977,"processState":0,"programId":0,"programScheduleId":0,"radioId":0,"realAlubmId":321701,"sequnceId":"64f8a43462d148b9a107259f5a623c02","shares_counts":0,"sortKeyword":0,"status":1,"title":"1860年代：维多利亚的秘密","trackId":11053128,"uid":10936615,"userCoverPath":"http://fdfs.xmcdn.com/group4/M05/D7/C8/wKgDtFP62n-gh5HgAAJs3cEsqnM853_mobile_small.jpg","user_source":0}]'
#s='[{"a":0,"b":2},{"a":2,"b":4}]'
#p=re.compile(r'"albumCoverPath":"(^,)"')
#matchObj = p.findall(s)
#print(matchObj)
#for m in matchObj:
#    print(m)
parts = s.split('},{')
for part in parts:
    subparts = part.split(',')
    for subpart in subparts:
        subsubparts = subpart.split('":')        
        pn=subsubparts[0].replace('"','')
        pv=subsubparts[1].replace('"','')
        #print(pn, pv)
        if pn == 'downLoadUrl':
            url = pv
            print(pn, pv)
        if pn == 'albumName':
            album = pv
            if not os.path.exists(album):
                os.makedirs(album)
        if pn == 'title':
            fn = album+'/'+pv+'.m4a'
            if os.path.exists(fn):
                break
            else:
                print(pn, fn)
                urllib.request.urlretrieve(url, fn)
                break
            
            
