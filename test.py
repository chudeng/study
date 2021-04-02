import pandas as pd

member = ['라이언', '무지', '콘', '프로도', '제이지', '네오', '어피치']
weight = ['30', '25', '5', '20', '25', '15', '20']
age = ['5', '4', '10', '3', '7', '6', '11']

kakao_friends = pd.DataFrame()
kakao_friends['member'] = member
kakao_friends['weight'] = weight
kakao_friends['age'] = age
print(kakao_friends)

for row_index, row in kakao_friends.iterrows():
    print(row_index, row)