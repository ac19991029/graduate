def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    if needle in haystack:
        x = haystack.find(needle)
        return x
    else:
        return -1
print(strStr('ccc','ll'))
print(strStr('hello','ll'))
print(strStr('ccc',''))