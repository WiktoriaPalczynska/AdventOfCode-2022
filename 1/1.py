#AdventOfCode 2022-1

#Reading data from a file
with open("input.txt") as file:
    data = [line for line in file.read().strip().split('\n')]

#Traversing every element in our data
calories = []
add = 0
for item in data:
    if item == '':
        add = 0
    else:
        #Calories carried by each elf
        num = int(item)
        add += num
        calories.append(add)

#The most calories
print(max(calories))

