input_path = 'challenges/Day 1: Secret Entrance/input'

_max, dial, zeros, dirs = 100, 50, 0, {
  'L': lambda x, y : (x - y),
  'R': lambda x, y: (x + y)
}

with open(input_path) as f:
  for line in f:
    prev, _dial = dial, dirs[line[0]](dial, int(line[1:-1]) % _max)
    dial = _dial % _max
    zeros += (int(line[1:-1]) // _max) + (1 if dial == 0 or (prev != 0 and dial != _dial) else 0)

print('Part 2:', zeros)