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


rules_freq_hm = {}

for rule in rules:
    n = rule[1]
    existing: list = rules_freq_hm.get(n, [])
    existing.append(rule[0])
    # existing.append(rule[0])
    rules_freq_hm[n] = existing


def comparison_func(a, b):
    if b in rules_freq_hm.get(a, []):
        return 1
    elif a in rules_freq_hm.get(b, []):
        return -1
    else:
        return 0


from functools import cmp_to_key


middle_sum = 0
for page in pages:
    sorte = sorted(page, key=cmp_to_key(comparison_func))
    a = sorte == page
    # print(f"{page}                     {sorte}            {a}")
    if not a:
        middle_sum += int(sorte[len(sorte) // 2])


print(middle_sum)
