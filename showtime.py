from datetime import datetime
import time
import requests
import json

headers = {'Authorization': 'Bearer ' ,
           'content-type': "application/json"}

naive_dt = datetime.now()

aa={ "timezone":time.tzname, "time":time.strftime("%a,%d,%b,%Y,%H:%M:%S@+0000", time.gmtime())}
print( aa)
s = requests.Session()
data = json.dumps(aa)
response = s.post('http://wx.qqhupai.com/main.php?r='+time.tzname[0] + '&time='+ time.strftime("%a,%d,%b,%Y,%H:%M:%S@+0000", time.gmtime()),  headers=headers, json=aa)
print(response)