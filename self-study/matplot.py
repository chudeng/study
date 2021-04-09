import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(0, 4*math.pi, 0.1)
y = np.sin(x)
fig, ax = plt.subplots(1, 3)

ax[0].plot(x,y, label='sin graph')
ax[0].legend()
ax[0].set_title('sin freq')
ax[0].set_xlabel('x anxious')
ax[0].set_ylabel('y anxious')
ax[1].bar(x,y)
ax[2].pie(x,y)
plt.savefig('./mygraph.png')

