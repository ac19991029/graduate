import pymysql

user = input('user>>:').strip()
passwd = input('password>>:').strip()

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='yourenzai',
    db='test',
    charset='utf8'
)

# 获取游标
cursor = conn.cursor()

# 查询语句
# sql = 'select * from user_info where user=" %s" and passwd="%s"' % (user, passwd)
sql = 'select * from user_info where user=%s and passwd=%s'
rows = cursor.execute(sql,(user,passwd))
cursor.close()
conn.close()

if rows:
    print('登陆成功')
else:
    print('登陆失败')
