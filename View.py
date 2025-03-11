from Model import *
from Controller import *
def get_num():
    while True:
        try:
            num = input("введите числа ЧЕРЕЗ ПРОБЕЛЫ: ")
            number_list = [float(numbers) for numbers in num.split()]
            return number_list
        except ValueError:
            print("я же русским языком написал что вписать!")

def get_oper():
    while True:
        operatorion = input("теперь введём знак операции (+, -, *, /): ")
        if operatorion in ('+', '-', '*', '/'):
            return operatorion
        else:
            print("только те знаки которые я написал!")
