from functools import reduce


def count_trees(right_move, down_move):
    position = 0
    trees = 0
    for line in puzzle[::down_move]:
        if len(line) - 1 < position:
            position -= len(line)
        if line[position] == '#':
            trees += 1
        position += right_move
    return trees


with open('data_day_3.txt', 'r') as data:
    puzzle = data.read().splitlines()

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = []
for slope in slopes:
    trees.append(count_trees(*slope))
print(trees[1])
print(reduce(lambda x, y: x * y, trees))
