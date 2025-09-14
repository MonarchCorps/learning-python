# def add(*args):
#     total = sum(args)
#     return total
#
# print(add(1, 2, 2))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
#
# display_name("Monarch", "Corps")

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# print_address(
#     street="Ayinde Sanni",
#     city="Ikeja",
#     state="Lagos",
#     zip="102010"
# )

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "street" in kwargs:
        print(f"{kwargs.get('street')}")
    else:
        print(f"{kwargs.get('city')} {kwargs.get('state')}")

shipping_label(
    "Dr.",
    "Monarch",
    "Corps",
    # street="Ayinde Close",
    apt="100",
    city="Austin",
    state="California",
    zipcode="12345",
)
