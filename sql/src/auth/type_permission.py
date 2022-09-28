from src.repository.user_info import UserInfoRepository
from src.repository.permission import PermissionRepository
from src.repository.user_type import UserTypeRepository
from src.repository.user_type_to_permission import UserTypeToPermissionRepository


def look_per():
    '''
    查看用户目前拥有的所有权限
    :return
    '''

obj_user=UserInfoRepository()
obj_type_per=UserTypeToPermissionRepository()
username=input('请输入需要查看的用户')
userinfo=obj_user.fetch_by_user(username)
type_id=userinfo['user_type_id']
pers=obj_type_per.fetch_permission_by_type_id(type_id)#获取用户所有权限
print("{:>8}{}所有权限信息如下：".format('',username))
for i in pers:
    print('{:>8}{}.'.format('',i['caption']))


def add_per():
    '''为某个用户分配权限'''

    obj_per=PermissionRepository()
    obj_type=UserTypeRepository()
    obj_type_per=UserTypeToPermissionRepository()
    pers=obj_per.fetch_all()#从permission表中获取所有权限列表
    types=obj_type.get_info()#从user_type表中获取所有角色列表
    print("{:>8}目前可以管理的角色信息如下：".format(''))
    for i in types:
        print(i['nid'],i['caption'])
    type_id=input("请输入需要管理的角色id:")
    print("{:>8}目前可以分配的角色信息如下：".format(''))
    for i in pers:
        print(i['nid'],i['caption'])
    per_id=input("请输入需要分配权限的id:")
    obj_type_per.add(user_type_id=type_id,permission_id=per_id)
    print("{:>8}权限分配成功".format(''))