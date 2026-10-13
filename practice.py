#Count the positive, negative, and zeroo  Given: numbers = [10, -5, 0, 8, -2, 0, 15, -7] find: numbers of positive values, numbers of negative values, number of zeroes....
'''numbers = [10, -5, 0, 8, -2, 0, 15, -7]

positive = 0
negative = 0
zeros = 0
for num in numbers:
    if num > 0:
        positive +=1
    elif num < 0:
        negative +=1
    else:
        zeros +=1
print("positive values:",positive)
print("negative values:",negative)
print("zeros values:",zeros)'''

#find the second largest number Given: numbers = [12, 34, 7, 32, 18, 78, 29] find the second largest distinctt number. Don't use sort() or sorted().
'''def second_largest(arr):
    first = arr[0]
    second = first

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second
print(second_largest([12, 34, 7, 32, 18, 78, 29]))'''

#Write a programm to reverse a string and try solving it using a loop first...
'''def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text 
    return reversed_text


xyz = "Hello World"
print(reverse_string(xyz))'''

#write a program to count the vowlels and also count the how many vowels are present in the string.
'''str = input("enter a string:")
vowels = "aeiouAEIOU"
count = 0
for char in str:
    if char in vowels:
        count+=1

print(count)

'''
#5. Frequency of numbers:
# Given:
# numbers = [2, 3, 2, 5, 3, 2, 7, 5, 3]

# Find how many times each number occurs.
# Expected idea:
# 2 → 3
# 3 → 3
# 5 → 2
# 7 → 1

# Try doing this with a dictionary
'''numbers = [2, 3, 2, 5, 3, 2, 7, 5, 3]
 frequency = {}

for num in numbers:
   if num in frequency:
      frequency[num] +=1
    else:
        frequency[num] = 1

 print(frequency)'''

# Sum of digits
# Take an integer:
# 5832

# Output:
# 18

# Do it using a loop. Don't convert the number to a string.
'''num = 5832
sum_digit = 0

while num > 0:
    sum_digit += num % 10
    num //= 10
print("sum of digit: ",sum_digit)'''

# Count odd digits
# Given:
# number = 7283519


# Count how many digits are odd.
# Expected answer:
# 5

'''number = 7283519
count = 0

for digit in str(number):
    if int(digit) %2 != 0:
        count+=1

print("count of odd number:",count)'''

# Reverse a number
# Input:
# 12345

# Output:
# 54321

# Try using mathematical operations rather than string slicing.
'''number = 12345
reversed_num = 0

while number != 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number//=10
print("reversed number: ",reversed_num)


'''

# Check palindrome number
# Input:
# 1221

# Output:
# Palindrome

# Try using the reverse-number logic from Q3.


