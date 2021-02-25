# 패키지 임포트(import)
# 데이터 적재를 위해 필요한 패키지를 임포트(Import)한다.
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation

# 데이터 적재(Load)와 분할
(train_data, train_label), (validation_data, validation_label) = mnist.load_data()

# 적재된 데이터 확인
# 대상 데이터를 적재(Load)하고 학습 데이터와 검증 데이터로 나눈다.
for images in train_data[:2]:
    for image in images:
        for dat in image:
            print('{:3}'.format(dat), end='')
        print()
    print(end="\n\n")

# 데이터 전처리
# 데이터를 신경망 학습 모델이 학습 가능한 형태로 변환하는 과정의 전처리를 진행한다.
# 학습용 정수형 초평면 데이터를 2차원의 실수형 데이터로 변환한다.
train_data = train_data.reshape(train_data.shape[0], 784).astype('float64') / 255
validation_data = validation_data.reshape(validation_data.shape[0], 784).astype('float64') / 255

# 초매개 변수(Hyper Parameter)를 설정
# 학습 모델을 생성하고 학습 모델 I에 레이어(Layer)를 초매개 변숫값과 함께 추가하여 설 정한다.
model = Sequential()
model.add(Dense(128, input_dim=784, activation='relu'))
model.add(Dense(10, activation='softmax'))

# 학습 모델 생성
# 하이퍼 파라미터가 적용된 학습 모델에 손실 함수, 옵티마이저, 메트릭을 적용하여 생성한다.
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 학습 실행
# 앞서 준비한 학습 데이터를 이용하여 모델을 학습시킨다.
model.fit( train_data, train_label, validation_data=(validation_data, validation_label), epochs=10, batch_size=200, verbose=0, callbacks=[cb_checkpoint, cb_early_stopping])

# 검증 데이터 준비
# 검증용 데이터를 One Hot Encoding(문자를 고유의 숫자 인덱스로 표현)을 적용하여 학습 모델 검증에 이용할 수 있도록 준비한다.
train_label = np_utils.to_categorical(train_label, 10)
validation_label = np_utils.to_categorical(validation_label, 10)

# 학습 모델 평가
# 검증 데이터를 이용하여 학습 모델을 평가하고, 평가된 결괏값을 확인한다.
accuracy = model.evaluate(validation_data, validation_label)[1]
print('\nAccuracy: {:.2f}'.format(accuracy))
