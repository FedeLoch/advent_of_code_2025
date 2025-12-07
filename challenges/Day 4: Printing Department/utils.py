DIRS = {
    'UP': (-1, 0),  'DOWN': (1, 0), 'LEFT': (0, -1), 'RIGHT': (0, 1),
    'UP_LEFT': (-1, -1), 'UP_RIGHT': (-1, 1), 'DOWN_LEFT': (1, -1), 'DOWN_RIGHT': (1, 1)
}

def dict_from_file(input_path):
  row, array = 0, []
  with open(input_path) as f:
    for line in f:
      array.append([num for num in line[:-1]])
      row +=1

  return array