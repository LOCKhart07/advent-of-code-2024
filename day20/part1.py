"""AoC_Year2024_Day20_Part1"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"


with open(INPUT_PATH, "r") as f:
    input_lines = f.readlines()


matrix = []
for line in input_lines:
    matrix.append([c for c in line.strip()])

import numpy as np

matrix = np.array(matrix)

rows, cols = matrix.shape

# print(matrix)
for y in range(cols):
    for x in range(rows):
        # print(x, y)
        char = matrix[y, x]
        if char == "S":
            start = (y, x)
        elif char == "E":
            end = (y, x)


# print(start, end)
# print(matrix[start], start)


directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def check_in_bounds(pos):
    y, x = pos
    if x < 0 or y < 0 or x > rows - 1 or y > cols - 1:
        return False
    return True


current_pos = start

visited = dict()
current_node_number = 0
visited[current_pos] = current_node_number
while True:
    # print(current_pos, matrix[current_pos])
    if matrix[current_pos] == "E":
        break

    for direction in directions:
        new_position = (current_pos[0] + direction[0], current_pos[1] + direction[1])
        if not check_in_bounds(new_position):
            continue
        if new_position in visited:
            continue
        if matrix[new_position] == "." or matrix[new_position] == "E":
            current_pos = new_position
            current_node_number += 1
            visited[current_pos] = current_node_number

            break


# print(matrix[1, 14], cols)

positions_to_check = [
    (-2, 0),
    (2, 0),
    (2, 0),
    (-2, 0),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]

shortcuts = {}

for current_pos in visited:
    y, x = current_pos
    # print(current_pos, matrix[current_pos], visited[current_pos])

    # right
    hash_pos = (y, x + 1)
    hy, hx = hash_pos
    if check_in_bounds(hash_pos) and matrix[hash_pos] == "#":
        f_pos = hy - 1, hx
        s_pos = hy, hx + 1
        t_pos = hy + 1, hx
        for p in [f_pos, s_pos, t_pos]:
            if check_in_bounds(p) and (matrix[p] == "." or matrix[p] == "E"):
                if (hash_pos, p) not in shortcuts:
                    shortcuts[(hash_pos, p)] = visited[p] - visited[current_pos] - 2
    # left
    hash_pos = (y, x - 1)
    hy, hx = hash_pos
    if check_in_bounds(hash_pos) and matrix[hash_pos] == "#":
        f_pos = hy - 1, hx
        s_pos = hy, hx - 1
        t_pos = hy + 1, hx
        for p in [f_pos, s_pos, t_pos]:
            if check_in_bounds(p) and (matrix[p] == "." or matrix[p] == "E"):
                if (hash_pos, p) not in shortcuts:
                    shortcuts[(hash_pos, p)] = visited[p] - visited[current_pos] - 2

    # up
    hash_pos = (y - 1, x)
    hy, hx = hash_pos
    if check_in_bounds(hash_pos) and matrix[hash_pos] == "#":
        f_pos = hy, hx - 1
        s_pos = hy - 1, hx
        t_pos = hy, hx + 1
        for p in [f_pos, s_pos, t_pos]:
            if check_in_bounds(p) and (matrix[p] == "." or matrix[p] == "E"):
                if (hash_pos, p) not in shortcuts:
                    shortcuts[(hash_pos, p)] = visited[p] - visited[current_pos] - 2

    # down
    hash_pos = (y + 1, x)
    hy, hx = hash_pos
    if check_in_bounds(hash_pos) and matrix[hash_pos] == "#":
        f_pos = hy, hx - 1
        s_pos = hy + 1, hx
        t_pos = hy, hx + 1
        for p in [f_pos, s_pos, t_pos]:
            if check_in_bounds(p) and (matrix[p] == "." or matrix[p] == "E"):
                if (hash_pos, p) not in shortcuts:
                    shortcuts[(hash_pos, p)] = visited[p] - visited[current_pos] - 2

from collections import defaultdict

len_dict = defaultdict(int)

for shortcut in shortcuts:
    if shortcuts[shortcut] > 0:
        len_dict[shortcuts[shortcut]] += 1

result = 0
for l in len_dict:
    if l >= 100:
        result += len_dict[l]


print(result)
