allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def this(all_guests, item):
    num = 0
    for k, v in all_guests.items():
        num += v.get(item, 0)
    return num


print('Number of things being brought:')
print(' - Apples         ' + str(this(allGuests, 'apples')))
print(' - Cups           ' + str(this(allGuests, 'cups')))
print(' - Cakes          ' + str(this(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(this(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(this(allGuests, 'apple pies')))
