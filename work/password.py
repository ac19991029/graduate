count =3
password = 'ccc'

while count:
    passwd=input('please input password:\n')
    if passwd==password:
        print("you are right")
        break
    elif '*' in passwd:
        print("the password is not expose '*',you have",count-1,"chances",end='\n')
        continue
    else:
        print("the password is wrong,you have",count-1,"chances",end='\n')
    count -=1




