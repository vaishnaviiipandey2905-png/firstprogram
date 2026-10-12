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
