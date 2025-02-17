# 1. Data Types and Variables
# Task: Create a Python program 
# to convert temperatures between
# Celsius and Fahrenheit.

# Input: A temperature value 
# (can be in either Celsius or Fahrenheit).
# Output: Convert and display the 
# temperature in the other unit.
# Hints: Use basic arithmetic formulas for 
# conversion (C = (F - 32) * 5/9 and 
#             F = C * 9/5 + 32).


# F = int(input("value"))
# C = int(input("value"))
# A = (F - 32) * 5/9
# B = C * 9/5 + 32
# print(A)
# print(B)






# 2. Strings and String Operations
# Task: Write a program that checks if a word is a palindrome.

# Input: A string from the user.
# Output: Print "Palindrome" if the string is the same 
# forwards and backwards, otherwise print "Not Palindrome".
# Hint: Use string slicing (word[::-1]) to reverse the string.

# C = (input("value"))
# x = (input("value"))
# print(x[::-1])
# print(x[::1])








# 3. Lists
# Task: Create a program that takes a list of integers and 
# returns the largest number in the list.

# Input: A list of numbers (e.g., [2, 3, 1, 4, 9]).
# Output: The largest number in the list (e.g., 9).


# x = (input("enter list"))
# y = max(x)
# print(y)





# 4. Tuples
# Task: Write a program that swaps the first and last elements 
# of a tuple.

# Input: A tuple (e.g., (1, 2, 3, 4)).
# Output: A new tuple with the first and last elements swapped 
# (e.g., (4, 2, 3, 1)).


# x = (input("enter tuple"))
# y = x[::-1]
# print(y)



# 5. Dictionaries
# Task: Write a program that counts the frequency of words 
# in a sentence.
# Input: A sentence (e.g., "apple banana apple grape apple").
# Output: A dictionary where the keys are the words and the 
# values are the frequency counts 
# (e.g.,{"apple": 3, "banana": 1, "grape": 1}).  















# 6. Sets
# Task: Write a program to find the intersection of two sets.

# Input: Two sets (e.g., {1, 2, 3} and {2, 3, 4}).
# Output: A set with the common elements (e.g., {2, 3}).



# set1 = eval(input("Enter set1"))
# set2 = eval(input("Enter set 2"))
# set3 = set1.intersection(set2)
# print(set3) 





# 7. If/Else Statements
# Task: Create a program that determines whether a given 
# number is positive, negative, or zero.
# Input: A number (e.g., 5).
# Output: Print whether the number is "Positive", 
# "Negative", or "Zero". 



# n = eval(input("number"))
# if n == 0:
#     print("number is zero")
# elif n > 0:
#     print("number is positive")
# elif n < 0:
#     print("number is negative")






# 8. Loops
# Task: Write a program that calculates the sum 
# of all even numbers from 1 to a given number.

# Input: A number n.
# Output: The sum of all even numbers from 1 to n.


# thislist = eval(input("number"))
# mylist = thislist + thislist
# print(mylist)
   


# #  9. Functions
# Task: Write a function that takes a list of numbers 
# and returns the average of the list.

# Input: A list of numbers (e.g., [2, 4, 6, 8, 10]).
# Output: The average of the numbers (e.g., 6).
# Hint: Use sum() and len() to calculate the 
# sum and count of numbers.  

# 10. List Comprehension
# Task: Write a program that generates a list of squares 
# of numbers from 1 to 10 using list comprehension.

# Output: A list like [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].

# squares = [x**2 for x in range(1, 11)]
   
# print("List of squares from 1 to 10:", squares)

  

# 11. Lambda Functions
# Task: Create a program that sorts a list of tuples by the 
# second element using a lambda function.

# Input: A list of tuples (e.g., [(1, 2), (3, 1), (5, 4)]).
# Output: The list sorted by the second element of each tuple
#  (e.g., [(3, 1), (1, 2), (5, 4)]).






# 12. Exception Handling
# Task: Write a program that handles a division by zero error.
# Input: Two numbers, divide the first by the second.
# Output: If there is an exception (like division by zero), 
# handle it and print a message saying 
# "Cannot divide by zero."





# 13. File Handling
# Task: Write a program that reads a text file and counts the
#  number of lines and words.

# Input: A text file (you can create a sample file).
# Output: Print the number of lines and words in the file.










# 14. Classes and Objects
# Task: Create a class Car with attributes like  make, model,
#  and year. Add methods to display the 
# car's information and to calculate the car's age.

# Input: Instantiate a Car object with specific values.
# Output: Display the car’s information and age.


class MyClass:
 x = 5
p1 = MyClass()
print(p1.x) 