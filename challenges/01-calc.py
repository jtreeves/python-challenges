# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

age_string = input('How old are you? ')
age_int = int(age_string)
age_plus_one = age_int + 1
print('In one year, you will be {} years old.'.format(age_plus_one))