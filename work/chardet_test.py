import  chardet

#对bytes进行检测
print(chardet.detect(b'hello,world!'))

#对GBK编码检测
data = '湘江北去，橘子洲头'.encode('gbk')
result=chardet.detect(data)
print(result)
#对UTF-8检测
data1 = '湘江北去，橘子洲头'.encode('utf-8')
print(chardet.detect(data1))

#对日文检测
data2 = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data2))

