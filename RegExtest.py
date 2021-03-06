import re

txt = "Billy is a handsome boy"
x = re.search("^Billy.*boy$", txt)
print(x)

# findall() 返回所有包含匹配項的list
y = re.findall("is", txt)
print(y)

# search() 搜尋字串中的字元
z = re.search("\s", txt) # 搜尋字串中的第一個空白字元
print("The first white-space character is located in position:", z.start())

# split() 返回一個list 在每次匹配時被拆分
s = re.split("\s",txt)
print(s)

# sub() 把所匹配到的結果換成指定的字元
u = re.sub("\s", "87", txt, 2)# 第四個count參數(2)用來控制替換次數
print(u)
