import random


def v_fuel_consumption():
    result = random.random() * 100
    res = str(round(result, 2))
    return res + '%'


# print(v_fuel_consumption())


def car_id():
    char0 = '京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽赣粤青藏川宁琼'
    char1 = 'ABCDEFGHJKLMNPQRSTUVWXYZ'  # 车牌号中没有I和O，可自行百度
    char2 = '1234567890'
    len0 = len(char0) - 1
    len1 = len(char1) - 1
    len2 = len(char2) - 1
    code = ''
    index0 = random.randint(1, len0)
    index1 = random.randint(1, len1)
    index2 = random.randint(1, len1)
    code += char0[index0]
    code += char1[index1]
    code += char1[index2]
    for i in range(1, 5):
        index3 = random.randint(1, len2)
        code += char2[index3]
    return code


# print(car_id())


if __name__ == '__main__':
    car_id()
    v_fuel_consumption()
