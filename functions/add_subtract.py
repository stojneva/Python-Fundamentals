def sum_numbers(num1, num2):
    return num1 + num2


def subtract(num1, num2, num3):
    return sum_numbers(num1, num2) - num3


def add_and_subtract(num1, num2, num3):
    return subtract(num1, num2, num3)


number1 = int(input())
number2 = int(input())
number3 = int(input())
print(add_and_subtract(number1, number2, number3))