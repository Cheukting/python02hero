catalog = {'apple': 1.5, 'banana': 0.8, 'toilet paper': 2}
cheuk_shopping = ['banana'] + ['toilet paper']*2

total = catalog[cheuk_shopping[0]] + catalog[cheuk_shopping[1]] + catalog[cheuk_shopping[2]]

print(f"Cheuk is buying {cheuk_shopping}, and it's {total} pounds.")
