# name1 = input()
# name2 = input()
# sign = input()
#
# print(f"{name1}{sign}{name2}")

# metres = int(input())
# result = metres / 1000
# print(f"{result:.2f}")
centuries = int(input())
years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")