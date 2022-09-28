#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse():
    with open(r"C:\Users\阿超\Desktop\parse.txt", "r") as f:
        line = f.readline()
        while line:
            line1 = line.strip('\n').split(' ')
            # pid=0C表示转速
            if line1[3] == "0C":
                data1 = int((line1[4] + line1[5]), 16) / 4
            # pid=0D表示车速
            elif line1[3] == "0D":
                data2 = int(line1[4], 16)
            # pid=05表示发动机冷却液温度
            elif line1[3] == "05":
                data3 = int(line1[4], 16) - 40
            # pid=1f表示汽车启动时长
            elif line1[3] == "1f":
                data4 = int((line1[4] + line1[5]), 16)
            # pid=2F表示剩余油量
            else:
                data5 = round((int(line1[4], 16) * 100 / 255), 2)
            # print(data)
            line = f.readline()
        return data1, data2, data3, data4, data5


var = parse()
print(var)