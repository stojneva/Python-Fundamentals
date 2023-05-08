def calculations(first, second , operator):
    if operator == "multiply":
        return first * second
    elif operator == "divide":
        return int(first / second)
    elif operator == "add":
        return first + second
    elif operator == "subtract":
        return first - second


operator_num = input()
first_num = int(input())
second_num = int(input())
print(calculations(first_num, second_num, operator_num))