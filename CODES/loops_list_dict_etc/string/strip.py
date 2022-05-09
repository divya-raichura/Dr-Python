spam = '    Hello World!    '
# print(spam.strip())
# print(spam.lstrip())
# print(spam.rstrip())


#
s = 'SpamSpamBaconSpamEggsSpamSpam'
#  a string argument will specify which characters on the
#  ends should be stripped
# The order of the characters in the string passed to strip()
# does not matter: strip('ampS') will do the same thing as
# strip('mapS') or strip('Spam').
print(s.strip('ampS'))
