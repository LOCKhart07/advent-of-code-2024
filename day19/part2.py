"""AoC_Year2024_Day19_Part2"""

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


design_memo = {}


def check_if_design_possible(design: str):
    if design in design_memo:
        return design_memo[design]

    # print(design)
    if design == "":
        raise ValueError

    designs_possible = 0
    for towel in towels:
        if design == towel:
            designs_possible += 1
        elif design.startswith(towel):

            designs_possible += check_if_design_possible(
                design=design.removeprefix(towel)
            )

    design_memo[design] = designs_possible
    return designs_possible


# designs = ["bwurrg"]
possible_designs_counter = 0
for design in designs:
    # print(design, check_if_design_possible(design))

    possible_designs_counter += check_if_design_possible(design)


# print(sum([1 for design in designs if check_if_design_possible(design)]))
print(possible_designs_counter)
