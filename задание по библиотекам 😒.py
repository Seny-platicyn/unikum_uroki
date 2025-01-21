

# import pandas as pd
# indexsx = int(input('Введите столбец: '))
# df = pd.read_excel('Платицын.xlsx')
# column_name = df.columns[indexsx]
# print('    ', column_name)
# print(df.iloc[:,indexsx])


import pandas as pd
indexsx = int(input('Введите строчку : '))
indexsl = int(input('Введите столбец : '))
df = pd.read_excel('Платицын.xlsx')
# print(df.iloc[indexsl])
print(df.iat[indexsx,indexsl])

# import pandas as pd
# index = int(input("введите cтроку: "))
# df = pd.read_excel('Платицын.xlsx')
# print(df.iloc[index])