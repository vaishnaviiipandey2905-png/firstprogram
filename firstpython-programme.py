# Python Programme
print( "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" )

# Reverse Number
# a = input("Enter the number:- ")
# b = a[::-1]
# print("Reverse Number:- ", a == b)

# def fib(n):
#     a = 0
#     b = 1
#     for i in range(2, n):
#         c = a+b
#         a = b
#         b = c
#         print(c)
# fib(8) 


# factorial Number
# def fact(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n * fact(n-1)

# print("======",fact(8))

# Take a input from the user and find the square and cube of a number.
# a = int(input("Enter a number:"))
# square = a**2
# cube = a**3
# print("square is:",{square},'\n' f"cube is:{cube}")

# Find the simple interest.
# p = int(input("enter a principal:"))
# r = int(input("enter interest rate:"))
# t = int(input("enter a time in years:"))
# simple_interest = p*r*t/100
# print("simple_interest:",simple_interest)

# Write a program to perform operator using arithmetic operator.
# a = int(input("enter a first number:"))
# b = int(input("enter a second number:"))

# print("addition:",a+b)
# print("subtraction:",a-b)
# print("multiplication:",a*b)
# print("division:",a/b)
# print("modulus:",a%b)
# print("floor divison:",a//b)
# print("exponential:",a**b)

# Write a program to check wheather a string is a palidrome
# string = input("enter a string: ")
# string = string.lower()
# if string==string[::-1]:
#     print("this is a palidrome")
# else:
#     print("this is not a palidrome")

# Write a program to check wheather a number is even or odd
# a = int(input("enter a number: "))
# if a%2==0:
#     print("This is a even number.")
# else:
#     print("This is a odd number.") 

# Write a program to check prime number
# n = int(input("Enter a number:"))

# if n<=1:
#     print("Not prime number.")
# else:
#     for i in range(2, n):
#         if n%i==0:
#             print("Not prime number.")
#             break
#     else:
#         print("Prime number.")            

# # Write a program and use title(), capitalize(), swapcase().
# str = input("Enter a string: ")
# print("Title: ",str.title())
# print("Capitalize: ", str.capitalize())
# print("Swapcase: ",str.swapcase())

# Wap to print student information first name, last name, age, gender, mother name, father name, branch and college.
fname = input("Enter first name: ")
lname = input("Enter a last name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
mother_name = input("Enter your mother name: ")
father_name = input("Enter your father name: ")
branch = input("Enter your branch: ")
college = input("ENter your college name: ")
print(f"My name is {fname}{lname} and my age is {age}. I am a {gender}. My mother's name is {mother_name} and my father's name is {father_name}. I am pursing my {branch} in {college}.")