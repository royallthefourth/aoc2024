import sys

def parse_line(l: str) -> list[int]:
    out = list()
    nums = l.split(" ")
    for n in nums:
        out.append(int(n))
    return out

def is_safe(report: list[int]) -> bool:
    pos = True
    for ix, n in enumerate(report):
        if ix == 0:
            continue
        if ix == 1:
            pos = n > report[ix-1]
        if (abs(n - report[ix-1]) > 3
            or n == report[ix-1]
            or pos != (n > report[ix-1])):
            return False
    return True

def is_safe_damp(report: list[int]) -> bool:
    if is_safe(report):
        return True
    for ix, n in enumerate(report):
        r = report.copy()
        del r[ix]
        if is_safe(r):
            return True
    return False

def main() -> int:
    nsafe = 0

    with open(sys.argv[1], encoding="utf-8") as f:
        for line in f:
            report = parse_line(line)
            if is_safe_damp(report):
                nsafe += 1

    print(nsafe)
    return 0

if __name__ == "__main__":
    sys.exit(main())
