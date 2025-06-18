#파이썬 자동화프로그램 예제_빈 값 있는 행 제거
#사용한 엑셀은 임의로 만든 데이터값이다.

import pandas as pd
#파일 불러오기
df = pd.read_excel("C:/Users/user/Downloads/sample_data1.xlsx", engine="openpyxl")
#데이터 확인
print(df.head())
#NaN있는 행 제거
cleaned_df = df.dropna()
#새 데이터 저장
cleaned_df.to_excel("C:/Users/user/Downloads/sample_data1.xlsx", index=False)

