
a = input('Введите фразу для посчёта гласных: ')
glasnie = 0
alfofit = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
for i in a:
        if i.isalpha():
            if i in alfofit:
                glasnie += 1
print('В вашем предложении',glasnie,'гласных.')
