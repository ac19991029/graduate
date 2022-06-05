import serial
import pynmea2
import time
import datetime
from datetime import timedelta
import json
import paho.mqtt.client as mqtt
import struct
from math import radians, cos, sin, sqrt, asin

ser=serial.Serial("/dev/ttyAMA1",9600)
BrokerHost = '183.230.40.39'  # OneNET使用TCP方式连接时的主机地址
BrokerPort = 6002  # OneNET使用TCP方式连接时的主机端口号

DeviceId = '920319674'  # 设备ID
ProductId = '501534'  # 产品ID
APIKey = "5E=bfg5gVRKkjPKwIlA0t66EIcs="  # 可以是设备单独的APIKey，也可以是产品的MasterAPIKey


# 转换Json格式1为字符串数组
def convert_json_format1(_body):
    packet_type = 0x01
    packet = bytearray()
    packet.extend(struct.pack("!B", packet_type))  # 首先填充数据点类型值
    packet_content = json.dumps(_body)  # 将Json格式数据转换为字符串
    if isinstance(packet_content, str):
        packet_content = packet_content.encode('utf-8')
        packet_content_length = len(packet_content)
        # 填充json字符串长度和json字符串
        packet.extend(struct.pack("!H" + str(packet_content_length) + "s", packet_content_length, packet_content))
    return packet


def get_distance():
    with open(r'Latitude and longitude.txt','a+') as f:
        line = f.read()
        # print(type(line))
        # print(line.strip().split(" "))
#         line1 = line.split(" ")  # type:list
        line1=''.join(line)
        numbers = list(map(float,line1))
#         print(numbers)
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
    
    
def speed():
    distance=get_distance()
    speed=distance/3
    return speed

def warning():
    if speed()<=0.15:
        return 1
    else:
        return 0
# def time_sums():
#     with open(r'time.txt','a+') as f:
#         line = f.read()
#         line1 = line.strip().split(' ')
#         i = 0
#         time_sum = 0
#         while i < len(line1) - 2:
#             start_time1 = line1[i] + ' ' + line1[i + 1]
#             end_time1 = line1[i + 2] + ' ' + line1[i + 3]
#             start_time = datetime.strptime(start_time1, "%Y-%m-%d %H:%M:%S.%f")
#             end_time = datetime.strptime(end_time1, "%Y-%m-%d %H:%M:%S.%f")
#             time_diff = (end_time - start_time).seconds
#             time_sum += time_diff
#             i += 4
#         return time_sum // 10 ** 5

# 连接结果
def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print("连接失败:" + mqtt.connack_string(rc))
        return
    print("连接成功")
    # 上传测试数据
#     with open(r"C:\Users\阿超\Desktop\GPS_in.txt") as f:
#         line = f.read()
#         line1 = line.strip().split("\n")
#         str = ' '.join(line1)
#         line2 = str.split(' ')
#         i = 0
#         while i <= len(line2) - 1:
    test_data = {
        'datastreams': [
            {
                'id': 'location',
                'datapoints': [
                    {
                        "value": {
                            "Car_id":"蒙AS0000",
                            "latitude": latitude,
                            "longitude": longitude,
                        }
                    }
                ]
            },
            {
                'id':'get_speed',
                'datapoints':[
                    {
                        "value":{
                            "content":"current_speed",
                            "speed":speed(),
                        }
                    }
                ]
            },
            {
                'id': 'warning',
                'datapoints': [
                    {
                        "value": {
                            "拥堵":warning(),
                        }
                    }
                ]
            }
            ]
        }
    payload = convert_json_format1(test_data)
    client.publish("$dp", payload, qos=0)

# 从服务器接收发布消息时的回调。
def on_message(client, userdata, msg):
    print("***** 接收到消息 *****")
    print(msg.topic + ":" + msg.payload.decode("utf-8"))


# 当broker响应订阅请求时被调用
def on_subscribe(client, userdata, mid, granted_qos):
    print("***** Broker响应订阅请求*****")
    print(granted_qos)


# 消息发送回调
def on_publish(client, userdata, mid):
    print("[on_publish] mid:" + str(mid))


def main():
    mqtt_broker_host = BrokerHost
    mqtt_broker_port = BrokerPort
    mqtt_user_name = ProductId
    mqtt_password = APIKey
    mqtt_client_id = DeviceId
    client = mqtt.Client(client_id=mqtt_client_id, protocol=mqtt.MQTTv311)
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.username_pw_set(username=mqtt_user_name, password=mqtt_password)
    client.connect(host=mqtt_broker_host, port=mqtt_broker_port, keepalive=60)
    client.loop_start()
    client.loop_stop()

while True:
    line=str(str(ser.readline()))
    
    if line.startswith("b\'$GNRMC"):
        line=line.replace('\\r\\n\'','')
        print(line)
        msg=pynmea2.parse(line.split("'")[1])
        longitude=msg.longitude
        latitude=msg.latitude
        datetime=msg.datetime
        with open(r'Latitude and longitude.txt','a+')as f:
            f.write(str(longitude))
            f.write(' ')
            f.write(str(latitude))
            f.write(' ')
#         with open(r'time.txt','a+')as f:
#             f.write(str(datetime))
#             f.write(' ')
        main()
        print(speed())
        time.sleep(3)
        
        