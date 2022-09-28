import psutil

# data=psutil.cpu_count()#cpu逻辑数量
# print(data)
# data2=psutil.cpu_count(logical=False)#cpu物理核心 2说明是双核超线程，4是3核非超线程
# print(data2)
#
# #统计cpu的用户/系统/空闲时间
# data3=psutil.cpu_times()
# print(data3)
#
# #每一秒刷新一次cpu使用率累计10次
# for x in range(10):
#     print(psutil.cpu_percent(interval=1,percpu=True))
#
# #获取物理内存
# data4=psutil.virtual_memory()
# print(data4)
# #获取交换内存信息
# data5=psutil.swap_memory()
# print(data5)
# data6=psutil.disk_partitions()#磁盘分区信息
# print(data6)
# data7=psutil.disk_usage('/')#磁盘使用情况
# print(data7)
# data8=psutil.disk_io_counters()#磁盘IO
# print(data8)

# #获取网络信息
# data9=psutil.net_io_counters()#获取网络读写字节/包的个数
# print(data9)

# data10=psutil.net_if_addrs()#获取网络接口信息
# print(data10)
# data11=psutil.net_if_stats()#获取网络接口状态
# print(data11)

# data12=psutil.net_connections()#获取当前网络连接信息
# print(data12)

#获取进程信息
data13=psutil.pids()#所有进程ID
print(data13)

data14=psutil.Process(1008)
print(data14.name())#进程名字
print(data14.exe())#进程路径
# print(data14.cwd())#进程工作目录
print(data14.ppid())#父进程
print(data14.parent())#子进程列表
print(data14.status())#进程状态
# print(data14.username())#进程用户名
print(data14.create_time())#进程创建时间

#模拟linux中ps功能
ccc=psutil.test()
print(ccc)
