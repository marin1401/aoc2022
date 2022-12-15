#Day 09

with open('./09.txt') as my_input:
    input_lines = my_input.read().splitlines()

motions = [(line[0], int(line[2:])) for line in input_lines]

head = [(0, 0)]
for direction, steps in motions:
    for step in range(steps):
        xh, yh = head[-1]
        xh = xh + 1 if direction == 'R' else xh
        xh = xh - 1 if direction == 'L' else xh
        yh = yh + 1 if direction == 'U' else yh
        yh = yh - 1 if direction == 'D' else yh
        head.append((xh, yh))

def knots(next_knot, knot, n):
    for (xp, yp), (xc, yc) in zip(knot, knot[1:]):
        xn, yn = next_knot[-1]
        dx = xc - xp
        dy = yc - yp
        x_dist = abs(xc-xn)
        y_dist = abs(yc-yn)
        if x_dist == 2 and not y_dist:
            next_knot.append((xn + dx, yn))
        elif not x_dist and y_dist == 2:
            next_knot.append((xn, yn + dy))
        elif x_dist == 2 and y_dist == 1:
            next_knot.append((xn + dx, yc))
        elif x_dist == 1 and y_dist == 2:
            next_knot.append((xc, yn + dy))
        elif x_dist == 2 and y_dist == 2:
            next_knot.append((xp, yp))
    n -= 1
    knots([(0, 0)], next_knot, n) if n else print(len(set(next_knot)))

#Part 1

knots([(0, 0)], head, 1)

#Part 2

knots([(0, 0)], head, 9)