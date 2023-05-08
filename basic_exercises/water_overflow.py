number = int(input())
tank = 255
counter = 0

for i in range(number):
    litres = int(input())
    capacity = tank - litres
    if 0 > capacity:
        print("Insufficient capacity!" )
        continue
    tank = tank - litres
    counter = counter + litres
print(counter)