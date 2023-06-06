products = input().split()
search_products = input().split()

product_dict = {}

for x in range(0, len(products), 2):
    product_dict[products[x]] = products[x + 1]

for x in search_products:
    if x in product_dict:
        print(f"We have {product_dict[x]} of {x} left")
    else:
        print(f"Sorry, we don't have {x}")
