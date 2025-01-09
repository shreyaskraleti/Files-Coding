# 1. Program to Find the Factorial of a Number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
a = int(input("Enter a number:"))
result = factorial(a)
print(f"factorial of {a} is {result}")

#2. Program to find even or odd number
a = int(input("enter a number:"))
if a % 2 == 0:
    print(f"{a} is even number")
else:
    print(f" {a} is odd number")
    

