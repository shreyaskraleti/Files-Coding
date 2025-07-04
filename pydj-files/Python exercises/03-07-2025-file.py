# 1) Sum of Even Numbers in a List:
# Write a Python function that takes a list of integers and returns the sum of all even numbers in the list.
def sum_even(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total
    
my_list = [1,2,3,4,5,6,7,8,9,10]
result = sum_even(my_list)
print("sum of even numbers:", result)

# 2) Remove Duplicates:
# Write a Python program that takes a list and returns a new list with duplicates removed.
def remove_duplicates(old_list):
    new_list = list(set(old_list)) # set will remove duplicates
    return new_list
a = [1,2,2,3,1,3,4,5,4,5,6,1]
result = remove_duplicates(a)
print("new list is:", result)

# MCQ in Python:
# 1) How do you print “Hello, World!” in Python?
# A) print("Hello, World!") - option-A
# B) echo "Hello, World!"
# C) printf("Hello, World!")
# D) cout << "Hello, World!";

# 2) Which of these is the correct way to assign a variable in Python?
# A) int x = 5
# B) x = 5 - option-B
# C) 5 = x
# D) x : 5

# 3) What will len("Python") return?
# A) 5
# B) 6 - option-B
# C) 7
# D) Error

# 4) Which keyword is used to define a function in Python?
# A) function
# B) def - option-B
# C) fun
# D) define

# 5) What does the expression 4 // 2 evaluate to?
# A) 2.0 - option-A
# B) 2
# C) 2.5
# D) Error

# # 6) How do you write a single-line comment in Python?
# A) // This is a comment 
# B) /* This is a comment */
# C) # This is a comment - option-C
# D) -- This is a comment

# 7) Which data type is immutable in Python?
# A) list
# B) dict
# C) set
# D) tuple - option-D

# 8) What does my_list.append(10) do?
# A) Removes 10 from my_list
# B) Adds 10 to the end of my_list - option-B
# C) Sorts my_list
# D) Inserts 10 at the start of my_list

# 9) Which of these loops does Python support?
# A) for
# B) while
# C) Both A and B - option-C
# D) Neither A nor B

# 10) What will print(type(3.14)) output?
# A) <class 'int'>
# B) <class 'str'>
# C) <class 'float'> - option-C
# D) <class 'bool'>

