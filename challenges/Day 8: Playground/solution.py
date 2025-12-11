input_path = 'challenges/Day 8: Playground/input0'
from functools import reduce
from operator import mul
from utils import Box
import queue
import itertools

boxes, distances, tie = [], queue.PriorityQueue(), itertools.count()

with open(input_path) as f:
  for line in f:
    x, y, z = line[:-1].split(',')
    box = Box(int(x), int(y), int(z))
    for other_box in boxes:
        dist = box.euclidean_distance(other_box)
        distances.put((dist, next(tie), box, other_box))
    boxes.append(box)

def connect(times):
    circuits = []
    for _ in range(times):
        dist, _, box1, box2 = distances.get()
        print('Connecting boxes at distance', dist, '->', (box1.x, box1.y, box1.z), '<->', (box2.x, box2.y, box2.z))
        if box1.isConnected(box2): continue
        box1.connect(box2)
        circuits.append(box1.circuit)

    circuits.sort(key=lambda c: len(c))
    return map(lambda c: len(c), reversed(circuits))

print('Part 1: ', reduce(mul, list(connect(10))[0:3]))