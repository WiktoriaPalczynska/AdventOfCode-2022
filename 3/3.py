#AdventOfCode 2022-3

import string 

#Reading data from a file
with open("input.txt") as file:
    data = [line for line in file.read().strip().split('\n')]

#---------------------------PART_1--------------------------------

#Traversing every element in our data
total = 0
for item in data:
    #Find half line of data
    half = len(item)//2
    left = item[:half]
    right = item[half:]

    #Match the values ​​to the letters
    for priority, char in enumerate(string.ascii_letters):
        if char in left and char in right:
            total += priority + 1

#Sum of the priorities of those item types
print("Part 1: ", total)

#---------------------------PART_2--------------------------------

#The Elves are divided into groups of three
j = 3
prioritySum = 0
for i in range(0, len(data), 3):
    rucksack = data[i:j]
    j += 3 #Next three lines

    #Find the item type that corresponds to the badges of each three-Elf group
    for priority, char in enumerate(string.ascii_letters):
        if char in rucksack[0] and char in rucksack[1] and char in rucksack[2]:
            prioritySum += priority + 1

#Sum of the priorities of those item types
print("Part 2: ", prioritySum)