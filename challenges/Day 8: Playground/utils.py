
import math

class Box(object):
    def __init__(self, x, y, z):
        self.x = x; self.y = y; self.z = z; self.circuit = Circuit({self})
    
    def isConnected(self, other): return self.circuit is other.circuit
    def connect(self, other): return self.circuit.union(other.circuit)
    def euclidean_distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

class Circuit(object):
    def __init__(self, boxes):
        self.boxes = boxes
        for box in boxes: box.circuit = self

    def union(self, other): return Circuit(self.boxes.union(other.boxes))
    def __len__(self): return len(self.boxes)