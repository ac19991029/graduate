def romanToInt(s : str) :
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
           'CD': 400, 'CM': 900}
    result = 0
    length = len(s)
    i = 0
    while i < length - 1:
        result1 = s[i] + s[i + 1]
        if result1 in dic:
            result = result + dic[result1]
            i += 2
        else:
            result = result + dic[s[i]]
            i += 1
    if i < length:
        result = result + dic[s[length - 1]]
    return result
print(romanToInt("MCMXCIV"))
print(romanToInt("LVIII"))
# a=romanToInt()
# print(a('III'))
a=romanToInt('II')
print(a)