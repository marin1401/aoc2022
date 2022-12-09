#Day 07

with open('./07.txt') as my_input:
    input_lines = my_input.read().splitlines()

filesystem = {'/': []}
previous_dir = ['']
directory = '/'
for line in input_lines[1:]:
    st, nd, *_ = line.split()
    if st == '$':
        if nd == 'cd':
            go_to, = _
            if go_to == '..':
                previous_dir.pop()
            else:
                directory = previous_dir[-1]+'/'+go_to
                previous_dir.append(directory)
                filesystem[directory] = []
    elif st == 'dir':
        filesystem[directory].append([previous_dir[-1]+'/'+nd, st, 0])
    else:
        filesystem[directory].append([nd, 'file', int(st)])

zero_dir = True
while zero_dir:
    dir_sizes = []
    for d, ls in filesystem.items():
        total = 0
        zero_dir = False
        for *_, size in ls:
            if size:
                total += size
            else:
                zero_dir = True
                break
        if not zero_dir:
            dir_sizes.append((d, total))
    for directory, size in dir_sizes:
        for d, ls in filesystem.items():
            for i in range(len(ls)):
                if directory == filesystem[d][i][0]:
                    filesystem[d][i][2] = size
    total_space = 0
    zero_dir = False
    for *_, size in filesystem['/']:
        if size:
            total_space += size
        else:
            zero_dir = True
            break

#Part 1

max_size = 100000

total = 0
for k, ls in filesystem.items():
    for _, item, size in ls:
        if item == 'dir' and size <= max_size:
            total += size

print(total)

#Part 2

space_needed = total_space - 40000000

candidates_for_deletion = set()
for k, ls in filesystem.items():
    for _, item, size in ls:
        if item == 'dir':
            if size > space_needed:
                candidates_for_deletion.add(size)

print(min(candidates_for_deletion))