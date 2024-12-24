"""AoC_Year2024_Day23_Part1"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"

from collections import defaultdict


ad_g = defaultdict(list)
with open(INPUT_PATH, "r") as f:
    while line := f.readline().strip():
        a, b = line.split("-")
        ad_g[a].append(b)
        ad_g[b].append(a)


# for i in ad_g:
#     print(i, (ad_g[i]))


cycles = set()
for node in ad_g:
    for f_neighbor in ad_g[node]:  # Check first neighbor
        for s_neighbor in ad_g[f_neighbor]:  # Check neighbors' neighbors
            for t_neighbor in ad_g[s_neighbor]:  # Check neighbors' neighbors
                if t_neighbor == node:
                    # cycles.append([node, f_neighbor])
                    # print(node, f_neighbor, s_neighbor)
                    cycle = sorted([node, f_neighbor, s_neighbor])
                    cycles.add("-" + "-".join(cycle))


result = 0
for cycle in cycles:
    if "-t" in cycle:
        # print(cycle)
        result += 1

result
