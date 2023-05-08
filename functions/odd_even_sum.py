def result(number):

    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    for i in number:
        if int(i) % 2 == 0:
            sum_of_even_digits += int(i)
        else:
            sum_of_odd_digits += int(i)
    return sum_of_odd_digits, sum_of_even_digits


number_string = input()
sum_of_even_digits,sum_of_odd_digits = result(number_string)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")