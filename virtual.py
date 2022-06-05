import paho.mqtt.client as mqtt
import json
import struct
import info

BrokerHost = '183.230.40.39'  # OneNET使用TCP方式连接时的主机地址
BrokerPort = 6002  # OneNET使用TCP方式连接时的主机端口号

DeviceId = '920319674'  # 设备ID
ProductId = '501534'  # 产品ID
APIKey = "5E=bfg5gVRKkjPKwIlA0t66EIcs="  # 可以是设备单独的APIKey，也可以是产品的MasterAPIKey


# 转换Json格式1为字符串数组
def convert_json_format1(_body):
    packet_type = 0x01
    packet = bytearray()  # 初始化数组为0个元素
    packet.extend(struct.pack("!B", packet_type))  # 首先填充数据点类型值 ！表示大端传输，B表示unsigned char
    packet_content = json.dumps(_body)  # 将Json格式数据转换为字符串
    if isinstance(packet_content, str):
        packet_content = packet_content.encode('utf-8')
        packet_content_length = len(packet_content)
        # 填充json字符串长度和json字符串
        packet.extend(struct.pack("!H" + str(packet_content_length) + "s", packet_content_length, packet_content))
    return packet


# 连接结果
def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print("连接失败:" + mqtt.connack_string(rc))
        return
    print("连接成功")
    with open(r'GPS_out.txt','r')as f:
        line=f.readline()
        while line:
            line1=line.strip('\n').split(' ')
            vehicle_data = {
                'datastreams':[
                    {
                        'id':'virtual_v_info',
                        'datapoints':[
                            {
                                'value':{
                                    "carId": info.car_id(),
                                    "remaining": info.remaining(),
                                    "latitude":line1[1],
                                    "longitude":line1[0],
                                }
                            }
                        ]
                    },
                    {
                        'id':'CAN',
                        'datapoints':[
                            {
                                'value':{
                                    "发动机转速": str(info.var[0])+"RPM",
                                    "车速": str(info.var[1])+"km/h",
                                    "发动机冷却液温度": str(info.var[2])+'℃',
                                    "汽车启动时长": str(info.var[3])+'sec',
                                    "剩余油量": str(info.var[4])+'%',
                                }
                            }
                        ]
                    }
                ]
            }
            t_payload=convert_json_format1(vehicle_data)
            client.publish("$dp", t_payload, qos=0)
            line=f.readline()


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
