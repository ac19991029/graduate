# _*_ coding: utf-8 _*_
fpath=r'C:\Users\阿超\Desktop\read.txt'#r'代表保持字符原始值
with open(fpath,'r',encoding='utf-8') as f:
    s=f.read()
    print(s)