import re

with open("./day3/input.txt", "r") as f:
    input = f.read()


regex_str = r"mul\([0-9]{1,3}\,[0-9]{1,3}\)"

matches = re.findall(regex_str, input)


sumo = 0
for match in matches:
    a, b = match.replace("mul(", "").replace(")", "").split(",")
    sumo += int(a) * int(b)


print(sumo)
