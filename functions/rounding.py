def rounding(nums):
    round_list = []

    for numbers in nums:
        round_list.append(round(float(numbers)))

    return round_list


number_round = input().split(" ")
print(rounding(number_round))
