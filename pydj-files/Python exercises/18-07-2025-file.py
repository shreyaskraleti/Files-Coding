# Chapter-1 - Apna College:
# Variables and Data types:
# sum
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
sum = num1 + num2
print("sum is:", sum)

# area of a square
s = float(input("enter side:"))
area = s * s
print("area of a square is:", area)

# average
num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
average = (num1 + num2)/2
print("average of 2 numbers is:", average)

# input 2 floating point numbers and print their average.
num1 = float(input("enter first float number:"))
num2 = float(input("enter second float number:"))
average = (num1+num2)/2
print("average is:", average)

# input 2 int numbers, a and b, print true a is greater than or equal to b, if not false.
a = int(input("enter first number:"))
b = int(input("enter second number:"))
if a>=b:
    print("True")
else:
    print("False")