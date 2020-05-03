import copy
import checkout_sum as cs

def combine_the_list(list1, list2):
    combine_list = copy.copy(list1)

    for item in list2:
        if item not in list1:
            combine_list.append(item)

    return combine_list

tom_shopping = ['apple', 'toilet paper', 'magazine', 'banana']
matt_shopping = ['milk', 'banana', 'ice cream', 'toilet paper']

catalog = {'apple': 1.5,
           'toilet paper': 5,
           'magazine': 10,
           'milk': 0.5,
           'banana': 0.4,
           'ice cream': 3}

combine_list = combine_the_list(tom_shopping, matt_shopping)

print(f"The cobined list is {combine_list}")

total_amount = cs.checkout(combine_list, catalog)

print(f"They spend £{total_amount} in total.")
