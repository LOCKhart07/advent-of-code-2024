"""AoC_Year2024_Day19_Part1"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"


with open(INPUT_PATH, "r") as f:
    while line := f.readline().strip():
        towels = [i.strip() for i in line.split(",")]

    # print(towels)

    designs = []
    while line := f.readline().strip():
        designs.append(line.strip())

    # print(designs)


def check_if_design_possible(design: str):
    # print(design)
    if design == "":
        return True

    is_design_possible = False
    for towel in towels:
        if design == towel:
            is_design_possible = True
        elif design.startswith(towel):
            is_design_possible = check_if_design_possible(
                design=design.removeprefix(towel)
            )

        if is_design_possible:
            break

    return is_design_possible


# designs = ["bwurrg"]
# possible_designs_counter = 0
# for design in designs:
#     # print(design, check_if_design_possible(design))
#     if check_if_design_possible(design):
#         possible_designs_counter += 1


print(sum([1 for design in designs if check_if_design_possible(design)]))
# print(possible_designs_counter)
