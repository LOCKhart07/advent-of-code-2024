with open("day5/input.txt") as f:
    rules = []
    while True:
        line = f.readline()
        if line == "\n":
            break
        rules.append(tuple(line.strip().split("|")))

    pages = []
    while True:
        line = f.readline()
        if line == "":
            break
        pages.append(line.strip().split(","))


def get_permutations(page):
    permutations = set()
    for i in range(len(page)):
        for j in range(i + 1, len(page)):
            # print(f"{page[i]},{page[j]}")
            permutations.add(
                (
                    page[i],
                    page[j],
                )
            )
    return permutations


middle_sum = 0
for page in pages:
    permutations = get_permutations(page)

    for perm in permutations:
        if perm[::-1] in rules:
            break
    else:
        middle_sum += int(page[len(page) // 2])


print(middle_sum)
