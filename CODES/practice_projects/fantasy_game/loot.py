inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def add_to(inventory, loot):
    new_inv = {}
    num = 0
    for item in loot:
        if item not in inventory:
            new_inv.setdefault(item, 1)
        else:
            inventory[item] += 1
    for k, v in inventory.items():
        new_inv[k] = v
        num += v
    print("Inventory:")
    for k, v in new_inv.items():
        print(f'{k} {v}')
    print()
    print(f"Total number of items: {num}")
    return new_inv


def add_to_better(inventory, loot):
    num = 0
    for item in loot:
        if item not in inventory:
            # num += 1
            inventory.setdefault(item, 1)
        else:  # we can simplify to avoid else see in both_simplified file
            inventory[item] += 1
            # num += inventory[item]  # wrong, adds gold coins or any other items every else condition
    print("Inventory:")
    for k, v in inventory.items():
        num += v
        print(f'{k} {v}')
    print()
    print(f"Total number of items: {num}")
    return inventory


# print(add_to(inv, dragonLoot))
print(add_to_better(inv, dragonLoot))
