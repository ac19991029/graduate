from math import radians, cos, sin, sqrt, asin
from decimal import *

with open(r'C:\Users\阿超\Desktop\Latitude and longitude.txt') as f:
    line = f.read()
    # print(type(line))
    # print(line.strip().split(" "))
    line1 = line.strip().split(" ")  # type:list
    numbers = list(map(float, line1))
    print(numbers)
    radian = list(map(radians, numbers))
    print(radian)
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
    print(result)
    # 0.5543939325646355
    # 0.3388509175228877
    # 0.338850908768191
    # 0.2905761713736967
    # 0.5543939279918783
    # 0.5543939232004652
    # 0.6232016870716797
    # 0.6232016656509901
    # 0.5451826793689829
    # 4.423045813513407
    # c=str(Decimal(radian).quantize(Decimal('0.0000000000')))
