import json

# data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

with open(r'C:\Users\阿超\Desktop\js.txt')as f:
    data=f.read()
    data2=data.split(" ")
    print(len(data2))
    i=0
    while i < len(data2):
        data3=json.dumps({'latitude':int(data2[i]),'longitude':int(data2[i+1])},sort_keys=True,indent=4,separators=('.',': '))
        print(data3)
        i+=2

# data2 = json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': '))