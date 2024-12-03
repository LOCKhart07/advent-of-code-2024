import re

with open("./day3/input.txt", "r") as f:
    input = f.read()


regex_str = r"(mul\([0-9]{1,3}\,[0-9]{1,3}\))|(don\'t)\(\)|(do\(\))"

matches = re.findall(regex_str, input)


sumo = 0
is_enabled = True
for match in matches:

    match = "".join(match)
    print(match)
    # continue
    if match.startswith("don"):
        is_enabled = False
    elif match.startswith("do"):
        is_enabled = True
    elif is_enabled:
        a, b = match.replace("mul(", "").replace(")", "").split(",")
        sumo += int(a) * int(b)


print(sumo)
