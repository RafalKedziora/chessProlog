import string

board_width = 8
board_height = 8

available_coords = [
  'B5', 'C3', 'C6', 'D5', 'D6', 'E3', 'E4', 'E5', 'E7', 'F4', 'F5', 'F6', 'G4', 'G5', 'H5'
]

# fact generating

def convert_coord_to_numeric(position):
  alphabet = string.ascii_lowercase
  x_coord = (alphabet.find(position[0].lower())) + 1
  y_coord = int(position[1])

  return x_coord, y_coord

def convert_numeric_to_coord(numeric):
  return f'{string.ascii_uppercase[numeric[0] - 1]}{numeric[1]}'

def place_figure_fact(fact_name, positions):
  data = map(convert_coord_to_numeric, positions)
  arr = [['_' for x in range(board_height)] for y in range(board_width)]

  for idx, coord in enumerate(data):
    arr[board_height - coord[1]][coord[0] - 1] = string.ascii_uppercase[idx]

  content = ',\n'.join([', '.join(row) for row in arr])
  variables = ','.join(string.ascii_uppercase[0 : len(positions)])

  return f"{fact_name}({variables}, c({content}))."

# position generating
# following functions work only assuming that nothing stands on the way of figure

def get_black_pawn_attacks(pos):
  x, y = convert_coord_to_numeric(pos)
  attacks = []

  if y == 1:
    return attacks
  
  if x != board_width:
    attacks.append(convert_numeric_to_coord((x + 1, y - 1)))

  if x != 1:
    attacks.append(convert_numeric_to_coord((x - 1, y - 1)))

  return attacks

def get_white_pawn_attacks(pos):
  x, y = convert_coord_to_numeric(pos)
  attacks = []

  if y == board_height:
    return attacks
  
  if x != board_width:
    attacks.append(convert_numeric_to_coord((x + 1, y + 1)))

  if x != 1:
    attacks.append(convert_numeric_to_coord((x - 1, y + 1)))

  return attacks

def get_knight_attacks(pos):
  x, y = convert_coord_to_numeric(pos)
  potential = [(x + 2, y - 1), (x + 2, y + 1), (x - 2, y - 1), (x - 2, y + 1), (x + 1, y - 2), (x + 1, y + 2), (x - 1, y - 2), (x - 1, y + 2)]
  result = []

  for px, py in potential:
    if (px > 0 and px < board_width) and (py > 0 and py < board_height):
      result.append((px, py))

  return result

# TODO: rook, bishop, queen