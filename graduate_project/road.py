import requests
import re
import json


def get_page(url):
    try:
        response = requests.get(url)
        if response.content:  # 返回成功
            return response
    except requests.ConnectionError as e:
        print('url出错', e.args)


# 获取实时拥堵指数内容
def get_detail(page):
    transformData = json.loads(page.text)
    detail = transformData['data']['detail']
    print('实时拥堵指数数据：')
    for i in detail:
        print(str(i)+'：'+str(detail[i]))


url='https://jiaotong.baidu.com/trafficindex/city/details/?cityCode=176'
# print(type(get_page(url)))
# print(get_page(url).text)
print(get_detail(get_page(url)))