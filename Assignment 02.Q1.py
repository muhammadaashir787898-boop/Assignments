products = {
    "Electronics": {"LCD": 1200, "Headphones": 800},
    "Clothes": {"Pent": 50, "Shoes": 100},
    "Grocery": {"Rice": 20, "Lays": 10}
}
max= 0
product = ""

for category_items in products.values():
    for name, p in category_items.items():
        if p > max:
            max = p
            product = name


print(product+" ", max)