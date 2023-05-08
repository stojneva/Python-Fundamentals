def perfect_function(number):
    sum_num = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum_num += divisor
    if sum_num == number:
        return "We have a perfect number!"
    return "It's not so perfect."


all_numbers = int(input())
print(perfect_function(all_numbers))