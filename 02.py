#Day 01

with open('./02.txt') as my_input:
    input_lines = my_input.readlines()

replacements = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

def replace(letter):
    return int(letter.replace(letter, str(replacements[letter])))

rounds = [(replace(line.split()[0]), replace(line.split()[1])) for line in input_lines]

win = (0, 3, 1, 2)
lose = (0, 2, 3, 1)
draw = (0, 1, 2, 3)

#Part 1

total_score = 0
for opponent, me in rounds:
    if lose[opponent] == me:
        total_score += me + 6 #I won
    elif win[opponent] == me:
        total_score += me     #I lost
    else:
        total_score += me + 3 #draw

print(total_score)

#Part 2

total_score = 0
for opponent, result in rounds:
    if result == 3:
        total_score += lose[opponent] + 6 #I won
    elif result == 1:
        total_score += win[opponent]      #I lost
    else:
        total_score += opponent + 3       #draw

print(total_score)