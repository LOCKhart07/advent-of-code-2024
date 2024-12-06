import numpy as np
import re

with open("./day6/input.txt", "r") as f:

    input_lines = f.readlines()


matrix = []
for index, line in enumerate(input_lines):
    line_as_list = [c for c in line.strip()]
    try:
        starting_position = (line_as_list.index("^"), index)
    except Exception as e:
        pass
    matrix.append(line_as_list)


# print(starting_position)
def print_matrix(local_matrix):
    for row in local_matrix:
        print(" ".join(row))


# print_matrix(matrix)
print()


class Directions:
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


direction_change_hashmap = {
    Directions.UP: Directions.RIGHT,
    Directions.RIGHT: Directions.DOWN,
    Directions.DOWN: Directions.LEFT,
    Directions.LEFT: Directions.UP,
}

arrow_direction_symbol_hashmap = {
    Directions.UP: "^",
    Directions.RIGHT: ">",
    Directions.DOWN: "v",
    Directions.LEFT: "<",
}
guard_direction = Directions.UP

guard_current_position = starting_position

# guard_positions = [starting_position]
guard_positions = [guard_current_position]
while True:
    if guard_current_position != guard_positions[-1]:
        guard_positions.append(guard_current_position)
    matrix[guard_current_position[1]][guard_current_position[0]] = (
        arrow_direction_symbol_hashmap[guard_direction]
    )
    # print_matrix(matrix)

    # guard_current_position = guard_positions[-1]
    guard_next_position = tuple(
        a + b for a, b in zip(guard_current_position, guard_direction)
    )
    if (
        guard_next_position[1] < 0
        or guard_next_position[0] < 0
        or guard_next_position[0] > len(matrix[0]) - 1
        or guard_next_position[1] > len(matrix) - 1
    ):
        print("Going out of bounds")
        break
    elif matrix[guard_next_position[1]][guard_next_position[0]] == "#":
        guard_direction = direction_change_hashmap[guard_direction]
        continue
    else:
        matrix[guard_current_position[1]][guard_current_position[0]] = "X"
        guard_current_position = guard_next_position

    # print_matrix(matrix)
    # print()

print(len(set(guard_positions)))
# print(guard_positions)
# print_matrix(matrix)
