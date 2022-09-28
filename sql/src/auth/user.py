from src.repository.user_info import UserInfoRepository
from src.repository.user_type import UserTypeRepository


#实现向user_info表中添加和删除用户
def add_user():
    print('{:>8}请输入一下信息创建用户'.format(''))
    obj_user=UserInfoRepository()
    obj_type=UserTypeRepository()
    types=obj_type.get_info()
    name=input('请输入用户名:')
    passwd=input('请输入密码:')
    print('{:>8}角色列表如下:'.format(''))
    for i in types:
        print(i['nid'],i['caption'])
    typeid=input('请选择角色id:')
    obj_user.add(username=name,passwd=passwd,user_type_id=typeid)
    print('{:>8}成功创建用户'.format(''))



def del_user():
    obj=UserInfoRepository()
    name=input('请输入需要删除的用户名:')
    obj.dele(name)
    print('{:>8}成功删除用户'.format(''))