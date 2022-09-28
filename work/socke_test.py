import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#create connection
s.connect(('www.bing.com.cn',80))

#send data
s.send(b'GET / HTTP/1.1\r\nHost: www.bing.com.cn\r\nConnection: close\r\n\r\n')

#receive data
buffer=[]
while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)

s.close()
header, html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
#将接受的数据写入文件
with open('../bing.html', 'wb') as f:
    f.write(html)