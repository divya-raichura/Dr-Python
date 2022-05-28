print('''program starts!''')
ch = input('wanna play? y [yes] / n [no] : ')
ch_lower = ch.lower()

while ch_lower != 'n':
    age = int(input("your age? "))
    if age > 18:
        print('you can vote')
    elif age < 18:
        print('you cannot vote')
    else:
        print('welcome new voter 😊😎')
    ch = input('wanna play again? y [yes] / n [no] : ')
    ch_lower = ch.lower()

print('program ends')
