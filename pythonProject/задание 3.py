
a = input('Введите слово: ')
upheaval = []
for i in a:
    if i not in upheaval:
        upheaval.append(i)
print(''.join(upheaval))