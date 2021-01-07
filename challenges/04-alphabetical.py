# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

word = 'poTatasdfEWSkkdhdTTUNEGSKuiebhwmdho'
lower_word = word.lower()
split_word = list(lower_word)
split_word.sort()
new_word = ''.join(map(str, split_word))
print(new_word)