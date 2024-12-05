import numpy as np
import re

with open("./day4/input.txt", "r") as f:
    input_lines = f.readlines()


matrix = []
padding_to_add = 4

for line in input_lines:
    matrix.append(
        ["." for i in range(padding_to_add)]
        + [c for c in line.strip()]
        + ["." for i in range(padding_to_add)]
    )

for i in range(padding_to_add):
    # matrix.append((["." for i in range(len(matrix[0]))]))
    # matrix.append((["." for i in range(len(matrix[0]))]))

    matrix = np.insert(matrix, 0, ["." for i in range(len(matrix[0]))], axis=0)
    matrix = np.insert(
        matrix, len(matrix), ["." for i in range(len(matrix[0]))], axis=0
    )

rows, cols = matrix.shape

for y in range(cols):
    line = ""
    for x in range(rows):
        line += " " + matrix[y, x]
        current_char = matrix[y, x]
    print(line)


xmas_counter = 0
for y in range(padding_to_add, cols - padding_to_add):
    line = ""
    for x in range(padding_to_add, rows - padding_to_add):
        line += matrix[y, x]
        current_char = matrix[y, x]
        if current_char == "A":
            lr_diagonal = matrix[y - 1, x - 1] + matrix[y, x] + matrix[y + 1, x + 1]
            rl_diagonal = matrix[y - 1, x + 1] + matrix[y, x] + matrix[y + 1, x - 1]
            if (lr_diagonal == "SAM" or lr_diagonal == "MAS") and (
                rl_diagonal == "SAM" or rl_diagonal == "MAS"
            ):
                xmas_counter += 1


print(xmas_counter)
