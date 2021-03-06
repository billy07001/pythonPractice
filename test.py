# python註解用#

"""
三引號為多行注釋號

"""

import random  # 亂數模塊

title = " Learn Code with Billy "

author = "Billy"

print(title)
print(author)


def test():
    global x
    x = "Billy is handsome"

test()

print(x)
print(random.randrange(1, 10))  # 印出1~9隨機數
print(len(title))  # 印出字串長度
print(title.strip())  # 去除字串開頭 結尾的空白字元
print(title.lower())  # 全轉小寫
print(title.upper())  # 全轉大寫
print(title.replace("Billy", "Billy Lai"))  # 替換字元

a = "Hello, Billy"
b = a.split(",")  # 找到,分割號時分割字串成子字串
print(b)

b = "Billy" in a  # 找出Billy字串是否存在於a字串 找出是否不存在用not in
print(b)

age = 20
c = "My name is {} and I'm {} years old"
print(c.format(author, age))  # 格式化輸出 將括號內參數填至{}

def test2(name = "Billy"):
    print( name +" is genious")

test2()
test2("Pio")