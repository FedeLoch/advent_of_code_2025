input_path = 'challenges/Day 6: Trash Compactor/input'

operations = {
  '*': lambda x, y: x * y,
  '+': lambda x, y: x + y,
}

numbers, ops = [], []

with open(input_path) as f:
  for line in f:
    _line = line[:-1].replace('  ', ' ').split()
    if _line[0] in operations.keys(): ops = _line
    else: numbers.append(list(map(int, _line)))

def apply_operations(numbers, ops):
  result = 0
  for i in range(len(ops)):
    current_result = numbers[0][i]
    for j in range(1, len(numbers)):
      current_result = operations[ops[i]](current_result, numbers[j][i])
    result += current_result

  return result

print('Part 1:', apply_operations(numbers, ops))