birthdays = {'Divya': "1 Apr", 'Daddy': '29 Apr', 'Mummy': '22 Apr',
             'Vedika': '9 Apr'}
while True:
    name = input('Enter a name: (blank to quit) ')
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        birthdays[name] = input('What is their birthday? ')
        print('Birthday database updated.')


# note:
# You can see if the entered name exists as a key in the
# dictionary with the in keyword, just as you did for lists.
# If the name is in the dictionary, you access the associated
# value using square brackets; if not, you can add it using
# the same square bracket syntax combined with the assignment
# operator


# Of course, all the data you enter in this program is
# forgotten when the program terminates. You’ll learn how to
# save data to files on the hard drive in Chapter 9.
