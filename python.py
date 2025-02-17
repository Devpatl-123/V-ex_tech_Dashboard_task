# # # 1. Basics of Python
# # Write a Python program to print "Hello, World!".
# # Write a program to take user input for their name and 
# # print a greeting message.
# # What is the difference between print() and input()
# #  in Python?
# # Write a program to swap two variables without using a 
# # third variable.
# # Write a Python script to check the type of a variable.

# 1

# a = (input("Devanshu"))
# d = (input("Hellow,word"))
# print(d)

2
a = 3 
b = 7
a = b
print(a)

# b = a 
# print(b)
# print(type(a))




# # 2. Data Types and Variables
# # What are mutable and immutable data types in Python?
# # Write a program to convert an integer to a string and vice versa.
# # Write a program to check if a number is of integer type.
# # What will be the output of print(type([]) is list)? Explain why.
# # Create a dictionary with three key-value pairs and print the value of a specific key
# #
# # 
# #   - list :
# # x = ["shailesh", "dev"]
# # print(x)
# #

# #  #  - Dictionaries 
# # person1 = { 
# # "name": "John", 
# # "age": 36, 
# # "country": "Norway" 
# # } 
# # print(person1)
# # 
# #  - set 
 
# # # set = {1, 2, 3, 4, 11, 15, 2, 3, 15}
# print(set)

# # immutable data:-

# #   Integer - 
# x = [1,3,2]
# print(x)



# #  string - 


#  #tuple - 
# #  Write a program to convert 
# # an integer to a string and vice versa.





# # Write a program to check if a number 
# # is of integer type.
# def is_integer(value):
#     return type(value) == int

# value = 123

# print(is_integer(value)) 

# value = 12.34
# print(is_integer(value))  




# # What will be the output of 
# # print(type([]) is list)? Explain why.


# # Create a dictionary with three key-value pairs
# #  and print the value of a specific key.

# my_dict = { 
# "name": "John", 
# "age": 36, 
# "country": "Norway" 
# } 
# print(my_dict["age"])








# # 3. Operators
# # Write a Python program to demonstrate the use of
# #  all arithmetic operators.
# # What is the difference between is and == operators?


# Addition (a + b)
# a = 10
# b = 5
# print(a + b)

# Subtraction (a - b)
# print(a - b)

# Multiplication
# print(a * b)

# division
# print(a / b)

# Modulus 
# print(a % b)


# # What is the difference between is and == operators?
# a = 1
# b = 1 
# #  print( a == b )  ( Compares the memory addresses of the two objects to see if they are the exact same object.)

# a = [1,2,3]
# b = [1,2,3]
# print(a is b ) 


# # # == compares values (whether they are the same).
# # # is compares identities 
# # (whether they are the exact same object in memory).






# # Write a Python program to check if a number is even or 
# # odd using conditional operators.


# num = int(input("Enter a number: "))

# if num %2  == 0:
#     print(num, " is even")
# else:
#     print(num," is odd")


# # # Explain the working of bitwise operators in Python with an example.
# a = 5   
# b = 3   

# # AND Operator
# and_result = a & b
# print(f"{a} & {b} = {and_result}") 

# # OR Operator
# or_result = a | b
# print(f"{a} | {b} = {or_result}")  


# # Write a program to swap two numbers using bitwise XOR.
 
# a =(input('enter the value:'))
# # x = [1, 2, 3, 4]
# swapped_x = a[::-1]
# print(swapped_x)










# # 4. Control Flow (if-else, loops)
# # Write a program to check if a given 
# # number is positive, negative, or zero.
# # Write a Python program to print the first 10 
# # numbers using a for loop.


# number = int(input("enter the number - "))

# if number > 0:
#     print("the number is possitive")
# elif number < 0:
#     print("the number is negetive")
# else:
#     print("the number is zero")



# #  Write a Python program to print the first 10
# #  numbers using a for loop.

# for x in range(1 , 11):
#     if x %2 == 0:
#           print(x, "is even")
#     else:
#          print(x, "is odd")




# # What is the difference between break and continue statements? Give examples.
# # Loop through numbers 1 to 5
# for x in range(1, 6):
#     if x == 3:
#         print("Skipping x = 3")
#     print(x)

# # Write a program to check whether a given year is
# #  a leap year.

# year = int(input("Enter a year: "))

# if (year % 4 == 0):
#     print(year, "is a leap year.")
# else:
#    print(year, "is not a leap year.")





# 5. Functions
# Write a function to find the sum 
# # of two numbers.
# def sum_two_numbers(a, b):
#     return a + b
# a = 5
# b = 10
# result = sum_two_numbers(a, b)
# print(f"The sum of {a} and {b} is {result}.")



# Explain the difference between return
#  and print() in functions
# 
# # e return statement sends the result (10) back to the caller (add_numbers()), which allows it to be stored in result and used later.

# def factorial(n):

#     if n == 0 or n == 1:  # Base case
#         return 1
#     else:
#         return n * factorial(n - 1)  
# num = 2
# result = factorial(num)
# print(f"The factorial of {num} is {result}.")






# What is the use of *args
#  and **kwargs in function definitions?

# def display_info(*args, **kwargs):
   
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)


# display_info(1, 2, 3, name="John", age=25)


# Write a function that takes a list and returns
#  a new list with only even numbers.


# # x = int(input("Enter a number: "))
# for x in range(1 , 10): 
     
#  if x %2  == 0:
#     print(x, " is even")



# 6. Lists and Tuples
# Write a Python program 
# to find the largest element in a list.


# thislist = [1,2,3,4,5,6]
# print(max(thislist))


# What is the difference between a list and a tuple?



# Lists are preferred when you need a dynamic collection
#  of items (e.g., a list of user inputs).
# Tuples are used for fixed collections 
# (e.g., coordinates, days of the week) to protect 
# data from modification.



# Write a Python program to reverse a list without 
# using reverse().



# thislist = [1,2,3,5,4,6,7]
# thislist.sort(reverse = True)
# print(thislist)

# Write a program to find the sum of all elements in a tuple.
# def sum_all(*args):
   
#     return sum(args)

# result = sum_all(1, 2, 3, 4, 5)
# print(f"The sum is {result}.") 



# # Explain how list slicing works in Python with an example.





# b = "Hello, World!"
# print(b[2:5])
# b = "Hello, World!"
# print(b[:5])

# b = "Hello, World!"
# print(b[2:]) 


# 7. Strings
# Write a Python program to check if a string is a palindrome.

# def is_palindrome(string):
    
#     cleaned_string = ''.join(char.lower() for char in string if char.isalnum())

#     return cleaned_string == cleaned_string[::-1]


# user_input = input("Enter a string: ")


# if is_palindrome(user_input):
#     print(f'"{user_input}" is a palindrome.')
# else:
#     print(f'"{user_input}" is not a palindrome.')




# What is the difference between split() and join() methods?

# split
# a = "Hello, World!"
# print(a.split(",")) 
 

# #  join
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3) 

# Write a program to count the number 
# of vowels in a given string.




# def count_vowels(string):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in string:
#         if char in vowels:
#             count += 1
#     return count

# string = input("Enter a string: ")
# vowel_count = count_vowels(string)
# print(f"The number of vowels in the given string is: {vowel_count}")




# Write a Python program to replace all
#  occurrences of a word in a string.
# a = "Hello, World!"
# print(a.replace("H", "Hi H")) 


# Explain how f-strings work in Python with an example.


# name = "Devanshu"
# age = 21
# height = 6

# # Using f-strings
# greeting = f"My name is {name}, I am {age} years old, and I am {height:.1f} feet tall."
# print(greeting)







# 8. Dictionaries and Sets
# Write a Python program to merge two dictionaries.


# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"d": 4, "e": 5, "c": 6}

# merged_dict = dict1 | dict2
# print("Merged Dictionary:", merged_dict)




# How do you access a value from a dictionary safely 
# without an error?




# Write a program to remove duplicates from a list using sets.
# a = input("set")

# unique_list = list(set(a))
# print(unique_list)



# Write a Python program to find the common elements 
# between two sets.


# a = input("set 1")
# b = input("set 2")
# common = list(set(a) & set(b))
# print(common)



# Explain how dictionary comprehensions work with an example


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x ]
# print(newlist) 



# 9. File Handling
# Write a Python program to read a file and print
#  its contents.




# Explain the difference between r, w, a, and r+ modes
#  in file handling.


# r (Read Mode)
# Opens the file for reading only

"""2. w (Write Mode)
Opens the file for writing only.
If the file exists, its content is overwritten.
If the file doesn’t exist, a new file is created."""


'''3. a (Append Mode)
Opens the file for writing, but does not overwrite the existing content.
The file pointer is positioned at the end of the file.
If the file doesn’t exist, a new file is created.'''


'''4. r+ (Read and Write Mode)
Opens the file for both reading and writing.
The file must exist, or it will raise a FileNotFoundError.
The file pointer is positioned at the beginning, so writing will overwrite from the 
start unless moved.'''

# Write a program to copy the contents of one file to another.

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)




# Write a Python script to count the number of words in a file


# set = input("set")
# x = set.count("22") 
# print(x)


# What is the use of the with statement in file handling?




     


# '''10. Object-Oriented Programming (OOP)
# Define a class in Python and create an object of that class.
# What is the difference between instance variables and class variables?
# Explain the concept of inheritance in Python with an example.
# What is the use of super() in Python?
# Write a Python program demonstrating method overriding.'''

# 11. Exception Handling
# Write a program to demonstrate try, except,
#  finally blocks.






# What is the difference between raise and assert statements?










# Write a Python program to handle a ZeroDivisionError.











# What is the purpose of custom exceptions in Python?











# Write a function that raises a ValueError if the input is 
# not a positive integer.







# 12. Modules and Libraries
# Write a Python program to import a module and use its function.

# import math
# result = math.sqrt(16)
# print(result)




# Explain the difference between import module and from 
# module import function.








# Write a program using the random module to generate a 
# random number between 1 and 100.


# from datetime import datetime
# import random

# current_datetime = datetime.now()

# random_number = random.randint(1, 100)

# print("Current Date and Time:", current_datetime)

# print("Random Number:", random_number)








# How do you install external libraries in Python?










# Write a Python script to get the current date and time 
# using the datetime module


# from datetime import datetime
# import random

# current_datetime = datetime.now()
# print("Current Date and Time:", current_datetime)



# 13. Regular Expressions
# Write a Python program to check if a given string contains 
# only digits using regex.








# Explain the difference between re.search() and re.match()








# Write a program to extract all email addresses from a given 
# text using regex









# What is the purpose of re.sub() in Python?










# Write a regex pattern to validate a strong password.












# 15. Web Scraping (BeautifulSoup & Requests)
# Write a Python script to fetch the HTML content of a 
# webpage using requests.






# How do you parse an HTML page using BeautifulSoup?














# Write a program to extract all hyperlinks from a webpage











# Explain the difference between find() and find_all() in BeautifulSoup.












# Write a script to extract the title of a webpage using web scraping













# 16. Data Science & Pandas
# Write a Python program to read a CSV file
#  using Pandas.






# What is the purpose of df.describe() in Pandas?












# Write a program to filter rows in a DataFrame based on a condition.
# Write a script to plot a graph using matplotlib.







# What is the use of groupby() in Pandas?







# 19. Decorators
# Task: Write a decorator that measures the time taken to execute a function.

# Input: A function that performs some task.
# Output: The time taken to execute the function.


















# 20. Web Scraping
# Task: Use the requests and BeautifulSoup libraries to scrape the titles of articles from a website (e.g., a news website).

# Input: The URL of the website.
# Output: A list of article titles.

import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h1')
    for title in titles:
        print(title.text)

url = input("Enter the URL to scrape: ")
scrape_titles(url)








# 17. Advanced Topics
# Explain the concept of decorators with an example.






# Write a Python program using a generator function.








# How does multithreading work in Python?








# What is the Global Interpreter Lock (GIL)?












# Explain how Python handles memory management.
