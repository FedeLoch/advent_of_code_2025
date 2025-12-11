
import math

class Box(object):
    def __init__(self, x, y, z):
        self.x = x; self.y = y; self.z = z; self.circuit = {self}
    
    def isConnected(self, other): return self.circuit is other.circuit
    def connect(self, other):
        new_circuit = self.circuit.union(other.circuit)
        for box in new_circuit: box.circuit = new_circuit
    def euclidean_distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)
