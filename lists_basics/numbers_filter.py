number = int(input())

even = []
odd = []
negative = list()
positive = list()

for i in range(number):
    integers = int(input())
    if integers % 2 == 0:
        even.append(integers)
        if integers >= 0:
            positive.append(integers)
        elif integers < 0:
            negative.append(integers)
    else:
        odd.append(integers)
        if integers >= 0:
            positive.append(integers)
        elif integers < 0:
            negative.append(integers)

word = input()

if word == "even":
    print(even)
elif word == "odd":
    print(odd)
elif word == "positive":
    print(positive)
elif word == "negative":
    print(negative)
