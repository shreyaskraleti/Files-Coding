# Program for Simple Calculator using Python:
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
option = input("Choose operation: (+, -, *, /)")
if option == "+":
    print("result is:", a+b)
elif option == "-":
    print("result is:", a-b)
elif option == "*":
    print("result is:", a*b)
elif option == "/" and b != 0:
    print("result is:", a/b)
else:
    print("Invalid option or not divisible by zero!")