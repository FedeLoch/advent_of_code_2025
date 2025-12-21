input_path = 'challenges/Day 12: Christmas Tree Farm/input'
from utils import Shape, Region

shapes, regions = {}, []
with open(input_path) as f:
    blocks = f.read().split('\n\n')
    
    # Parsing shapes
    for block in blocks:
        lines = block.strip().split('\n')
        if not lines: continue
        
        header = lines[0]
        if ':' in header and header.split(':')[0].strip().isdigit():
            shape_id = int(header.split(':')[0])
            grid = [list(line) for line in lines[1:]]
            shapes[shape_id] = Shape(shape_id, grid)
        elif ':' in header and 'x' in header.split(':')[0]:
            # Parsing regions
            for line in lines:
                if ':' not in line: continue
                parts = line.split(':')
                dimensions = parts[0].strip().split('x')
                w, h = int(dimensions[0]), int(dimensions[1])
                counts = list(map(int, parts[1].strip().split()))
                
                requirements = []
                for s_id, count in enumerate(counts):
                    if count > 0: requirements.append((s_id, count))
                
                regions.append(Region((w, h), requirements))

print('Part 1: ', len(list(filter(lambda region: region.isSatisfiable(shapes), regions))))