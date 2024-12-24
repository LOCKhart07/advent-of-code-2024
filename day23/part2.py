"""AoC_Year2024_Day23_Part2"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"

from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt


graph = nx.Graph()

with open(INPUT_PATH, "r") as f:
    while line := f.readline().strip():
        a, b = line.split("-")
        graph.add_edge(a, b)


# pos = nx.spring_layout(graph)
# nx.draw_networkx(
#     graph, pos, with_labels=True, node_size=500,
# )
# plt.show()


maxi = []
for i in nx.find_cliques(graph):
    if len(i) > len(maxi):
        maxi = i


print(",".join(sorted(maxi)))

# for node in graph.nodes():
#     pass
#     print(node)
