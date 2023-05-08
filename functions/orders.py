# numbers = lambda a, b, c: a * b * c
# print(numbers(1,2,3))

def orders(product,quantity):
    if product == "coffee":
        return quantity * 1.50
    elif product == "coke":
        return quantity * 1.40
    elif product == "water":
        return quantity * 1.00
    elif product == "snacks":
        return quantity * 2.00

type_product = input()
type_quantity = int(input())
print(f"{orders(type_product,type_quantity):.2f}")
