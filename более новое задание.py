
import pandas as pd
df = pd.read_excel('Платицын.xlsx')
# print(df)
# index = int(input("введите cтроку: "))
# print(df.iloc[index])
# indexsx = int(input('Введите строчку : '))
# indexsl = int(input('Введите столбец : '))
action = input("Выбирете действие(найти строку(1), найти столбик(2), вывести весь датасет(3), вывести ячейку(4)) : ")

if action == "3":
    print(df)

elif action == '1':
    index = int(input("введите cтроку: "))
    print(df.iloc[index])

elif action == '2':
    int(input('Введите столбец: '))
    column_name = df.columns[indexsx]
    print('    ', column_name)
    print(df.iloc[:, indexsx])

elif action == '4':
    indexsx = int(input('Введите строчку : '))
    indexsl = int(input('Введите столбец : '))
    print(df.iloc[indexsl])
    print(df.iat[indexsx,indexsl])