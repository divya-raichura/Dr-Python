import random

value = random.randint(1, 6)  # both inclusive
a = ['hi', 'hello', 'howdy', 'hola']
choice = random.choice(a)  # random value from list

colors = ['red', 'black', 'green']
# we want 10 rounds of random colors
# print(random.choices(colors, k=10))


# but what if there are 18 red packets, 18 black, 2 green this means
# probability of red-black shud be more and they shud appear more
# we can do this using
choices = random.choices(colors, k=10, weights=[18, 18, 2])
# probability: 18/38, 18/38, 2/38
# print(choices)


# what if want to shuffle a list of deck of 52 cards
deck = list(range(1, 53))
random.shuffle(deck)
# print(deck)
# if we want to select 5 random cards, we can't use choices method
# cause it can pick same card twice, we want unique only
hand = random.sample(deck, k=5)
print(hand)

