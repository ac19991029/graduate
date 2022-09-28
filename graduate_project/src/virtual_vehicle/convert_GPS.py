# -*- coding: utf-8 -*-
import math
import json

x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 偏心率平方
coordinate = []
lon = []
lat = []
converted_lon = []
converted_lat = []


def wgs84_to_gcj02(lon, lat):
    """
    WGS84转GCJ02(火星坐标系)
    :param lon:WGS84坐标系的经度
    :param lat:WGS84坐标系的纬度
    :return:
    """
    if out_of_china(lon, lat):  # 判断是否在国内
        return [lon, lat]
    dlat = _transformlat(lon - 105.0, lat - 35.0)
    dlon = _transformlon(lon - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlon = (dlon * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglon = lon + dlon
    return [mglon, mglat]


def gcj02_to_bd09(lon, lat):
    """
    火星坐标系(GCJ-02)转百度坐标系(BD-09)
    谷歌、高德——>百度
    :param lon:火星坐标经度
    :param lat:火星坐标纬度
    :return:
    """
    z = math.sqrt(lon * lon + lat * lat) + 0.00002 * math.sin(lat * x_pi)
    theta = math.atan2(lat, lon) + 0.000003 * math.cos(lon * x_pi)
    bd_lon = z * math.cos(theta) + 0.0065
    bd_lat = z * math.sin(theta) + 0.006
    return [bd_lon, bd_lat]


def wgs84_to_bd09(lon, lat):
    lon, lat = wgs84_to_gcj02(lon, lat)
    return gcj02_to_bd09(lon, lat)

def _transformlat(lon, lat):
    ret = -100.0 + 2.0 * lon + 3.0 * lat + 0.2 * lat * lat + \
          0.1 * lon * lat + 0.2 * math.sqrt(math.fabs(lon))
    ret += (20.0 * math.sin(6.0 * lon * pi) + 20.0 *
            math.sin(2.0 * lon * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


def _transformlon(lon, lat):
    ret = 300.0 + lon + 2.0 * lat + 0.1 * lon * lon + \
          0.1 * lon * lat + 0.1 * math.sqrt(math.fabs(lon))
    ret += (20.0 * math.sin(6.0 * lon * pi) + 20.0 *
            math.sin(2.0 * lon * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lon * pi) + 40.0 *
            math.sin(lon / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lon / 12.0 * pi) + 300.0 *
            math.sin(lon / 30.0 * pi)) * 2.0 / 3.0
    return ret


def out_of_china(lon, lat):
    """
    判断是否在国内，不在国内不做偏移
    :param lon:
    :param lat:
    :return:
    """
    return not (lon > 73.66 and lon < 135.05 and lat > 3.86 and lat < 53.55)


pathIn = r'C:\Users\阿超\Desktop\GPS_in.txt'
pathOut = r"C:\Users\阿超\Desktop\GPS_out.txt"
result = []
count = 0
if __name__ == '__main__':
    with open(pathIn, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line1 = line.strip()
            # print(type(line1))
            tmp = line1.split(" ")
            lon.append(float(tmp[0]))
            lat.append(float(tmp[1]))
    try:
        print(len(lon))
        for i in range(len(lon)):
            converted = wgs84_to_bd09(lon[i], lat[i])
            # data=json.dumps({'latitude':float(converted[0]),'longitude':float(converted[1])},sort_keys=True,indent=4,separators=('.',': '))
            with open(pathOut, 'a',) as f:
                # f.write(data+'\n')
                # print(str(converted))
                f.writelines(str(converted)+' ')
                # f.writelines('\n')
                count += 1
            print("第" + str(count) + "条数据写入成功...")
    except Exception as err:
        print(err)