import numpy as np
import re

with open("./day4/input.txt", "r") as f:
    input_lines = f.readlines()


matrix = []
for line in input_lines:
    matrix.append([c for c in line.strip()])


for row in matrix:
    print(row)

cols = len(matrix)
rows = len(matrix[0])


horizontal_lines = []
for y in range(0, cols):
    conc_str = ""
    for x in range(0, rows):
        current_letter = matrix[y][x]
        conc_str += current_letter
    horizontal_lines.append(conc_str)


vertical_lines = []
for y in range(0, cols):
    conc_str = ""
    for x in range(0, rows):
        current_letter = matrix[x][y]
        conc_str += current_letter
    vertical_lines.append(conc_str)
# print(vertical_lines)


lr_diagonal_lines = []


rl_diagonal_lines = []

for i in range(0 - rows + 1, 0 + rows):
    lr_diagonal_lines.append("".join(np.diag(matrix, k=i)))


for i in range(0 - rows + 1, 0 + rows):
    rl_diagonal_lines.append("".join(np.diag(np.fliplr(matrix), k=i)))


total_lines = horizontal_lines + vertical_lines + lr_diagonal_lines + rl_diagonal_lines

r_str = "XMAS"

xmas_counter = 0
for line in total_lines:
    print(line)
    matches = re.findall(r_str, line) + re.findall(r_str[::-1], line)
    print(matches)
    print()
    xmas_counter += len(matches)


print(xmas_counter)


# for i in vertical_lines:
#     print(i)

# print()

# for i in horizontal_lines:
#     print(i)

# print()
# for i in lr_diagonal_lines:
#     print(i)

# print()
# for i in rl_diagonal_lines:
#     print(i)

# print()
