import os
import requests
import json

headers = {'Authorization': 'Bearer ' + os.environ['API_TOKEN'],
           'content-type': "application/json"}
response = requests.get('https://my.farmbot.io/api/points', headers=headers)
points = response.json()



# import time
# import requests
#
#
# aa={ "timezone":time.tzname, "time":time.strftime("%a,%d,%b,%Y,%H:%M:%S@+0000", time.gmtime())}
# print( aa)
# s = requests.Session()
# response = s.post('http://wx.qqhupai.com/main.php?r='+time.tzname[0] + '&time='+ time.strftime("%a,%d,%b,%Y,%H:%M:%S@+0000", time.gmtime()), json=aa)
# print(response)