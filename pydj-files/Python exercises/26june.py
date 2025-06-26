# 1. Write a program to take a number from the user and print whether it is even or odd.
a = int(input("Enter a number:"))
if a%2 == 0:
    print("a is even number")
else:
    print("a is odd number")

# 2. Ask the user to input three numbers. Print the largest one.
a = int(input("enter your first number:"))
b = int(input("enter your second number:"))
c = int(input("enter your third number:"))
if a>b and a>c:
    print("a is largest number")
elif b>a and b>c:
    print("b is largest number")
else:
    print("c is largest number")
    
# 3. Input a number n, and print the sum of the first n natural numbers.
n = int(input("Enter a number:"))
total = 0
for i in range(1, n+1):
    total += i
print("sum is", total)

# 4. Take a string from the user and check if it is a palindrome (reads the same backward).
a = input("Enter a string:")
if a == a[::-1]:
    print("a is palindrome")
else:
    print("a is not a palindrome")
    
# 5. Ask the user to input a number, and print its multiplication table from 1 to 10.
a = int(input("Enter your number:"))
table = list(map(lambda i : i * a, range(1,11)))
print("Multiplication table is:", table)