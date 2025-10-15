import re
import sys

def find_muls(corpus: str) -> list:
    return re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", corpus)

def run_prog(prog: list[str]) -> int:
    active = True
    acc = 0
    for inst in prog:
        if inst == "do()":
            active = True
        elif inst == "don't()":
            active = False
        elif active:
            acc += do_mul(inst)
    return acc

def do_mul(input: str) -> int:
    parts = input.replace("mul(", "").replace(")","").split(",")
    return int(parts[0]) * int(parts[1])

def main() -> int:

    with open(sys.argv[1]) as f:
        print(run_prog(find_muls("".join(f.readlines()))))

    return 0

if __name__ == "__main__":
    sys.exit(main())
