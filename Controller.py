from Model import *
from View import *
def calculator():

num = get_num()
operation = get_oper()

try:
    if operation == "+":
        print("Ответ", addition(num))
    elif operation == "-":
        print("Ответ", subtract(num))
    elif operation == "*":
        print("Ответ", multi(num))
    elif operation == "/":
        print("Ответ", divide(num))

except ValueError as e:
    print("Ошибка: {e}")

calculator()