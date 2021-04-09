#https://m.blog.naver.com/okkam76/221919274832
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 1)
x_new = x.reshape(-1,1)
print(x_new)
print(x)
y= 2*x - 1
plt.plot(x, y)

print('x배열의 원소 개수:', x.shape[0])
idx = np.arange(x.shape[0])
print('기존 인덱스:', idx)
np.random.shuffle(idx)
print('셔플 인덱스:', idx)

x = x[idx]
y = y[idx]
print('x=',x, '\n', 'y=', y)


