import json
import requests

APIKEY = 'B0UlUUF3U=zYaIZbc2TkC2lL8FI='  # APIKEY
api_url = 'http://api.heclouds.com/devices/926693077/datapoints'  # api地址
api_headers = {'api-key': APIKEY, 'Content-Length': '10'}


def http_put():
    temperature = 1.4324234
    payload = {'datastreams': [{"id": "ceshi1", "datapoints": [{"value": temperature}]}]}
    print("上传值为: %.3f" % temperature)
    jdata = json.dumps(payload)  # 对数据进行JSON格式化编码
    # 打印json内容
    print(jdata)
    r = requests.post(api_url, headers=api_headers, data=json.dumps(payload))
    return r


resp = http_put()
print("OneNET请求结果:\n %s" % resp)
