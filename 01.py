#Day 01

with open('./01.txt') as my_input:
    input_lines = my_input.readlines()

all_calories = [line.strip() for line in input_lines]

calories_per_elf = [0]
for calorie in all_calories:
    if calorie:
        calories_per_elf[-1] += int(calorie)
    else:
        calories_per_elf.append(0)

#Part 1

print(max(calories_per_elf))

#Part 2

print(sum(sorted(calories_per_elf)[-3:]))
