# -*- coding: utf-8 -*-
from geopy.geocoders import Nominatim
#from geopy.geocoders import GoogleV3
import exifread

tags = exifread.process_file(open('IMG_20170104_150153R.jpg', 'rb'))
#==============================================================================
# geo = {i:tags[i] for i in tags.keys() if i.startswith('GPS')}
# for tag in tags.keys():
#     if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
#         print("Key: %s, value %s" % (tag, tags[tag]))
#==============================================================================
def ratio_to_degress(r):
    d = float(str(r[0]))

    m = float(str(r[1]))
    
    s0 = str(r[2]).split('/')
    s = float(s0[0])/float(s0[1])
    
    return d + (m / 60.0) + (s / 3600.0)

GPSlatitude = tags['GPS GPSLatitude'].values
GPSLongitude = tags['GPS GPSLongitude'].values
DateTime = tags['Image DateTime'].values

ll = '%.6f, %.6f' % (ratio_to_degress(GPSlatitude),ratio_to_degress(GPSLongitude))
print(ll)

geolocator = Nominatim()
#geolocator = GoogleV3()
location = geolocator.reverse(ll)#, exactly_one=True)
print(location.address)

#print(location)

