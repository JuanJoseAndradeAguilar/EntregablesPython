import matplotlib.pyplot as plt
import numpy as np
a = 0
b = 2.5
c = 0.1

fig = plt.subplots(figsize=(12, 6))

x = np.array([0, 1, 0.5, 2.5])
plt.plot(x, color='black')

plt.xticks(np.arange(a, b+0.1, c))
plt.yticks(np.arange(a, b+0.1, c))

plt.show()