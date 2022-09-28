# -*- coding: UTF-8 -*-
from datetime import timedelta
import pynmea2

for line in open(r'C:\Users\阿超\Desktop\text.txt'):
    # line1 = str(str(line)[:])
    # print('line=%s'% line)
    print(line)
    print(line.split('\\r\\n'))
    # print(type(line))
    # print(line.split("'"))
    # print(line.split("'")[1])
    # print(type(line.split("'")[1]))
    msg = pynmea2.parse(line.split("'")[1])
    # print(msg.data[6])
    print(msg.longitude)
    # print(type(msg.longitude))
    # time = msg.datetime
    # print("UTC_time:%s" % time)
    # print("BJ_time: %s" % (time + timedelta(hours=8)))
    # print({
    #     # "时间": msg.datetime,
    #     "纬度": [msg.latitude, msg.lat_dir],
    #     "经度": [msg.longitude, msg.lon_dir],
    # })
    # $GNRMC, 074230.899, A, 3535.7557, N, 11141.8679, E, 2.72, 21.59, 210322,, , A * 46
    # sb=bytes(line,encoding='utf-8')
    # print(type(sb))
    # c=line.encode('utf-8').decode('utf-8')
    # print(type(c))
    # line1=str(line).split(',')
    # c=line1.encode('utf-8').decode('utf-8')
    # print(line1)
    # msg=pynmea2.parse(c)
    # print(msg.data)
