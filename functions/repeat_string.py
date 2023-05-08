# def numbers(repeat_string, times):
#     return repeat_string * times
#
#
# string = input()
# time = int(input())
# print(numbers(string,time))

string = input()
number = int(input())

result = lambda a, b: a * b

end_result = result(string,number)
print(end_result)