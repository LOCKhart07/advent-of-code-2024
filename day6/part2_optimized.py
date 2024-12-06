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


def check_if_valid_matrix(local_matrix, return_positions=False):

    guard_direction = Directions.UP
    guard_current_position = starting_position
    guard_positions_and_direction = set()
    guard_positions_and_direction.add(((1, 2), Directions.UP))
    while True:
        if (
            guard_current_position,
            guard_direction,
        ) in guard_positions_and_direction:
            return True
        guard_positions_and_direction.add(
            (
                guard_current_position,
                guard_direction,
            )
        )

        guard_next_position = (
            guard_current_position[0] + guard_direction[0],
            guard_current_position[1] + guard_direction[1],
        )
        if (
            guard_next_position[1] < 0
            or guard_next_position[0] < 0
            or guard_next_position[0] > len(local_matrix[0]) - 1
            or guard_next_position[1] > len(local_matrix) - 1
        ):
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
# print(positions_to_check)
for index, position_to_check in enumerate(positions_to_check):
    print(f"checking {index+1} position: {position_to_check}")
    local_matrix = deepcopy(matrix)
    local_matrix[position_to_check[1]][position_to_check[0]] = "#"
    if check_if_valid_matrix(local_matrix):
        valid_counter += 1


print(valid_counter)
