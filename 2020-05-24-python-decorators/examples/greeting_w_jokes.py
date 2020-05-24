
from functools import wraps

def adding_jokes(greeting):
    @wraps(greeting)
    def better_greeting(*args, **kwargs):
        """This is a function that greets and tell a joke"""
        greeting(*args, **kwargs)
        print("How did the farmer find his missing cow? He tractor down")
    return better_greeting

@adding_jokes
def greeting(name):
    "This is a simple greeting"
    print(f"Hello, {name}")

@adding_jokes
def special_greeting(name, gender):
    if gender == "female":
        print(f"hey babe, {name}")
    else:
        print(f"sup bro, {name}")

special_greeting("Cheuk", "female")
