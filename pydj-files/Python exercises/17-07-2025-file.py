# right angled triangle of stars:
rows = int(input("Enter no. of rows:"))
for i in range(1, rows+1):
    print("*" * i)

# Armstrong number:
num = int(input("Enter a number:"))
sum = 0
temp = num
while temp>0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num, "is armstrong number")
else:
    print(num, "is not an armstrong number")
    
# factorial:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# remove:
animals = ["cat", "dog", "tiger", "elephant"]
animals.remove("tiger")
print(animals)

# pop:
animals = ["cat", "dog", "tiger", "elephant"]
animals.pop(2)
print(animals)
animals.pop()
print(animals)

# math module:
import math
print(math.sqrt(25))
print(math.sqrt(9))
print(math.sqrt(16))
print(math.sqrt(4))
print(math.factorial(5))
print(math.pow(3,2))