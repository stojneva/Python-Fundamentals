factor = int(input())
count = int(input())
# list_count = list()
#
# for n in range(1, count + 1):
#     list_count.append(factor * n)

list_count = [factor * n for n in range(1, count + 1)]


print(list_count)