# # Python Programme
# print( "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
# "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" )

# # Reverse Number
# # a = input("Enter the number:- ")
# # b = a[::-1]
# # print("Reverse Number:- ", a == b)

# # def fib(n):
# #     a = 0
# #     b = 1
# #     for i in range(2, n):
# #         c = a+b
# #         a = b
# #         b = c
# #         print(c)
# # fib(8) 


# # factorial Number
# # def fact(n):
# #     if (n == 0 or n == 1):
# #         return 1
# #     else:
# #         return n * fact(n-1)

# # print("======",fact(8))

# # Take a input from the user and find the square and cube of a number.
# # a = int(input("Enter a number:"))
# # square = a**2
# # cube = a**3
# # print("square is:",{square},'\n' f"cube is:{cube}")

# # Find the simple interest.
# # p = int(input("enter a principal:"))
# # r = int(input("enter interest rate:"))
# # t = int(input("enter a time in years:"))
# # simple_interest = p*r*t/100
# # print("simple_interest:",simple_interest)

# # Write a program to perform operator using arithmetic operator.
# # a = int(input("enter a first number:"))
# # b = int(input("enter a second number:"))

# # print("addition:",a+b)
# # print("subtraction:",a-b)
# # print("multiplication:",a*b)
# # print("division:",a/b)
# # print("modulus:",a%b)
# # print("floor divison:",a//b)
# # print("exponential:",a**b)

# # Write a program to check wheather a string is a palidrome
# # string = input("enter a string: ")
# # string = string.lower()
# # if string==string[::-1]:
# #     print("this is a palidrome")
# # else:
# #     print("this is not a palidrome")

# # Write a program to check wheather a number is even or odd
# # a = int(input("enter a number: "))
# # if a%2==0:
# #     print("This is a even number.")
# # else:
# #     print("This is a odd number.") 

# # Write a program to check prime number
# # n = int(input("Enter a number:"))

# # if n<=1:
# #     print("Not prime number.")
# # else:
# #     for i in range(2, n):
# #         if n%i==0:
# #             print("Not prime number.")
# #             break
# #     else:
# #         print("Prime number.")            

# # # Write a program and use title(), capitalize(), swapcase().
# # str = input("Enter a string: ")
# # print("Title: ",str.title())
# # print("Capitalize: ", str.capitalize())
# # print("Swapcase: ",str.swapcase())

# # # Wap to print student information first name, last name, age, gender, mother name, father name, branch and college.
# # fname = input("Enter first name: ")
# # lname = input("Enter a last name: ")
# # age = int(input("Enter your age: "))
# # gender = input("Enter your gender: ")
# # mother_name = input("Enter your mother name: ")
# # father_name = input("Enter your father name: ")
# # branch = input("Enter your branch: ")
# # college = input("ENter your college name: ")
# # print(f"My name is {fname}{lname} and my age is {age}. I am a {gender}. My mother's name is {mother_name} and my father's name is {father_name}. I am pursing my {branch} in {college}.")

# # # Wap and use nested if
# # num = int(input("Enter a number: "))
# # if num > 0:
# #     if num%2== 0:
# #         print("positive and even number.")
# #     else:
# #         print("negative and odd number.")
# # else:
# #     print("negative number:")

# # # wap and find the percentage of student.
# # percentage = int(input("Enter percentage: "))
# # if percentage >=60:
# #     print("1st division")
# # elif percentage >=40:
# #     print("2nd division")
# # elif percentage >=33:
# #     print("3rd division")
# # else:
# #     print("fail")

# # # Wap and use split()
# # str = input("Enter a string: ")
# # str_result = str.split()
# # print("result  =",str_result)

# # #count and tell appearance of repeated list.
# # list = [2,3,4,5,6,5,3,2,7,4,5,2,3,4,5,7,7,8,9,9,9]
# # count = {}
# # for i in list:
# #     count[i]= count.get(i,0)+1
# # print(count)

# # # Wap and whether a year is leap year or not.
# # year = int(input("Enter a year: "))
# # if (year%400==0) or (year%4==0 and year%100!=0):
# #     print("This is a leap year.")
# # else:
# #     print("This is not a leap year.")

# # #check frequency of a string.
# # str = input("Enter a character: ")
# # frequency = {}

# # for char in str:
# #     if char in frequency:
# #         frequency[char] += 1
# #     else:
# #         frequency[char] = 1
# # print(frequency)

# # # Write a program and check whether a number is divisible by 5 and 11.
# # num = int(input("Enter a number: "))
# # if num%5==0 and num%11==0:
# #     print("It is divisible by 5 and 11.")
# # else:
# #     print("It is not divisible by 5 and 11.")

# #to check whether which number is larger. 
# # numbers = [10, 45, 23, 89, 34]

# # largest = numbers[0]

# # for num in numbers:
# #     if num > largest:
# #         largest = num

# # print("Largest number is:", largest)

# # # Accept temperature in celsuis and print whether water is boiling or not.
# # a = float(input("Enter the temperature: "))
# # if a>=100:
# #     print("Water is boiling.")
# # else:
# #     print("Water is not boiling.")

# # # Write a program to find maximum and minimum numbers.
# # a = [23,45,67,34,56,12,45]
# # maximum = max(a)
# # minimum = min(a)
# # print("list of number: ", a)
# # print("maximum number: ", maximum)
# # print("minimum number: ", minimum)

# #add two number.
# # a = int(input("Enter 1st number: "))
# # b = int(input("Enter 2nd number: "))
# # sum = a+b
# # print("result= ",sum)

# # Accept two numbers and print the greatest number between them
# # a = int(input("enter first number:"))
# # b = int(input("enter second number:"))
# # if a>b:
# #     print(" a is greater than b")
# # else:
# #     print(" b is greater than a")

# # Accept the gender from the user as char and print the respective message.
# # gen = input("enter your gender as character(M or F): ")
# # if gen== "M":
# #     print("good morning sir")
# # else:
# #     print("good morning mam")

# # Accept name and age from the user and check if the user is valid for vote or not.
# # name = input("Enter your name: ")
# # age = int(input("enter your age: "))
# # if age >=18:
# #     print(f"hello {name} you are valid voter.")
# # else:
# #     print(f"hello {name} you are not a valid voter.")

# # Write a program to simple calculator.
# # a = int(input("Enter first number: "))
# # b = int(input("Enter a second number: "))
# # c = input("Enter operator(+, -, *, /): ")

# # if c=='+':
# #     print("result= ",a+b)
# # elif c=='-':
# #     print("result= ",a-b)
# # elif c=='*':
# #     print("result: ",a*b)
# # elif c=='/':
# #     print("result: ",a/b)
# # else: 
# #     print("invalid operator")

# # Write a program to print  table of any number.
# a = int(input("Enter a number for table:"))
# for i in range(1, 11):
#     print(a,"x",i,"=",a*i)

# Print natural number upto n.
# n = int(input("enter natural number: "))
# for i in range(1, n+1):
#     print(i)

# # Reverse loops from n to 1.
# n = int(input("Enter a number for reverse: "))
# for i in range(n,0,-1):
#     print(i)

# # Take a number and print the table.
# n = int(input("Enter a number: "))
# for i in range(1,11):
#     print(n,"x",i,"=",n*i)

# Print sum of all even or odd in a range separately.
# n = int(input("Enter a number:"))
# even = 0
# odd = 0
# for i in range(1, n+1):
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i
# print(f"sum of all even number is {even} and odd number is {odd}.")

# Print factor of any number.
# n = int(input("Enter any number: "))
# for i in range(1, n+1):
#     if n%i==0:
#         print(i)

# Check whether the number is pefect number or not.
# n = int(input("Enter any number: "))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("Perfect number")
# else:
#     print("Not a perfect number")

# Check whether the number is prime or not.
# n = int(input("Enter the number: "))
# count = 0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("This is a Prime Number.")
# else:
#     print("This is not a Prime Number.")