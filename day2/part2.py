with open("../day2/input.txt", "r") as f:
    levels = f.readlines()


def is_safe(l: list):
    a_reports = sorted(l)
    if a_reports == l:
        diffs = [l[n] - l[n - 1] for n in range(1, len(l))]
        # print(diffs)
        for diff in diffs:
            if diff < 1 or diff > 3:
                break
        else:
            # print("safe")
            return True
        return False

    d_reports = sorted(l, reverse=True)
    if d_reports == l:
        diffs = [l[n - 1] - l[n] for n in range(1, len(l))]
        # print(diffs)
        for diff in diffs:
            if diff < 1 or diff > 3:
                break
        else:
            # print("safe")
            return True
        return False

    return False


safe_counter = 0
for i in levels:
    # print("--------------------------------------------------------")
    reports = [int(x) for x in i.split()]
    # print(reports)

    if is_safe(reports):
        safe_counter += 1
        continue

    # Brute force each combination to check if safe
    for i in range(0, len(reports)):
        temp_l = reports[:i] + reports[i + 1 :]
        # print(temp_l)
        if is_safe(temp_l):
            safe_counter += 1
            break


print(safe_counter)
