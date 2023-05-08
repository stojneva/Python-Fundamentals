numbers_string = input().split()
# opposite_list = []

# for number in numbers_string:
#     current_num = -int(number)
#     opposite_list.append(current_num)


opposite_list = [-int(number) for number in numbers_string]


print(opposite_list)