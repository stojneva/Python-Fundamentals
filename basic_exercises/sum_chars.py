number = int(input())
counter = 0

for i in range(number):
    chars = input()
    total_sum = ord(chars)
    counter += total_sum

print(f"The sum equals: {counter}")