# import pandas as pd
# indexsx = int(input('Введите строку: '))
# df = pd.read_excel('Платицын.xlsx')
# print(df.loc[indexsx])

# import pandas as pd
# indexsx = int(input('Введите столбец: '))
# df = pd.read_excel('Платицын.xlsx')
# column_name = df.columns[indexsx]
# print('    ', column_name)
# print(df.iloc[:, indexsx])


import pandas as pd
indexsx = input('Введите имя : ')
indexsl = input('Введите предмет : ')
df = pd.read_excel('Платицын.xlsx')
column_name = df.columns['indexsx', 'indexsl']
df.at[indexsx]
print('    ', column_name)
print(df.at[indexsx])
