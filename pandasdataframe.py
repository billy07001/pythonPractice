import pandas as pd

# 將csv檔案轉換成dataframe
df = pd.read_csv('stock_info.csv', encoding='utf-8')

# 輸入資料概況
print(df.info())
print(df.describe())

# 輸出頭尾資料
print(df.head(3))
print(df.tail(5))
