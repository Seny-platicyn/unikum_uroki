num1 = float(input('введите 1 число:'))
num2 = float(input('введите 2 число:'))
action = input("Выбирете действие(summ, minus, multiply, share): ")
def summ(num_1, num_2):
    return num_1 + num_2

def minus(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def share(num_1, num_2):
    return num_1 / num_2

if action == "summ":
    print(summ(num1, num2))

elif action == 'minus':
    print(minus(num1, num2))

elif action == 'multiply':
    print(multiply(num1, num2))

elif action == 'share':
    print(share(num1, num2))