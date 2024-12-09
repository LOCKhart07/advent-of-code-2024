"""AoC_Year2024_Day9_Part2"""
INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"


with open(INPUT_PATH, "r") as f:
    line = f.read().strip()


# line = "0112233"

f_list = []
file_id = 0
for index, char in enumerate(line):
    if index % 2 == 0:
        f_list.append((file_id, int(char)))
        file_id += 1
    else:
        f_list.append((".", int(char)))


# print(f_list)
# print()

i = 0
j = len(f_list) - 1

final_list = f_list.copy()

# print("".join(str(tup[0]) * tup[1] for tup in final_list))


def find_index_in_list_of_tuples(l, element_to_find):
    for indi, f in enumerate(l):
        if f[0] == element_to_find:
            return indi


elements_added_counter = 0
for index, current_group in enumerate(f_list[::-1]):
    index = len(f_list) - index - 1
    current_group_char = current_group[0]
    current_group_len = current_group[1]
    if current_group_char != ".":

        for i in range(
            0, find_index_in_list_of_tuples(final_list, current_group_char) + 1
        ):
            dot_group = final_list[i]
            dot_group_char = dot_group[0]
            dot_group_len = dot_group[1]
            if final_list[i][0] != ".":
                continue

            if dot_group_len == current_group_len:
                final_list[find_index_in_list_of_tuples(final_list, current_group_char)] = (".", current_group_len)

                final_list[i] = current_group
                break
            elif dot_group_len > current_group_len:
                remaining = dot_group_len - current_group_len
                final_list[
                    find_index_in_list_of_tuples(final_list, current_group_char)
                ] = (".", current_group_len)
                final_list[i] = current_group
                final_list.insert(i + 1, (".", remaining))
                elements_added_counter += 1

                break


j = 0
checksum = 0
for tup in final_list:
    for _ in range(tup[1]):
        if tup[0] != ".":
            checksum += tup[0] * j
        j += 1

# print("".join(str(str(tup[0]) * tup[1]) for tup in f_list))
# print("".join(str(str(tup[0]) * tup[1]) for tup in final_list))

print(checksum)