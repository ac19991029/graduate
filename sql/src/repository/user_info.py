#操作用户信息的表的类
from unittest import result
from src.utils.db_connection import DbConnection

class UserInfoRepository:
    def __init__(self) -> None:
        self.db_conn=DbConnection()


    def add(self,**kwargs):
        #新增用户
        #param kwargs
        cursor=self.db_conn.connect()
        sql = """ insert into user_info(%s) values(%s)"""
        key_list = []
        value_list = []
        for k, v in kwargs.items():
            key_list.append(k)
            value_list.append('%%(%s)s' % k)
        sql = sql % (','.join(key_list), ','.join(value_list))
        cursor.execute(sql, kwargs)
        self.db_conn.close()


    def dele(self,name):
        #根据用户名删除用户
        #param name
        cursor=self.db_conn.connect()
        sql="delete from user_info WHERE isername=%s"
        cursor.execute(sql,name)
        self.db_conn.close()


    def fetch_by_user_pwd(self,username,password):
        #根据用户名密码获取找好信息，角色类型
        #param username:
        #param passwprd:

        cursor=self.db_conn.connect()
        sql="""
            select
                user_info.nid as nid,
                user_info.username as username,
                user_info.user_type_id as user_type_id,
                user_type.caption as user_type_caption
            from
                user_info
            left join user_type on user_info.user_type_id=user_type.nid
            where
                user_info.username=%s and user_info.passwd=%s
        """
        cursor.execute(sql,[username,password,])
        result=cursor.fetchone()
        self.db_conn.close()
        return result


    def fetch_by_user(self,username):

        cursor=self.db_conn.connect()
        sql="""
        select
            user_info.nis as nid,
            user_indo.username as username,
            user_info.user_type_id as user_type_id,
            user_type.caption as user_type_caption
        from
            user_info
        left join user_type on user_info.user_type_id=user_type.nid
        where
            user_info.username=%s
        """
        cursor.execute(sql,username)
        result=cursor.fetchone()
        self.db_conn.close()
        return result


    def exist(self,username):
        #根据用户名判断用户是否存在
        sql="select 1 from user_info where username=%s"
        cursor=self.db_conn.connect()
        cursor.execute(sql,[username,])
        result=cursor.fetchone()
        self.db_conn.close()
        return result