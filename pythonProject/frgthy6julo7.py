text=input()
WTF=[] #wall_table_factory
for i in text:
    if i not in WTF:
        WTF.append(i)
print(''.join(WTF))