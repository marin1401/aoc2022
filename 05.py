#Day 05

with open('./05.txt') as my_input:
    input_lines = my_input.read().splitlines()

for line in input_lines:
    if line[1] == '1':
        stacks_row = input_lines.index(line)
        row_length = len(line)
        break

starting_stacks = []
for space in range(1, row_length, 4):
    stack = []
    for row in reversed(range(stacks_row)):
        crate = input_lines[row][space].strip()
        if crate:
            stack.append(crate)
    starting_stacks.append(stack)

procedure = [tuple(map(int, line.split()[1::2]))
            for line in input_lines[stacks_row+2:]]

def crate_mover(model):
    stacks = [[crate for crate in stack] for stack in starting_stacks]
    for quantity, sender, recipient in procedure:
        stack = []
        for _ in range(quantity):
            stack.append(stacks[sender-1].pop())
        if model == 9000:
            for crate in stack:
                stacks[recipient-1].append(crate)
        elif model == 9001:
            for crate in reversed(stack):
                stacks[recipient-1].append(crate)
    return ''.join(stack[-1] for stack in stacks)

#Part 1

print(crate_mover(9000))

#Part 2

print(crate_mover(9001))