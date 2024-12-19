"""AoC_Year2024_Day12_Part1"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"
import numpy as np

with open(INPUT_PATH, "r") as f:

    input_lines = f.readlines()


matrix = []
for index, line in enumerate(input_lines):
    line_as_list = [c for c in line.strip()]
    try:
        starting_position = (line_as_list.index("^"), index)
    except Exception as e:
        pass
    matrix.append(line_as_list)

matrix = np.array(matrix)
# print(matrix)


from collections import defaultdict

rows, cols = matrix.shape


def check_bounds(pos):
    if pos[1] < 0 or pos[0] < 0 or pos[0] > rows - 1 or pos[1] > cols - 1:
        return False
    return True


DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


visited_plants = set()
regions = defaultdict(list)
region_id = 0


def add_to_region(plant_coords, current_plant):
    if matrix[plant_coords] == current_plant:
        if plant_coords in visited_plants:
            return (0, 0, True)

        regions[str(region_id) + "|" + current_plant].append(plant_coords)
        visited_plants.add(plant_coords)

        perimeter = 4
        area = 1
        for direction in DIRECTIONS:
            next_pos = tuple(a + b for a, b in zip(plant_coords, direction))
            if check_bounds(next_pos):

                uska_perimiter, uska_area, is_same_plant = add_to_region(
                    next_pos, current_plant
                )

                if is_same_plant:
                    area += uska_area
                    perimeter = perimeter + uska_perimiter - 1
                # area = area + uska_area
            # else:
            #     perimeter
        return (perimeter, area, True)
    else:
        return (0, 0, False)


# def calculate_price(plant_coords):
#     if plant_coords in visited_plants:
#         return 0

#     perimeter = 0
#     for direction in DIRECTIONS:
#         next_pos = tuple(a + b for a, b in zip(plant_coords, direction))
#         if not check_bounds(next_pos):
#             perimeter += 1
#             continue

#         calculate_price(next_pos)


cost = 0
for x in range(cols):
    for y in range(rows):
        plant = matrix[x, y]
        # print(plant)
        bruh = add_to_region((x, y), plant)
        # if bruh[1] != 0:
        #     print(str(region_id) + "|" + plant, bruh)
        cost += bruh[0] * bruh[1]
        region_id += 1

# regions
print(cost)
