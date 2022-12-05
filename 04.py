#Day 01

with open('./04.txt') as my_input:
    input_lines = my_input.readlines()

pairs = [line.strip().split(',') for line in input_lines]

full_overlap, any_overlap = 0, 0
for pair in pairs:
    limits = [list(map(int, elf.split('-'))) for elf in pair]
    ranges = [set(range(limit[0], limit[1]+1)) for limit in limits]
    overlap = ranges[0] & ranges[1]
    if overlap in ranges:
        full_overlap += 1
    if overlap:
        any_overlap += 1

#Part 1

print(full_overlap)

#Part 2

print(any_overlap)