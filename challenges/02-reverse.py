# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

sentence = 'Look at the black dog jumped over the fence'
print(sentence[::-1])

num_array = [1,2,3]
num_array.reverse()
print(num_array)

split_sentence = list(sentence)
print(split_sentence)
split_sentence.reverse()
print(split_sentence)
reverse_sentence = ''.join(map(str, split_sentence))
print(reverse_sentence)