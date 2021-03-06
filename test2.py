import mymodule as mm
import platform
from mymodule import person1
import datetime # 時間模塊

mm.greeting("Billy")

a = mm.person1["graduationyear"]
print(a)

x = platform.system()
print(x)

y = dir(mm) # dir()函數列出模塊裡所有函數
print(y)

print(person1["name"])

z = datetime.datetime.now()
print(z)
print(z.year) # 返回年分
print(z.strftime("%A")) # 返回星期幾

# 創建日期
date = datetime.datetime(2020, 7, 1)
print(date)

# strftime()方法 將對象格式化成可讀字串
print(date.strftime("%B"))