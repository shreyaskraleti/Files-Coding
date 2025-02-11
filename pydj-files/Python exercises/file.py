""" Write a Python program to find a list of integers with exactly two occurrences of nineteen 
and at least three occurrences of five. Return True otherwise False. """
def check_occurences(num):
    return num.count(19) == 2 and num.count(5) >= 3

a = [19,19,2,3,5,5,5,2]
print(check_occurences(a))
b = [19,19,2,3,5,5,2]
print(check_occurences(b))
c = [19,2,3,5,5,5,2]
print(check_occurences(c))






