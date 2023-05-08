class Party:

    def __init__(self):
        self.names = []

    def print_func(self):
        return f"Going: {', '.join(party.names)}\n" + f"Total: {len(party.names)}"


party = Party()

while True:
    name = input()

    if name == "End":
        break
    else:
        party.names.append(name)

print(party.print_func())
