import random
import math


#  参数含义
# base_log：经度基准点，
# base_lat：维度基准点，
# radius：距离基准点的半径

def generate_random_gps(base_log=None, base_lat=None, radius=None):
    radius_in_degrees = radius / 111300
    u = float(random.uniform(0.0, 0.5))
    v = float(random.uniform(0.0, 0.5))
    w = radius_in_degrees * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)
    longitude = y + base_log
    latitude = x + base_lat
    # 保留6位小数
    loga = '%.6f' % longitude
    lata = '%.6f' % latitude
    # return loga, lata
    return loga, lata


count = 0
pathIn = r'GPS_out.txt'
while count < 5:
    lon, lat = generate_random_gps(base_log=111.7, base_lat=40.8, radius=1000)
    count += 1
    with open(pathIn, 'a') as f:
        f.write(lon+' ')
        f.write(lat+'\r')
    print(lon, lat)  # 输出经度，纬度
    
    
def remaining():
    result = random.random() * 100
    res = str(round(result, 2))
    return res + '%'


def car_id():
    char0 = '京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽赣粤青藏川宁琼'
    char1 = 'ABCDEFGHJKLMNPQRSTUVWXYZ'  # 车牌号中没有I和O，可自行百度
    char2 = '1234567890'
    len0 = len(char0) - 1
    len1 = len(char1) - 1
    len2 = len(char2) - 1
    code = ''
    index0 = random.randint(1, len0)
    index1 = random.randint(1, len1)
    index2 = random.randint(1, len1)
    code += char0[index0]
    code += char1[index1]
    code += char1[index2]
    for i in range(1, 5):
        index3 = random.randint(1, len2)
        code += char2[index3]
    return code


def can():
    with open(r'can.txt', "r") as f:
        line = f.readline()
        while line:
            line1 = line.strip('\n').split(' ')
            # pid=0C表示转速
            if line1[3] == "0C":
                data1 = int((line1[4] + line1[5]), 16) / 4
            # pid=0D表示车速
            elif line1[3] == "0D":
                data2 = int(line1[4], 16)
            # pid=05表示发动机冷却液温度
            elif line1[3] == "05":
                data3 = int(line1[4], 16) - 40
            # pid=1f表示汽车启动时长
            elif line1[3] == "1f":
                data4 = int((line1[4] + line1[5]), 16)
            # pid=2F表示剩余油量
            else:
                data5 = round((int(line1[4], 16) * 100 / 255), 2)
            # print(data)
            line = f.readline()
        return data1, data2, data3, data4, data5
var = can()