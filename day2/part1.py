with open("../day2/input.txt", "r") as f:
    levels = f.readlines()


safe_counter = 0
for i in levels:
    reports = [int(x) for x in i.split()]
    # reports = i.split()

    a_reports = sorted(reports)
    if a_reports == reports:
        diffs = [reports[n] - reports[n - 1] for n in range(1, len(reports))]
        # print(diffs)
        for diff in diffs:
            if diff < 1 or diff > 3:
                break
        else:
            safe_counter += 1
        continue

    d_reports = sorted(reports, reverse=True)
    if d_reports == reports:
        diffs = [reports[n - 1] - reports[n] for n in range(1, len(reports))]
        # print(diffs)
        for diff in diffs:
            if diff < 1 or diff > 3:
                break
        else:
            safe_counter += 1
        continue


print(safe_counter)
