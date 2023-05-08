# def positive_integers(numbers):
#     for num in numbers:
#         if num == num[::-1]:
#             print(True)
#         else:
#             print(False)
#
#
# all_numbers = input().split(", ")
# positive_integers(all_numbers)

def positive_integers(numbers):
    result = []
    for num in numbers:
        if num == num[::-1]:
            result.append("True")
        else:
            result.append("False")
    return "\n".join(result)


all_numbers = input().split(", ")
print(positive_integers(all_numbers))