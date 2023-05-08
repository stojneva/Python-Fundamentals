# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = filter(lambda x: x % 2 != 0, numbers)
# print(list(result))

# def yana():
#     result = 5*5
#     print(result)
# yana()

def receive_grade(grade):
    if 2.00 <= grade <= 2.99:
        return "Fail"
    elif 3.00 <= grade <= 3.49:
        return "Poor"
    elif 3.50 <= grade <= 4.49:
        return "Good"
    elif 4.50 <= grade <= 5.49:
        return "Very Good"
    elif 5.50 <= grade <= 6.00:
        return "Excellent"


result = float(input())
print(receive_grade(result))

