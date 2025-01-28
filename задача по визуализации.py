# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Шаг 1: Считываем данные из Excel
# file_path = 'Платицын.xlsx'  # Путь к файлу Excel
# df = pd.read_excel(file_path)
#
# # Проверяем структуру данных
# print(df.head())  # Вывод первых строк для проверки
#
# # Шаг 2: Построение графика
# plt.figure(figsize=(20, 6))  # Размер окна графика
#
# # Используем данные из DataFrame
# plt.plot(df['фрукт'], df['цена'], marker='o', label='Зависимость цены от фрукта')
#
# # Настройка графика
# plt.title('График из Excel')
# plt.xlabel('фрукт')
# plt.ylabel('цена')
# plt.legend()
# plt.grid(True)  # Включить сетку
#
# # Шаг 3: Отображаем график
# plt.show()

