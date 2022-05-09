# Unlike lists, items in dictionaries are unordered.
# The first item in a list named spam would be spam[0].
# But there is no “first” item in a dictionary. While the
# order of items matters for determining whether two lists are
# the same, it does not matter in what order the key-value
# pairs are typed in a dictionary.

# >>> spam = ['cats', 'dogs', 'moose']
# >>> bacon = ['dogs', 'moose', 'cats']
# >>> spam == bacon
# False
# >>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
# >>> ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
# >>> eggs == ham
# True
