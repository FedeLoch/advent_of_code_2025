from collections import deque

def is_valid_rectangle(p1, p2, valid):
    xmin, xmax = sorted([p1[0], p2[0]])
    ymin, ymax = sorted([p1[1], p2[1]])

    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            if (x, y) not in valid: return False

    return True

def build_border(points):
    border, n = set(), len(points)

    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]

        if x1 == x2:
            step = 1 if y2 > y1 else -1
            for y in range(y1, y2 + step, step): border.add((x1, y))
        else:
            step = 1 if x2 > x1 else -1
            for x in range(x1, x2 + step, step): border.add((x, y1))
    return border

def fill_inside(border):
    xs = [x for x, _ in border]
    ys = [y for _, y in border]

    minx, maxx = min(xs) - 1, max(xs) + 1
    miny, maxy = min(ys) - 1, max(ys) + 1

    visited = set()
    queue = deque([(minx, miny)])

    while queue:
        x, y = queue.popleft()
        if (x, y) in visited: continue
        if (x, y) in border: continue
        if not (minx <= x <= maxx and miny <= y <= maxy): continue

        visited.add((x, y))
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]: queue.append((x+dx, y+dy))

    inside = set()
    for x in range(minx+1, maxx):
        for y in range(miny+1, maxy):
            if (x, y) not in visited:
                inside.add((x, y))

    return inside

def print_graph(graph):
    for row in graph:
        print(''.join(row))

def add_points_to_graph(points, red_points, filled, graph):
    for x, y in points: graph[y][x] = 'X'
    for x, y in filled: graph[y][x] = 'X'
    for x, y in red_points: graph[y][x] = '#'

    return graph

def valid_tiles(red_points):
    border = build_border(red_points)
    grid = [ [ '.' for i in range(14) ] for i in range(9) ]
    # filled = fill_inside(border)
    print_graph(add_points_to_graph(border, red_points, [], grid))
    return fill_inside(border)
