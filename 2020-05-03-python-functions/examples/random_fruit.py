import random

def lucky_draw(basket):
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
    return check_out

my_basket = ["apple", "orange", "pear", "banana", "peach"]
print(f"At the end I got {lucky_draw(my_basket)}")

print("Another basket")
another_basket = ["apple", "orange", "pear", "banana", "peach", "apple", "apple", "apple", "apple"]
print(f"At the end I got {lucky_draw(another_basket)}")
