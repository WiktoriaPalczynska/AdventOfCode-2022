#AdventOfCode 2022-2

#Reading data from a file
with open("input.txt") as file:
    data = [line for line in file.read().strip().split('\n')]

#A,X - Rock, B,Y - Paper, C,Z - Scissors
#Rock - 1, Paper - 2, Scissors - 3
# 0 - defeat, 3 - draw, 6 - win
#Traversing every element in our data
points = 0
for item in data:
    if item == 'A X':
        points += 4
    elif item == 'A Y':
        points += 8
    elif item == 'A Z':
        points += 3
    elif item == 'B X':
        points += 1
    elif item == 'B Y':
        points += 5
    elif item == 'B Z':
        points += 9
    elif item == 'C X':
        points += 7
    elif item == 'C Y':
        points += 2
    elif item == 'C Z':
        points += 6

#Total score
print(points)

