"""AoC_Year2024_Day9_Part1"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"


with open(INPUT_PATH, "r") as f:
    line = f.read().strip()

# print(line)


f_list = []


file_id = 0
for index, char in enumerate(line):
    if index % 2 == 0:
        f_list += [file_id for _ in range(int(char))]
        file_id += 1
    else:
        f_list += ["." for _ in range(int(char))]


# print(f_str)

# print("".join([str(i) for i in f_list]))
# print(f_list)
# print()
i = 0
j = len(f_list) - 1


while i < j:
    if f_list[i] != ".":
        i += 1
        continue
    if f_list[j] == ".":
        j -= 1
        continue

    f_list[i] = f_list[j]
    f_list[j] = "."

    # print("".join([str(i) for i in f_list]))
    i += 1
    j -= 1

checksum = 0
for index, char in enumerate(f_list):
    if char == ".":
        break

    checksum += int(char) * index


print(checksum)
