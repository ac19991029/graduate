from datetime import datetime
from math import radians, cos, sin, sqrt, asin
import self as self


class get_speed:

    def __init__(self):
        print()
    def get_distance(self,lon1, lat1, lon2, lat2):
        # 将十进制的经纬度转化为弧度
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # haversine
        r = 9371  # 地球半径km
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        x = sin(dlat / 2) ** 2 + cos(lat2) * cos(lat1) * sin(dlon / 2) ** 2
        d = 2 * r * asin(sqrt(x))
        return d * 1000  # m

    def time(self,start_time, end_time):
        start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S.%f")
        end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S.%f")
        x = (end_time - start_time).microseconds
        return x


d=get_speed.get_distance(self,35.570418333333336, 111.66612166666667, 35.57042, 111.66612)
t=get_speed.time(self,'2022-03-31 14:22:32.484000', '2022-03-31 14:22:32.884000')//1000
print(d)
speed=d/(t/1000)
print(speed)
