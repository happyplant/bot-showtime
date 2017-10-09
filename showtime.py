#!/usr/bin/env python
'''Take a photo.
Take a photo using a USB or Raspberry Pi camera.
'''
#
import os
# import time
# import requests
#
#
# aa={ "timezone":time.tzname, "time":time.strftime("%a,%d,%b,%Y,%H:%M:%S@+0000", time.gmtime())}
# print( aa)
# s = requests.Session()
# response = s.post('http://wx.qqhupai.com/main.php?r='+time.tzname[0] + '&time='+ time.strftime("%a,%d,%b,%Y,%H:%M:%S@+0000", time.gmtime()), json=aa)
# print(response)


if __name__ == '__main__':
    try:
        CAMERA = os.environ['camera']
    except (KeyError, ValueError):
        CAMERA = 'USB'  # default camera
    print(CAMERA)