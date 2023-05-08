numbers = input().split()
result = []
count = int(input())
for i in numbers:
    result.append(int(i))
    current_min = min(result)

# result1 = [int(i) for i in numbers]


print(result)