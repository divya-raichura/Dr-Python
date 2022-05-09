stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    num = 0
    for k, v in inventory.items():
        num += v
        print(f'{v} {k}')
    print(f"Total number of items: {num}")


display_inventory(stuff)
