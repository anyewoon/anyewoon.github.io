#부서별 매출 합계 구하기
import pandas as pd

#엑셀 파일 불러오기
df=pd.read_excel("c:/Users/user/Downloads/sample_data2.xlsx")
#부서별 매출 합계 계산
sales= df.groupby("부서")["매출"].sum().reset_index()
print(sales)
sales.to_excel("c:/Users/user/Downloads/부서별_매출_정리.xlsx", index=False)