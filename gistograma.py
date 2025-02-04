import numpy as np
import matplotlib.pyplot as plt

# Генерация случайных данных из нормального распределения
# mean = 0, std = 1, size = 1000
data = np.random.normal(0, 7, 1000)

# Создание гистограммы
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black')  # bins=30 — количество столбцов

# Добавление подписей
plt.title('Гистограмма случайных данных (нормальное распределение)')
plt.xlabel('Значения')
plt.ylabel('Частота')

# Отображение сетки
plt.grid(True, linestyle='--', alpha=0.7)

# Показ графика
plt.show()