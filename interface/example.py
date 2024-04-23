import json
import requests
import base64

fileName = "文件路径"
callback_url =  "结果回调url"
token_id = "用户token"
file = open(fileName, 'rb')
file_content = file.read()
file.close()
ext = fileName.split('.')[-1]
data_base64=base64.b64encode(file_content).decode('ascii')
r = requests.post( "http://www.api.bgd.faship.cn:8000/api/parse_async", 
timeout=5,
json={'document':data_base64, 
'ext':ext, 
'token_id': token_id,
'callback_url':callback_url  } )
result = r.text.encode('utf-8', 'ignore')
result = json.loads(result)
