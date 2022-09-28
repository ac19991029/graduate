import random
times = 3
secret = random.randint(1, 10)
print("--------little game--------")
#给guess赋值
guess = 0
print("please guess a number:", end=" ")
while(guess != secret ) and (times > 0):
    temp = input()
    guess = int(temp)
    #每输入一次，次数减一
    times = times-1
    if guess == secret:
        print("congratulate!")
    else:
        if guess > secret:
            print("this number is bigger")
        else:
            print("this number is smaller")
        if times > 0:
            print("please try again")
        else:
            print("you are no chance anymore")
print("game over")