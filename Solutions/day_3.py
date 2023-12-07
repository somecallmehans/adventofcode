# Forgive me father this is not my
import re
from collections import defaultdict
from math import prod

file = open("day_3_input.txt", "r")
lines = file.read().split("\n")

symbols = dict()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c not in "1234567890.":
            symbols[(x, y)] = c

part_numbers = defaultdict(list)
part_numbers_sum = 0
for y, line in enumerate(lines):
    for num in re.finditer(r"\d+", line):
        for s_x, s_y in symbols:
            if (num.start() - 1 <= s_x <= num.end()) and (y - 1 <= s_y <= y + 1):
                int_num = int(num.group())
                part_numbers[(s_x, s_y)].append(int_num)
                part_numbers_sum += int_num
                break

# ========= PART 1 =========
print(part_numbers_sum)

# ========= PART 2 =========
print(
    sum(
        prod(parts)
        for pos, parts in part_numbers.items()
        if len(parts) == 2 and symbols[pos] == "*"
    )
)
