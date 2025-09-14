# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")
#
# hello("Good morning", first="Monarch", title="Mr", last="Corps")

# for x in range(1, 11):
#     print(x, end=" ")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country="234", area="808", first="113", last="596")

print(phone_num)
