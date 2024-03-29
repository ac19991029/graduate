import socket
import threading
import time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#监听端口
s.bind(('127.0.0.1',9999))
s.listen(5)
print('Waiting for connection...')

def tcplink(sock, addr):
    print('Accept new connection form %s:%s...'%addr)
    sock.send(b'welcome')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.deode('utf-8')=='exit':
            break
        sock.send(('hello,%s'% data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('connection from %s:%s closed'%addr)

while True:
    #接受一个新连接
    sock, addr=s.accept()
    #创建新线程来处理Tcp连接
    t=threading.Thread(target=tcplink, args=(sock,addr))
    t.start()
