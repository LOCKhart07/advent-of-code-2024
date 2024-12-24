'''AoC_Year2024_Day24_Part1'''



INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"
EXAMPLE2_INPUT_PATH = "example2.txt"

from collections import defaultdict
import re


graph = nx.DiGraph()


wires = {}

PATTERN = r"(\w+) (\w+) (\w+) -> (\w+)"


to_process = []
with open(INPUT_PATH, "r") as f:
    while line := f.readline().strip():
        name, value = line.split(": ")
        wires[name] = int(value), "EXACT", int(value)
        # print()

    while line := f.readline().strip():
        # name, value = line.split(": ")
        # wires[name] = int(value)
        # print(line, re.findall(PATTERN, line))
        a, gate, b, c = re.findall(PATTERN, line)[0]
        # print(a, gate, b, c)
        wires[c] = (a, gate, b)
        # print(a, gate, b, c)


def get_value(wire):
    a, gate, b = wires[wire]

    if gate == "AND":
        return int(get_value(a) and get_value(b))
    elif gate == "OR":
        return int(get_value(a) or get_value(b))
    elif gate == "XOR":
        return int(get_value(a) != get_value(b))
    else:
        return int(a)


output = []

for wire in wires:
    wire: str

    if wire.startswith("z"):
        # print(wire, wires[wire], get_value(wire))

        output.append((wire, get_value(wire)))

# print(wires)
# for i in sorted(output, key=lambda x: x[0]):
#     print(i)

binary = "".join([str(j) for i, j in sorted(output, key=lambda x: x[0], reverse=True)])
# print(binary)
# print("0011111101000")
print(int(binary, 2))
