input_path = 'challenges/Day 5: Cafeteria/input'
from functools import reduce

range_lines, ids = [], []

def merge(_ranges):
    ranges = sorted(map(lambda x: tuple(map(int, x.split('-'))), _ranges))
    merged = []
    cur_start, cur_end = ranges[0]

    for _min, _max in ranges[1:]:
        if _min <= cur_end + 1:
            cur_end = max(cur_end, _max)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = _min, _max

    merged.append((cur_start, cur_end))

    return merged

with open(input_path) as f:
    lines = [line.strip() for line in f]
    blank = lines.index("")
    range_lines = merge(lines[:blank])
    ids = lines[blank+1:]

is_in = lambda id, ranges: any(low <= id <= high for low, high in ranges)
count_valid_ids = lambda ranges, ids: reduce(lambda acc, id: acc + (1 if is_in(int(id), ranges) else 0), ids, 0)

print('Part 1:', count_valid_ids(range_lines, ids))