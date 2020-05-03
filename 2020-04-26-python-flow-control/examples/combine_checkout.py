import copy

tom_shopping = ['apple', 'toilet paper', 'magazine', 'banana']
matt_shopping = ['milk', 'banana', 'ice cream', 'toilet paper']

catalog = {'apple': 1.5,
           'toilet paper': 5,
           'magazine': 10,
           'milk': 0.5,
           'banana': 0.4,
           'ice cream': 3}

combine_list = copy.copy(tom_shopping)

for item in matt_shopping:
    if item not in tom_shopping:
        combine_list.append(item)

print(f"The cobined list is {combine_list}")

total_amount = 0

for item in combine_list:
    total_amount += catalog[item]

print(f"They spend £{total_amount} in total.")
