import pandas as pd

# 建立Series物件，傳入list當作參數
series_1 = pd.Series([2, 1, 7, 3])

print(series_1)
print("------------------------------------------------------")
# 建立Series 物件並設定index索引
grades = pd.Series([60, 27, 72, 53], index=['小郭', '小王', '小華', '小明'])

print(grades)
print("------------------------------------------------------")
# 使用索引取值
print(series_1[0])
print(series_1[1:3])
print(grades['小王'])
print("------------------------------------------------------")
# 建立DataFrame物件
data = {
    'name' : ['王浚亦', '楊子逸', '王彥碩', '賴鴻運'],
    'age' : ['18', '19', '20', '21'],
    'grades' : [60, 60, 60, 100]
}

data2 = {
    'name' : ['王浚亦', '楊子逸', '王彥碩', '賴鴻運'],
    'age' : ['18', '19', '20', '21'],
    'grades' : [60, 60, 60, 100]
}

student_df = pd.DataFrame(data, index=['first', 'second', 'third', 'fourth']) # index參數可自定義索引
student_df2 = pd.DataFrame(data2, index=['first', 'second', 'third', 'fourth'])
print(student_df)

# 列出資料訊息
print(student_df.info()) # 列出欄位資料型別等資訊

print(student_df.describe()) # 列出統計資訊

print(student_df.index) # 列出DataFrame的index
print(student_df.columns) # 列出DataFrame的columns
# 列出頭尾指定的幾筆資料
print(student_df.head(3))
print(student_df.tail(3))

# 刪除欄位
student_df = student_df.drop(['age'], axis=1)
print(student_df)

# 列合併資料
student_fg_3 = pd.concat([student_df, student_df2], ignore_index=True) # ignore_index參數使列的索引重新排列
print(student_fg_3)

# 欄合併資料
student_fg_3 = pd.merge(student_df, student_df2)
print(student_fg_3)

# 輸出資料，將資料轉成檔案
print(student_fg_3.to_csv('student_demo.csv'))