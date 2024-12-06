from copy import deepcopy

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


def check_if_valid_matrix(l_matrix, return_positions=False):
    local_matrix = l_matrix
    guard_direction = Directions.UP
    guard_current_position = starting_position
    guard_positions_and_direction = [((1, 2), Directions.UP)]
    while True:
        if (
            guard_current_position,
            guard_direction,
        ) in guard_positions_and_direction:
            # print(guard_positions_and_direction)
            # print(
            #     (
            #         guard_current_position,
            #         guard_direction,
            #     )
            # )
            # print_matrix(local_matrix)

            # print("\n\n\n\n")
            return True
        if (
            guard_current_position,
            guard_direction,
        ) != guard_positions_and_direction[-1]:
            guard_positions_and_direction.append(
                (guard_current_position, guard_direction)
            )
        # local_matrix[guard_current_position[1]][guard_current_position[0]] = (
        #     arrow_direction_symbol_hashmap[guard_direction]
        # )
        # print_matrix(matrix)

        # guard_current_position = guard_positions[-1]
        guard_next_position = tuple(
            a + b for a, b in zip(guard_current_position, guard_direction)
        )
        if (
            guard_next_position[1] < 0
            or guard_next_position[0] < 0
            or guard_next_position[0] > len(local_matrix[0]) - 1
            or guard_next_position[1] > len(local_matrix) - 1
        ):
            # print("Going out of bounds")
            break
        elif local_matrix[guard_next_position[1]][guard_next_position[0]] == "#":
            guard_direction = direction_change_hashmap[guard_direction]
            continue
        else:
            # local_matrix[guard_current_position[1]][guard_current_position[0]] = "X"
            guard_current_position = guard_next_position

    if return_positions:
        return [i[0] for i in guard_positions_and_direction]
    return False
    # print_matrix(matrix)
    # print()


# print(len(set(guard_positions)))
# print(guard_positions)
# print_matrix(matrix)

valid_counter = 0

positions_to_check = set(check_if_valid_matrix(deepcopy(matrix), return_positions=True))
print(f"Have to check {len(positions_to_check)} positions")
for index, position_to_check in enumerate(positions_to_check):
    print(f"checking {index+1} postion")
    local_matrix = deepcopy(matrix)
    local_matrix[position_to_check[1]][position_to_check[0]] = "#"
    if check_if_valid_matrix(local_matrix):
        valid_counter += 1

# for y in range(len(matrix)):
#     for x in range(len(matrix[0])):
#         if matrix[y][x] != "#":
#             local_matrix = deepcopy(matrix)
#             local_matrix[y][x] = "#"
#             # print_matrix(matrix)
#             # print()
#             # print_matrix(local_matrix)
#             # print(matrix[0])
#             # print(local_matrix[0])

#             # print("\n\n\n\n")
#             if check_if_valid_matrix(local_matrix):
#                 valid_counter += 1
# raise SystemExit("Stop right there!")


print(valid_counter)
