import random

low = 1
high = 100
options = ("rock", "paper", "scissor")
cards = ["2,", "3", "4", "T", "L"]

# number =  random.randint(low, high)
# number = random.random()
# option = random.choice(options)

random.shuffle(cards)
print(cards)
