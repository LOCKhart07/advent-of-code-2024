"""AoC_Year2024_Day10_Part2"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"

import numpy as np

grid = []

with open(INPUT_PATH, "r") as f:
    while line := f.readline().strip():
        grid.append(list(map(int, line)))


grid = np.array(grid)

rows, cols = grid.shape


def check_bounds(pos):
    if pos[1] < 0 or pos[0] < 0 or pos[0] > rows - 1 or pos[1] > cols - 1:
        return False
    return True


class Directions:
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def check_if_incrementing(pos, value):
    if value + 1 == grid[pos]:
        return True

    return False


def find_paths(current_pos, visited_nines: list):
    # print(current_pos, "  ", grid[current_pos])

    if grid[current_pos] == 9:
        visited_nines.append(current_pos)
        return 1
    valid_path = 0
    for direction in DIRECTIONS:
        next_pos = tuple(a + b for a, b in zip(current_pos, direction))
        if check_bounds(next_pos) and check_if_incrementing(
            next_pos, grid[current_pos]
        ):
            valid_path += find_paths(next_pos, visited_nines)

    return valid_path


# print('\n'.join(str(row) for row in grid))
# print(grid)
# print(grid[(0, 3)])
# print(check_bounds((-1,4)))

vali = 0
for x in range(rows):
    for y in range(cols):
        if grid[x, y] == 0:
            # print(grid[x, y])
            vali += find_paths((x, y), [])

print(vali)
# find_paths((0, 3), [])
