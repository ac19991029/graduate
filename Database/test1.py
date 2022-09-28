import pymysql


conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='yourenzai',
    db='test',
    charset='utf8'
)


cursor=conn.cursor(pymysql.cursors.DictCursor)

# zeng
sql='insert into user_info(user,passwd) values(%s,%s);'
# cursor.executemany(sql,[(),(),()])插入多条记录
rows=cursor.execute(sql,('vvv','789'))
# print(cursor.lastrowid)# 查询当前id到哪
conn.commit()
cursor.close()
conn.close()

# chaxun
rows=cursor.execute('select * from user_info;')
print(cursor.fetchone())
cursor.close()
conn.close()


