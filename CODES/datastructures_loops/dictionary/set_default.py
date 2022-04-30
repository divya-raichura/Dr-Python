# spam = {'name': 'Pooja', 'age': 5}
# if 'color' not in spam:
#     spam['color'] = 'black'

# spam.setdefault('color', 'black')
# The first time setdefault() is called, the dictionary in
# spam changes to {'age': 5, 'name': 'Pooka', 'color': 'black'}.
#  When spam.setdefault('color', 'white') is called next, the
#  value for that key is not changed to 'white', because spam
#  already has a key named 'color'.


# amazing example
# this programs counts how many times each letter appeared
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# we will create dictionary to count how many times every
# character comes in the message
# if the character is not in dictionary, we add it

count = {}

for character in message:
    count.setdefault(character, 0)  # this means if eg, character 'w'
    # so setdefault() means, if character 'w' is not in dict,
    # add it to dict as key and make its value as 0, if it exists
    # then ignore
    count[character] += 1  # this means increase the value of key
    # eg 'w' key as one as it appeared once right now

print(count)