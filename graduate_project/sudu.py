from math import radians, cos, sin, sqrt, asin

with open(r'C:\Users\阿超\Desktop\Latitude and longitude.txt') as f:
    line = f.read()
    print(line)
    # print(type(line))
    # print(line.strip().split(" "))
    line1 = line.split(" ")  # type:list
    print(line1)
    numbers = list(map(float, line1))
    print(numbers)
    radian = list(map(radians, numbers))
    # print(radian)
    count = len(radian)
    i = 0
    result = 0
    while i < count - 2:
        dlon = radian[i + 3] - radian[i + 1]
        dlat = radian[i + 2] - radian[i]
        # print(dlon)
        # print(dlat)

        # haversine公式
        r = 9371  # 地球半径km
        x = sin(dlat / 2) ** 2 + cos(radian[i + 2]) * cos(radian[i]) * sin(dlon / 2) ** 2
        d = 2 * r * asin(sqrt(x)) * 1000
        # print(d * 1000)
        result += d
        i += 2