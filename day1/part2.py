with open("./input.txt", "r") as f:
    lines = f.readlines()


l1 = []
l2 = []
for i in lines:
    # print(i.split())
    a, b = i.split()
    l1.append(int(a))
    l2.append(int(b))


freq_hm = {}

for y in l2:
    if y not in freq_hm:
        freq_hm[y] = 0
    freq_hm[y] += 1


sum = 0
for x in l1:
    multiplied_num = x * freq_hm.get(x, 0)
    sum = sum + multiplied_num

print(sum)
