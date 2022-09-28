import threading

#创建全局threadlocal对象
local_school=threading.local()

def process_student():
    #获取当前线程关联的student
    std=local_school.student
    print('hello,%s(in%s)'%(std,threading.current_thread().name))

def process_thread(name):
    #绑定threadlocal的student
    local_school.student=name
    process_student()

t1=threading.Thread(target=process_thread,args=('alice',),name='thread-a')
t2=threading.Thread(target=process_thread,args=('bob',),name='thread-b')
t1.start()
t2.start()
t1.join()
t2.join()