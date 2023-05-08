number_of_snowballs = int(input())
weight = 0
time = 0
quality = 0
max_value = 0

for snow in range(number_of_snowballs):
    weight_snowball = int(input())
    time_needed = int(input())
    quality_snowball = int(input())
    value = (weight_snowball / time_needed) ** quality_snowball
    if value > max_value:
        weight = weight_snowball
        time = time_needed
        quality = quality_snowball
        max_value = value
print(f"{weight} : {time} = {int(max_value)} ({quality})")

