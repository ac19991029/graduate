# -*- coding:utf-8 -*-
#当前登录用户的权限列表
current_user_permission_list={}


#当前登录用户的基本信息：
#{'nid':,'username;:'root','role_id':1}
current_user_info={}

PY_MYSQL_CONN_DICT={
    "host":'localhost',
    'port':3306,
    "user":'root',
    "passwd":'yourenzai',
    "db":'test',
    "charset":'utf-8'
}


# import pymysql
# # pymysql.connect(**kwargs)
# pymysql.connect(host='localhost',port=3306)
# pymysql.connect(**{'host':'locahost','port': 3306})