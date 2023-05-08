def all_numbers(numbers):
    all_numbers = []

    for num in numbers:
        all_numbers.append(int(num))
    return sorted(all_numbers)


number = input().split()
print(all_numbers(number))

