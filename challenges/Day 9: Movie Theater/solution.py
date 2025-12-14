input_path = 'challenges/Day 9: Movie Theater/input'

points = set()
with open(input_path) as f:
  for line in f:
    point = tuple(map(int, line[:-1].split(',')))
    points.add(point)

rectangle_area = lambda p1, p2: (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def max_area(points):
    _max, seen = 0, {}
    for point in points:
        for other_point in points:
            if other_point == point: continue
            if (point, other_point) in seen: continue
            seen[(point, other_point)] = True
            seen[(other_point, point)] = True
            _max = max(_max, rectangle_area(point, other_point))
    return _max

print('Part 1:', max_area(points))
