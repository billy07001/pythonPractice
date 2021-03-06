import json

# 一些json
x = '{"name" : "Billy","age" : "20","graduationyear" : "2022"}'
# 解析x
y = json.loads(x)

print(y["age"])

# dictionary
a = {
    "name" : "Billy",
    "age" : "20",
    "graduationyear" : "2022"
}
# 將dictionary轉為json
b = json.dumps(a, indent=4, separators=(". ","= "), sort_keys=True)
# indent定義縮排數  separators定義用什麼符號來分割行數 sort_keys定義是否排序結果(根據鍵)

print(b)