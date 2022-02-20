import numpy as np
import matplotlib.pyplot as plt

# Параметр t для построения кривой
t = np.linspace(0, 2 * np.pi, 1000)

# Координаты кривой Лиссажу
x = np.sin(3 * t)
y = np.sin(4 * t)

plt.figure(figsize=(8, 8))
plt.plot(x, y)
plt.title('Кривая Лиссажу: sin(3t) vs sin(4t)')
plt.xlabel('sin(3t)')
plt.ylabel('sin(4t)')
plt.axis('equal')
plt.grid(True)
plt.show()
