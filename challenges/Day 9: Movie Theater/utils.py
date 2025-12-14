from collections import deque

def is_in(point, valid_lines):
    if point[0] not in valid_lines: return False
    return point[1] >= valid_lines[point[0]][0] and point[1] <= valid_lines[point[0]][1]

def is_valid_rectangle(p1, p2, valid_lines):
    xmin, xmax = sorted([p1[0], p2[0]])
    ymin, ymax = sorted([p1[1], p2[1]])

    return (is_in((xmin, ymin), valid_lines) and is_in((xmin, ymax), valid_lines) and
        is_in((xmax, ymin), valid_lines) and is_in((xmax, ymax), valid_lines)
    )

horizotal_points = lambda p1, p2: [ (p1[0], y) for y in range(min(p1[1], p2[1]) + 1, max(p1[1], p2[1])) ]
vertical_points = lambda p1, p2: [ (x, p1[1]) for x in range(min(p1[0], p2[0]) + 1, max(p1[0], p2[0])) ]
all_points_on_line = lambda p1, p2: horizotal_points(p1, p2) if p1[0] == p2[0] else vertical_points(p1, p2)

def build_border(points):
    border, seen = [], set()
    queue = deque([points.pop()])

    while queue:
        x, y = queue.popleft()
        if (x, y) in seen: continue
        seen.add((x, y))
        border.append((x, y))

        for point in points:
            if not point in seen and (point[0] == x or point[1] == y):
                border += all_points_on_line((x, y), point)
                queue.append(point)
    return border

def border_lines(border):
    _dict = {}
    for x, y in border:
        if x not in _dict: _dict[x] = (y, y); continue
        _dict[x] = (min(_dict[x][0], y), max(_dict[x][1], y))
    return _dict

valid_tiles = lambda red_points: border_lines(build_border(red_points))
