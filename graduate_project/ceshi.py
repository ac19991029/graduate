import random
import math
import paho.mqtt.client as mqtt
import json
import struct

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
    # 这里是想保留6位小数
    loga = '%.6f' % longitude
    lata = '%.6f' % latitude
    # return loga, lata
    return loga,lata


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


# 连接结果
def on_connect(client, userdata, flags, rc):
    global lon, lat
    if rc != 0:
        print("连接失败:" + mqtt.connack_string(rc))
        return
    print("连接成功")
    # 上传测试数据
    # value = random.randint(100,10000)
    count = 0
    while count < 2:
        lon, lat = generate_random_gps(base_log=111.7, base_lat=40.8, radius=1000)
        print(lon, lat)
        test_data = {
            'datastreams': [
                {
                    'id': '测试1',
                    'datapoints': [
                        {
                            "at": ' ',
                            "value": {
                                "lon": lon,
                                "lat": lat
                            }
                        }
                    ]
                }
            ]
        }
        count += 1
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
    client.loop_forever()


if __name__ == "__main__":
    main()

