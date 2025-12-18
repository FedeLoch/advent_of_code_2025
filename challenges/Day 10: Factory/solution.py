input_path = 'challenges/Day 10: Factory/input0'
from utils import Machine

# A *
part_1, part_2 = 0, 0
with open(input_path) as f:
  for line in f:
    splitted = line[:-1].split(' ')
    goal = list(map(lambda x: x == '#', splitted[0][1:-1]))
    buttons = list(map(lambda x: list(map(int, x[1:-1].split(','))), splitted[1:-1]))
    costs = list(map(int, splitted[-1][1:-1].split(',')))
    machine = Machine(goal, buttons, costs)
    part_1 += machine.fewest_required_buttons()

print('Part 1: ', part_1)