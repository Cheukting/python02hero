import random
basket = ["apple", "orange", "pear", "banana", "peach"]
check_out = []
while True: #DANGER
    choice = random.choice(basket)
    if choice == "oranges":
        print(f"Oh no!")
        continue

    if choice == "banana":
        print("I have got banana!")
        check_out.append(choice)
        break
    else:
        print(f"I got {choice}. Try again")
        check_out.append(choice)

print(f"At the end I got {check_out}")
