def immutable_eg(s):
    s = s + 'musk'
    print('inside', s)


string = 'elon'
print('before calling:', string)
immutable_eg(string)
print('after calling',string)
