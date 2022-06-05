import serial
import pynmea2
import datetime
import time
from datetime import timedelta


ser=serial.Serial("/dev/ttyAMA1",9600)
while True:
    line=str(str(ser.readline()))
    
    if line.startswith("b\'$GNRMC"):
        line=line.replace('\\r\\n\'','')
        print(line)
        msg=pynmea2.parse(line.split("'")[1])
        longitude=msg.longitude
        latitude=msg.latitude
        msg.lat_dir
        msg.lon_dir
        time=msg.datetime
        UTC_time=time
        BJ_time=time+timedelta(hours=8)
        with open(r'parse.txt','a+')as f:
            f.write(line+'\n')
            f.write(str('UTC_time:%s'%UTC_time)+'\n')
            f.write(str('BJ_time:%s'%BJ_time)+'\n')
            f.write(str({'纬度':[latitude,msg.lat_dir],
                           '经度':[longitude,msg.lon_dir]})+'\n')
#         with open(r'Latitude and longitude.txt','a+')as f:
#             f.write(str(longitude))
#             f.write(' ')
#             f.write(str(latitude))
#             f.write(' ')
#         with open(r'time.txt','a+')as f:
#             f.write(str(BJ_time))
#             f.write(' ')


