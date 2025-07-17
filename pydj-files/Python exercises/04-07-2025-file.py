# 1. Write a program that takes a string input from the user and prints the reversed string.
string_input = input("enter a string:")
reversed_string = string_input[::-1]
print("Reversed string is:", reversed_string)

# 2. Write a program that takes a string input from the user and checks if it’s a palindrome.
input_string = input("enter a string:")
if input_string == input_string[::-1]:
    print("input string is a palindrome")
else:
    print("input string is not a palindrome")

# 3. Write a program that takes a sentence input and counts the number of words. Words are separated by spaces.
sentence = input("enter a sentence:")
words = sentence.split()
word_count = len(words)
print("word count is:", word_count)

# 4. Write a program that takes a positive integer input from the user and calculates the sum of its digits.
number = int(input("enter a positive no:"))
total = 0
for i in str(number):
    total += int(i)
print("sum of digits is:", total)

# 5. Write a program that takes the radius of a circle as input from the user and calculates the area.
import math
radius = float(input("enter radius:"))
area = math.pi * radius * radius
print("area of a circle is:", area)