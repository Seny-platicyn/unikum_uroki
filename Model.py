from Controller import *
from View import *
def addition(num):
    result =sum(num)
    return result


def multi(num):
    result = 1
    for numbers in num:
        result *= numbers
    return result


def divide(num):
    result = num[0]
    for numbers in num[1:]:
        if numbers == 0:
            raise ValueError("делить на ноль нельзя")
        result /= numbers
        return result


def subtract(num):
    result = num[0]
    for numbers in num[1:]:
        result -= numbers
    return result
