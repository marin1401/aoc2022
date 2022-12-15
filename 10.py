#Day 10

with open('./10.txt') as my_input:
    input_lines = my_input.read().splitlines()

instructions = [line.split() for line in input_lines]

#Part 1

def cycle_update(x):
    values.append(x)
    if not (len(values)-20) % 40:
        strengths.append(len(values) * x)

x = 1
values = [x]
strengths = []
for instruction in instructions:
    if instruction[0] == 'noop':
        cycle_update(x)
    else:
        cycle_update(x)
        x += int(instruction[1])
        cycle_update(x)

print(sum(strengths))

#Part 2

position = 0
crt_row = ''
for value in values:
    sprite = range(value-1, value+2)
    pixel = '#' if position in sprite else '.'
    crt_row += pixel
    position += 1
    if not position % 40:
        print(crt_row)
        crt_row = ''
        position = 0