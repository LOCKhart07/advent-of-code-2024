"""AoC_Year2024_Day20_Part2"""

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
current_picosecond = 0
visited[current_pos] = current_picosecond
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
            current_picosecond += 1
            visited[current_pos] = current_picosecond

            break


def get_manhattan_distance(a, b):
    ay, ax = a
    by, bx = b
    return abs(ay - by) + abs(ax - bx)


from collections import defaultdict

cheats = defaultdict(int)


visited_l = list(visited)

ccc = {}


CHEAT_THRESHOLD = 20
PICOSECONDS_THRESHOLD = 100

for i, a in enumerate(visited_l):
    for j, b in enumerate(visited_l[i + PICOSECONDS_THRESHOLD :]):
        # print("checking ", a, b)
        # by, bx = b
        picoseconds_used_to_cheat = get_manhattan_distance(a, b)
        if picoseconds_used_to_cheat <= CHEAT_THRESHOLD:

            time_saved = visited[b] - visited[a] - picoseconds_used_to_cheat
            if time_saved < PICOSECONDS_THRESHOLD:
                continue
            cheats[time_saved] += 1
            ccc[(a, b)] = time_saved
    # print(a, visited[a])


# print(len(cheats))
result = 0
for no_of_seconds in cheats:
    # print(cest)
    # print(cheat, cheats[cheat])
    # if no_of_seconds < 1:
    #     continue
    # print(
    #     f"There is {cheats[no_of_seconds]} cheat that saves {no_of_seconds} picoseconds."
    # )
    result += cheats[no_of_seconds]


print(result)

# print(result)
# for i, a in enumerate(visited):
#     for j, b in enumerate(visited[i]):
#         # print(visited[v], v)
#         print(visited)
# # print(t)


# for i in ccc:
#     print(i, ccc[i])
