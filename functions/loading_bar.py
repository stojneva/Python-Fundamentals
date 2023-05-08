def loading_bar(nums):
    if nums == 100:
        return f"100% Complete! \n[%%%%%%%%%%]"

    result = nums // 10
    return f'{nums}% [{result * "%"}{(10 - result) * "."}]\nStill loading...'


numbers = int(input())
print(loading_bar(numbers))