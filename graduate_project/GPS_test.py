
from datetime import timedelta
import pynmea2

line = b'$GNRMC,074230.899,A,3535.7557,N,11141.8679,E,2.72,21.59,210322,,,A*46'
print(type(line))
c=line.decode('utf-8')
print(c)
# print(type(c))
msg=pynmea2.parse(c)
print(msg.latitude)
print(msg.longitude)
# print(msg.data)
time=msg.datetime
UTC_time=time
print(type(UTC_time))
BJ_time=(time+timedelta(hours=8))
# print("UTC_time:%s"%time)
# print("BJ_time: %s"%(time+timedelta(hours=8)))
# print(msg.lat)
# print(msg.lat_dir)
# print(msg.lon)
# print(msg.lon_dir)
# print({
#          # "时间": msg.datetime,
#          "纬度": [msg.lat, msg.lat_dir],
#          "经度": [msg.lon, msg.lon_dir],
#      })
