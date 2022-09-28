from datetime import datetime


def time_sums():

    with open(r'C:\Users\阿超\Desktop\time.txt') as f:
        line=f.read()
        line1=line.strip().split(' ')
        i=0
        time_sum=0
        while i<len(line1)-2:
            start_time1=line1[i]+' '+line1[i+1]
            end_time1=line1[i+2]+' '+line1[i+3]
            start_time=datetime.strptime(start_time1,"%Y-%m-%d %H:%M:%S")
            end_time=datetime.strptime(end_time1,"%Y-%m-%d %H:%M:%S")
            time_diff=(end_time-start_time).seconds
            time_sum+=time_diff
            i += 4
        return time_diff
            # print(type(start_time1))
            # print('1%s:'%start_time)
            # print('2%s:'%end_time)


print(time_sums())