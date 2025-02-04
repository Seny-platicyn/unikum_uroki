import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 7 * np.pi, 200)


y = np.sin(x)


plt.plot(x, y)


plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('График функции y = sin(x) от 0 до 2π')


plt.grid(True)


plt.show()