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
pathIn = r'C:\Users\阿超\Desktop\GPS_in.txt'
while count < 5:
    lon, lat = generate_random_gps(base_log=111.7, base_lat=40.8, radius=1000)
    count += 1
    with open(pathIn, 'a') as f:
        f.write(lon+' ')
        f.write(lat+'\r')
    print(lon, lat)  # 输出经度，纬度
