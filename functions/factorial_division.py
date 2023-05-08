def factorial(number):
    for fact in range(1, number):
        number *= fact
    return number


number1 = int(input())
number2 = int(input())
factorial_first = factorial(number1)
factorial_second = factorial(number2)
result = factorial_first / factorial_second
print(f"{result:.2f}")