#Day 01

import string

with open('./03.txt') as my_input:
    input_lines = my_input.readlines()

def priority(a_list):
    return sum(string.ascii_letters.index(char) + 1 for char in a_list)

#Part 1

common_chars = [next(iter(set(line[:len(line)//2]) & set(line[len(line)//2:]))) for line in input_lines]

print(priority(common_chars))

#Part 2

badges = [next(iter(set(line_1.strip()) & set(line_2.strip()) & set(line_3.strip()))) for line_1, line_2, line_3 in zip(input_lines[::3], input_lines[1::3], input_lines[2::3])]

print(priority(badges))