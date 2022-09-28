#按照100分制，90以上为A 80-90为B 60-80为C 60以下为D 用户随机输入一个数字 然后给出ABCD
temp =input("please give a number ")
grade = int(temp)
if 80> grade>=60:
    print("this grade is C")
elif 90> grade>=80:
    print("this grade is B")
elif 60> grade>=0:
    print("this grade is D")
elif(grade>=90)and(grade<=100):
    print("this grade is A")
else:
    print("this is wrong number!")



