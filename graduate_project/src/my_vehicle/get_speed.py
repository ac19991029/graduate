from datetime import datetime
from math import radians, cos, sin, sqrt, asin
import self as self


class get_speed:

    def __init__(self):
        pass

    # def get_distance(self,lon1, lat1, lon2, lat2):
    #     # 将十进制的经纬度转化为弧度
    #     lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    #     print(lon1,lat1,lon2,lat2)
    #     # haversine
    #     r = 9371  # 地球半径km
    #     dlon = lon2 - lon1
    #     dlat = lat2 - lat1
    #     x = sin(dlat / 2) ** 2 + cos(lat2) * cos(lat1) * sin(dlon / 2) ** 2
    #     d = 2 * r * asin(sqrt(x))
    #     return d*1000   # m
    def get_distance(self):
        with open(r'C:\Users\阿超\Desktop\Latitude and longitude.txt') as f:
            line = f.read()
            # print(type(line))
            # print(line.strip().split(" "))
            line1 = line.strip().split(" ")  # type:list
            numbers = list(map(float, line1))
            print(numbers)
            radian = list(map(radians, numbers))
            # print(radian)
            count = len(radian)
            i = 0
            result = 0
            while i < count - 2:
                dlon = radian[i + 3] - radian[i + 1]
                dlat = radian[i + 2] - radian[i]
                # print(dlon)
                # print(dlat)

                # haversine公式
                r = 9371  # 地球半径km
                x = sin(dlat / 2) ** 2 + cos(radian[i + 2]) * cos(radian[i]) * sin(dlon / 2) ** 2
                d = 2 * r * asin(sqrt(x)) * 1000
                # print(d * 1000)
                result += d
                i += 2
            return result
            # c=str(Decimal(radian).quantize(Decimal('0.0000000000')))

    # def time_sums(self):
    #     with open(r'C:\Users\阿超\Desktop\time.txt') as f:
    #         line = f.read()
    #         line1 = line.strip().split(' ')
    #         i = 0
    #         time_sum = 0
    #         while i < len(line1) - 2:
    #             start_time1 = line1[i] + ' ' + line1[i + 1]
    #             end_time1 = line1[i + 2] + ' ' + line1[i + 3]
    #             start_time = datetime.strptime(start_time1, "%Y-%m-%d %H:%M:%S.%f")
    #             end_time = datetime.strptime(end_time1, "%Y-%m-%d %H:%M:%S.%f")
    #             time_diff = (end_time - start_time).microseconds
    #             time_sum += time_diff
    #             i += 4
    #         return time_sum // 10 ** 5
    # def time(self,start_time, end_time):
    #     start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S.%f")
    #     end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S.%f")
    #     x = (end_time - start_time).microseconds
    #     return x


    # d=get_speed.get_distance(self,35.570418333333336, 111.66612166666667, 35.57042, 111.66612)
    # t=get_speed.time(self,'2022-03-31 14:22:32.484000', '2022-03-31 14:22:32.884000')//1000
    # print(d)
    # speed=d/(t/1000)
    # print(speed)
# def speed():
#     distance=get_speed.get_distance(self)
#     time=get_speed.time_sums(self)
#     speed=distance/time
#     return speed

# distance = get_speed.get_distance(self)
# time=get_speed.time_sums(self)
# print(distance)
# print(time)
# speed = distance/4
# print(speed)
# print('%.2f'%speed)

# print(speed())