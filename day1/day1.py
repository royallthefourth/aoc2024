import sys


def parse_line(line: str) -> tuple[int, int]:
    nums = line.split("   ")
    return int(nums[0]), int(nums[1])

a = list()
b = list()
acc = 0

with open(sys.argv[1], encoding="utf-8") as f:
    for line in f:
        l = parse_line(line)
        a.append(l[0])
        b.append(l[1])

a.sort()
b.sort()

for i in range(len(a)):
    acc += abs(a[i] - b[i])

print(acc)
