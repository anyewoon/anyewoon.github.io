#날짜별 분류
import pandas as pd

df = pd.read_excel("C:/Users/user/Downloads/sample_data3.xlsx")
df_sorted = df.sort_values("날짜")
sales_date= df.groupby("날짜")["매출"].sum().reset_index()
print(sales_date)