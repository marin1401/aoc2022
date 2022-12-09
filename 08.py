#Day 08

with open('./08.txt') as my_input:
    input_lines = my_input.read().splitlines()

forest = [[int(tree) for tree in row] for row in input_lines]
size = len(forest)
edge_trees = 4*(size - 1)

def transpose(array_2d):
    return list(map(list, zip(*array_2d)))

def visibilities_and_scores(grid):
    visibilities, scores = [], []
    for row in grid[1:-1]:
        row_visibility, row_score = [], []
        for tree in range(1, len(row)-1):
            score_left, score_right = 0, 0
            if row[tree] > max(row[:tree]) or row[tree] > max(row[tree+1:]):
                visibility = 1
            else:
                visibility = 0
            for next_tree in reversed(row[:tree]):
                score_left += 1
                if row[tree] <= next_tree:
                    break
            for next_tree in row[tree+1:]:
                score_right += 1
                if row[tree] <= next_tree:
                    break
            row_visibility.append(visibility)
            row_score.append(score_left * score_right)
        visibilities.append(row_visibility)
        scores.append(row_score)
    return visibilities, scores

row_visibilities, row_scores = visibilities_and_scores(forest)
column_visibilities, column_scores = visibilities_and_scores(transpose(forest))

#Part 1

visible_trees = edge_trees
for row, column in zip(row_visibilities, transpose(column_visibilities)):
    for row_tree, column_tree in zip(row, column):
        if row_tree or column_tree:
            visible_trees += 1

print(visible_trees)

#Part 2

scenic_scores = set()
for row, column in zip(row_scores, transpose(column_scores)):
    for row_score, column_score in zip(row, column):
        scenic_scores.add(row_score * column_score)

print(max(scenic_scores))