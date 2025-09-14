def happy_birthday(first_name, age):
    print(f"Happy Birthday {first_name}")
    print(f"You are {age} years old")


happy_birthday("David", 20)


def display_invoice(username, amount, due_date):
    print(f"Hello {username}, your invoice amount is {amount:.2f} and due_date is {due_date}")


display_invoice("David", 45.50, "2020")


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


print(add(1, 2))
print(sub(1, 2))
print(mul(1, 2))


def create_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return first_name + " " + last_name


full = create_name("monarch", "Corps")
print(full)
