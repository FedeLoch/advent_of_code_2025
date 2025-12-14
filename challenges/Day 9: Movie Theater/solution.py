input_path = 'challenges/Day 9: Movie Theater/input'
from utils import valid_tiles, is_valid_rectangle

points = set()
with open(input_path) as f:
  for line in f:
    point = tuple(map(int, line[:-1].split(',')))
    points.add(point)

rectangle_area = lambda p1, p2: (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def max_area(red_points, valid_points = [], part2 = False):
    _max, seen = 0, {}
    for point in red_points:
        for other_point in red_points:
            if other_point == point: continue
            if (point, other_point) in seen: continue
            seen[(point, other_point)] = True
            seen[(other_point, point)] = True
            if part2 and not is_valid_rectangle(point, other_point, valid_points): continue
            
            _max = max(_max, rectangle_area(point, other_point))
    return _max

print('Part 1:', max_area(points))
print('Part 2:', max_area(points, valid_tiles(list(points)), True))
