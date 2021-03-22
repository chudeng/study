import pandas as pd
from sklearn.datasets import load_iris
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

csv = load_iris()
csv_data = csv['data']
csv_label = csv['target']   # Label

for i in len(csv):
    print(csv_data[i],'\t\t', csv_label[i])
    i += 1

# 학습 전용 데이터와 테스트 전용 테이터로 나누기
train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)

# 데이터 학습 시키고 예측하기
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

# 정답률 구하기
ac_score = metrics.accuracy_score(test_label, pre)
print("정답률: ", ac_score)