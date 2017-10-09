from datetime import datetime
import time
import requests
import json

headers = {'Authorization': 'Bearer ' ,
           'content-type': "application/json"}

naive_dt = datetime.now()

aa={"timezone":time.tzname, "time":time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())}
print( aa)
data = json.dumps(aa)
response = requests.post('https://wx.qqhupai.com/main.php',
                         headers=headers, data=data)
print(response)