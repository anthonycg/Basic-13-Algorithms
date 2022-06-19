def replaceNegWithString(array):
    for x in range(len(array)):
        if array[x] < 0:
            array[x] = 'Negative'
    print(array)

replaceNegWithString([-1,-2,3,4,12])


# 1.
# Print 1-255 Write a program that would print all the numbers from 1 to 255.
# Solution:
i = 0
while i < 256:
    print(i)
i += 1

# 2.
# Print odd numbers between 1-255 Write a program that would print all the odd numbers from 1 to 255.

# Solution:
i = 0
while i < 256:
    if i % 2 != 0:
        print(i)
i += 1

# 3.
# Print the sum of all numbers from 1 to 255.5.
# Solution:
i = 0
sum = 0
while i < 256:
    sum += i
i += 1
print(sum)

# 4.
# Given an array, Example: [1,3,5,7,9,13], write a program that would iterate through each member of the array and print each value.

# Solution:
array = [1,3,5,7,9,13]
for num in array:
    print(num)

# 5.
# Write a program that takes any array and prints the maximum value in the array.
# Solution:
array = [1,3,5,16,9,13]
maxValue = array[0]
for num in range(1,len(array)):
    if array[num] > maxValue:
        maxValue = array[num]
print(maxValue)

# 6.
# Write a program that takes an array, and prints the AVERAGE of the values in the array. For example for an array [2, 10, 3], your program should print an average of 5.
array = [2, 10, 3]
# Solution:
sum = 0
for num in range(len(array)):
    sum += array[num]
avg = sum/len(array)
print(avg)

# 7.
# Write a program that creates an array that contains all the even numbers between 1 to 255.
# Solution:
array = []
i = 0
while i < 256:
    if i % 2 == 0:
        array.append(i)
vi += 1
print(array)

# 8.
# Write a program that takes an array and a number 'y' and returns the values in the array that are greater than a given 'y'.
# Solution:
def valuesGreaterThan(array, y):
    for x in array:
        if x > y:
            print(x)
valuesGreaterThan([2,2,8,4,1,78], 3)

# 9.
# Given any array x, say [1, 5, 10, -2], create an algorithm that squares each value in the array. Output: [1, 25, 100, 4].
# Solution:
arraySquared = []
def squareValues(array):
    for x in array:
        arraySquared.append(x*x)
    print(arraySquared)
squareValues([2,2,8,4,1,78])

# 10.
# Given any array x, say [1, 5, 10, -2], create an algorithm that replaces any negative number with the value of 0.
# Solution:
updatedArray = []
def replaceNeg(array):
    for x in array:
        if x < 0:
            x = 0
updatedArray.append(x)
print(updatedArray)
replaceNeg([2,-2,8,4,1,-78])

# 11.
# Given any array x, say [1, 5, 10, -2], create an algorithm that returns a hash with the maximum value, the minimum value, and the average of all values in the array.
# Solution:
values = {"min": 0, "max": 0, "avg": 0}
def minMaxAvg(array):
    sum =  0
    for x in array:
        if x < values["min"]:
            values["min"] = x
        if x > values["max"]:
            values["max"] = x
        sum += x
    values["avg"] = sum/len(array)
print(values)
minMaxAvg([1, 5, 10, -2])

# 12. 
# Given any array x, say [1, 5, 10, 7, -2], create an algorithm that shifts each number by one to the front. For example, when the program is done, the array [1, 5, 10, 7, -2] should become [5, 10, 7, -2, 0].
# Solution:
def minMaxAvg(array):
    for x in range(1, len(array)):
        array[x-1] = array[x]
    array[len(array)-1] = 0
    print(array)
minMaxAvg([1, 5, 10, 7, -2])

# 13.
# Write a program that takes an array of numbers and replaces any negative number with the string 'Negative'. For example, if array x is initially [-1, -3, 2] after your program is done that array should be ['Negative', 'Negative', 2].
# Solution:
def replaceNegWithString(array):
    for x in range(len(array)):
        if array[x] < 0:
            array[x] = 'Negative'
print(array)
replaceNegWithString([-1,-2,3,4,12])