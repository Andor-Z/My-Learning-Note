
import matplotlib.pyplot as plt
from numpy.random import randn


fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
plt.plot(randn(50).cumsum(), 'k--')