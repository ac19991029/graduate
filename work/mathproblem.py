x = 7
i = 0
flag = 0

while i<= 100:
    if(x%2 == 1)and(x%3 ==2)and(x%5 ==4)and(x%6 ==5):
        flag = 1
    else:
        x = 7 *(i+1)
    i +=1

    if flag== 1:
        print("the floor is :",x)
    else:
        print("this is no answer!")

