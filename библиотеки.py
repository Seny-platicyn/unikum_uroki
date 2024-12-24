import pandas as pd
indexsx = int(input('Введите индекс: '))
df = pd.read_excel('Платицын.xlsx')
print(df.loc[indexsx])