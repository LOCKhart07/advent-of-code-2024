with open("./input.txt", "r") as f:
    lines = f.readlines()


l1 = []
l2 = []
for i in lines:
    # print(i.split())
    a, b = i.split()
    l1.append(int(a))
    l2.append(int(b))


l1.sort()
l2.sort()

sum = 0

for x, y in zip(l1, l2):
    sum = sum + abs(x - y)


print(sum)
