# chapter-2
# Strings:
# to input user first name and print its length.
first_name = input("Enter your first name:")
length = len(first_name)
print("length of first name is:", length)

# to find count of $ in your string:
word = "i have $2300 dollars and my husband have $3500 dollars"
print(word.count("$"))

#conditional statements:
# check if a number entered by the user is odd or even.
num = int(input("enter a number:"))
if num%2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
    
# check which number is largest among three
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
if (a>=b and a>=c):
    print("a is largest number")
elif (b>=c):
    print("b is largest number")
else:
    print("c is largest number")
    
# check if a number is multiple of 7.
a = int(input("enter a number:"))
if a % 7 == 0:
    print(a, "is multiple of 7")
else:
    print(a, "not a multiple of 7")


