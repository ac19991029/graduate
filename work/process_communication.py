from multiprocessing import  Process,Queue
import os,time,random

#写数据进程执行的代码:
def write(q):
    print('process to write:%s'% os.getpid())
    for value in ['a','b','c']:
        print('put %s to queue...'% value)
        q.put(value)
        time.sleep(random.random())

#读数据进程执行的代码:
def read(q):
    print('process to read:%s'% os.getpid())
    while True:
        value=q.get(True)
        print('get %s from queue.'% value)

if __name__=='__main__':
    #父进程创建queue 并传给各个子进程
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    #启动子进程pw 写入
    pw.start()
    #启动子进程pr 读
    pr.start()
    #等待结束
    pw.join()
    pr.terminate()