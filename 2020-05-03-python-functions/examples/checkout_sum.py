shop_catalog = {'toilet paper': 10,
           'banana': 0.8,
           'coffee beans': 3}

def checkout(shop_list, catalog=shop_catalog):
    """This function calculate how much a customer need to pay.

    Parameters
    ==========
    shop_list, list
    catalog, dict

    Returs
    ======
    checkout_sum, float"""
    checkout_sum = sum([catalog[item] for item in shop_list])
    print(f"Thank you, the total is £{checkout_sum}")
    return checkout_sum

my_shop_list = ['toilet paper', 'banana']
to_pay = checkout(my_shop_list)
print(f"I have to pay {to_pay}")

your_shop_list = ['banana', 'coffee beans']
you_have_to_pay = checkout(your_shop_list, shop_catalog)
print(f"You have to pay {you_have_to_pay}")
