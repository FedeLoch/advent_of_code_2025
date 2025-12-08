import re


input_path = 'challenges/Day 6: Trash Compactor/input0'

operations = { '*': lambda x, y: x * y, '+': lambda x, y: x + y }
numbers, string_numbers, ops = [], [], []

with open(input_path) as f:
  for line in f:
    _line = line[:-1].replace('  ', ' ').split()
    if _line[0] in operations.keys(): ops = _line
    else:
      string_numbers.append([line[:-1][i:i+3] for i in range(0, len(line[:-1]), n)])
      numbers.append(list(map(int, _line)))

def part_1(numbers, ops):
  result = 0
  for i in range(len(ops)):
    current_result = numbers[0][i]
    for j in range(1, len(numbers)):
      current_result = operations[ops[i]](current_result, numbers[j][i])
    result += current_result

  return result

def read_cephalopod_column(matrix, i):
    col = [row[i] for row in matrix]
    res = []
    for i in reversed(range(len(col[0]))):
      s = ''.join(list(map(lambda e: e[i], col))).strip()
      res.append(int(s))
    return res

def part_2(numbers, ops):
  result = 0
  for i in range(len(ops)):
    column_numbers = list(read_cephalopod_column(numbers, i))
    current_result = column_numbers[0]
    for j in range(1, len(column_numbers)):
      current_result = operations[ops[i]](current_result, column_numbers[j])
    result += current_result

  return result  

print('Part 1:', part_1(numbers, ops))
print('Part 2:', part_2(string_numbers, ops))