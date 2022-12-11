#AdventOfCode 2022-4

#Reading data from a file
with open("input.txt") as file:
    data = [line for line in file.read().strip().split('\n')]

#-------------------------------------------PART_1------------------------------------------------

#Function that find ranges that completely envelop the other range
def rangeA_in_rangeB(range_a, range_b):
    start_a, end_a = map(int, range_a.split('-'))
    start_b, end_b = map(int, range_b.split('-'))
    return start_a >= start_b and end_a <= end_b

#Traversing every element in our data
summ_range = 0 #Range fully contain the other range
for pair in data:
    first_range, second_range = pair.split(',')
    if rangeA_in_rangeB(first_range,second_range) or rangeA_in_rangeB(second_range,first_range):
        summ_range += 1

#In how many assignment pairs does one range fully contain the other?
print("Part 1:",summ_range)

#-------------------------------------------PART_2------------------------------------------------

#Traversing every element in our data
pair_overlap = 0 #Pairs that overlap at all
for pair in data:
    first_range, second_range = pair.split(',')
    start_a, end_a = map(int, first_range.split('-'))
    start_b, end_b = map(int, second_range.split('-'))
    if start_a in range(start_b,end_b+1) or end_a in range(start_b,end_b+1) or start_b in range(start_a,end_a+1) or end_b in range(start_a,end_a+1):
        pair_overlap += 1
        
#In how many assignment pairs do the ranges overlap?
print("Part 2:",pair_overlap)