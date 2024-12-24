try:
    num1 = float(input('Введите число 1: '))
    num2 = float(input('Введите число 2: '))
    case = input('Введите оператор')
    if case == '*':
        print(num1*num2)
    elif case == '/':
        print(num1 / num2)
    elif case == '+':
        print(num1 + num2)
    elif case == '-':
        print(num1 - num2)
    elif case == '**':
        print(num1 * num1)
    elif case == '%':
        print(num1 % num2)
    else:
        print('Ничего не найдено')


    num1 or num2/0
except ZeroDivisionError as e:
    print('Не буду даже пробовать это делить это всё таки python🙄')