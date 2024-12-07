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

matrix_rows = len(matrix[0])
matrix_cols = len(matrix)


def check_if_valid_matrix(local_matrix, return_positions=False):

    guard_direction = Directions.UP
    guard_current_position = starting_position
    guard_positions_and_direction = set()
    guard_positions_and_direction.add(((0, 0), Directions.UP))

    while True:
        if return_positions:
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
            or guard_next_position[0] > matrix_rows - 1
            or guard_next_position[1] > matrix_cols - 1
        ):
            break
        elif local_matrix[guard_next_position[1]][guard_next_position[0]] == "#":
            if not return_positions:
                if (
                    guard_current_position,
                    guard_direction,
                ) in guard_positions_and_direction:
                    return True
                else:
                    guard_positions_and_direction.add(
                        (
                            guard_current_position,
                            guard_direction,
                        )
                    )
            guard_direction = direction_change_hashmap[guard_direction]

            continue
        else:
            guard_current_position = guard_next_position

    if return_positions:
        return [i[0] for i in guard_positions_and_direction]
    return False


valid_counter = 0
all_p_c = check_if_valid_matrix(matrix, return_positions=True)
positions_to_check = set(all_p_c)
for index, position_to_check in enumerate(positions_to_check):
    matrix[position_to_check[1]][position_to_check[0]] = "#"
    if check_if_valid_matrix(matrix):
        valid_counter += 1
    matrix[position_to_check[1]][position_to_check[0]] = "."

print(valid_counter)