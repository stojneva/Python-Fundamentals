events = input().split("|")
energy = 100
coins = 100
factory_closed = True
for event in events:
    event_items = event.split("-")
    event_name = event_items[0]
    event_value = int(event_items[1])
    if event_name == "rest":
        current_energy = energy
        energy += event_value
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event_name == "order":
        if energy >= 30:
            energy -= 30
            coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= event_value:
            coins -= event_value
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            factory_closed = False
            break
if factory_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

