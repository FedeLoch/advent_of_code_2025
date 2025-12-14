input_path = 'challenges/Day 8: Playground/input'
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
    circuits = set()
    for _ in range(times):
        _, _, box1, box2 = distances.get()
        if box1.isConnected(box2): continue
        circuits.discard(box1.circuit)
        circuits.discard(box2.circuit)
        circuits.add(box1.connect(box2))

    circuits = sorted(circuits, key=lambda c: len(c))
    return map(lambda c: len(c), reversed(circuits))

connected = list(connect(1000))
print('Connected:', connected)
print('Part 1: ', reduce(mul, connected[0:3]))