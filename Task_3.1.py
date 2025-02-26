# Zadanie 1
my_shopping_list = {
    "piekarnia": ['chleb', 'pączek', 'bułki'],
    "warzywniak": ['marchew', 'seler', 'rukola'],
    "meblowy": ['biurko', 'sofa', 'komoda']
}

count_values = sum(len(value) for value in my_shopping_list.values())

for key, values in my_shopping_list.items():
    result = f"Idę do {key.capitalize()}, kupuję tu następujące rzeczy: {[value.capitalize() for value in values]}"
    print(result)

count_values = sum(len(value) for value in my_shopping_list.values())
summary = f"W sumie kupuję {count_values} produktów."
print(summary)


# Zadanie 2
list_divide5 = []
for i in range(1,101):
    if i % 5 == 0:
        list_divide5.append(i**3)
    else:
        pass
print(list_divide5)