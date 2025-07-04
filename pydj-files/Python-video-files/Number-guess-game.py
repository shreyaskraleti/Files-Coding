import random
number = random.randint(1,10)
guess = int(input("Enter a number 1-10:"))
if guess == number:
    print(f"guess is matching with number")
else:
    print(f"guess is not matching and the number is {number}")