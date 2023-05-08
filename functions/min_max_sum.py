def min_num(nums):
    result = list(map(int, nums))
    return f"The minimum number is {min(result)}"


def max_num(nums):
    result = list(map(int, nums))
    return f"The maximum number is {max(result)}"


def sum_num(nums):
    result = list(map(int, nums))
    return f"The sum number is: {sum(result)}"


all_num = input().split()
print(min_num(all_num))
print(max_num(all_num))
print(sum_num(all_num))