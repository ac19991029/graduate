#操作角色表的类
import imp
from re import S
from unittest import result
from src.utils.db_connection import DbConnection



class UserTypeRepository:
    def __init__(self) -> None:
        self.db_conn=DbConnection


    def add(self,caption):
        #向user_type表中添加角色
        cursor=self.db_conn.connect()
        sql="""
        insert into user_type(caption) values(%s)
        """
        cursor.execute(sql,[caption,])
        self.db_conn.close()


    def del_role(self,role):
        #删除角色
        cursor=self.db_conn.connect()
        sql="delete from user_type WHERE caption=%s"
        cursor.execute(sql,role)
        self.db_conn.close()


    def get_info(self):
    #获取表中所有用户角色类型
        cursor=self.db_conn.connect()
        sql='select * from user_type'
        cursor.execute(sql)
        result=cursor.fetchall()
        self.db_conn.close()
        return result