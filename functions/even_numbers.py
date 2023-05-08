def all_numbers(numbers):
    even_numbers = []

    for num in numbers:
        if int(num) % 2 == 0:
            even_numbers.append(int(num))
    return even_numbers


start_numbers = input().split(" ")
print(all_numbers(start_numbers))


# numbers2 = input().split()
# numbers2 = [int(x) for x in numbers2]
# numbers = list(map(int,numbers2)
#
# result = filter(lambda x: x % 2 == 0, numbers)
# print(list(result))

# def funcion(nums):
#     nums = list(map(int, nums))
#     result = filter(lambda x: int(x) % 2 == 0, nums)
#     return result)
# num = input().split()
# print(funcion(num))


ll = ["1", "2"]

result = list(map(int, ll))

result2 = [int(x) for x in ll]

print(result)

print(result2)

