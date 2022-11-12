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

  return f"{fact_name}({variables}, c(\n{content}))."

# position generating
# following functions work only assuming that nothing stands on the way of figure

def get_black_pawn_attacks(pos):
  x, y = convert_coord_to_numeric(pos)
  attacks = []

  if y == 1:
    return attacks
  
  if x != board_width:
    attacks.append((x + 1, y - 1))

  if x != 1:
    attacks.append((x - 1, y - 1))

  return list(map(convert_numeric_to_coord, attacks))

def get_white_pawn_attacks(pos):
  x, y = convert_coord_to_numeric(pos)
  attacks = []

  if y == board_height:
    return attacks
  
  if x != board_width:
    attacks.append((x + 1, y + 1))

  if x != 1:
    attacks.append((x - 1, y + 1))

  return list(map(convert_numeric_to_coord, attacks))

def get_knight_attacks(pos):
  x, y = convert_coord_to_numeric(pos)
  potential = [(x + 2, y - 1), (x + 2, y + 1), (x - 2, y - 1), (x - 2, y + 1), (x + 1, y - 2), (x + 1, y + 2), (x - 1, y - 2), (x - 1, y + 2)]
  result = []

  for px, py in potential:
    if (px > 0 and px < board_width) and (py > 0 and py < board_height):
      result.append((px, py))

  return list(map(convert_numeric_to_coord, result))

def get_rook_attacks(pos):
  x, y = convert_coord_to_numeric(pos)
  results = []

  for ry in range(1, board_height + 1):
    for rx in range(1, board_width + 1):
      if (rx == x) != (ry == y):
        results.append((rx, ry))

  return list(map(convert_numeric_to_coord, results))

def get_bishop_attacks(pos):
  x, y = convert_coord_to_numeric(pos)
  results = []

  for ry in range(1, board_height + 1):
    for rx in range(1, board_width + 1):
      if abs(rx - x) == abs(ry - y) and (rx != x and ry != y) :
        results.append((rx, ry))

  return list(map(convert_numeric_to_coord, results))

def get_king_attacks(pos):
  x, y = convert_coord_to_numeric(pos)
  results = []

  for ry in range(max(y - 1, 1), min(y + 2, board_height)):
    for rx in range(max(x - 1, 1), min(x + 2, board_height)):
      if rx != x or ry != y:
        results.append((rx, ry))

  return list(map(convert_numeric_to_coord, results))

def get_edge():
  results = []

  for ry in range(1, board_height + 1):
    for rx in range(1, board_width + 1):
      if (rx == 1 or rx == board_width) or (ry == 1 or ry == board_height):
        results.append((rx, ry))

  return list(map(convert_numeric_to_coord, results))

# No queen attacks involed - it's a sum of rook + bishop so can be optimized
# Fact generator

def generate_all_facts():
  facts = { 
    'f4': [place_figure_fact('f4', ['f4'])],
    'edge': [], 
  }
  edge = get_edge()

  for coord in edge:
    if coord in available_coords:
      fact = place_figure_fact('edge', [coord])
      facts['edge'].append(fact)

  for coord in available_coords:
    figure_moves = {
      'bishop_attacks': get_bishop_attacks(coord),
      'black_pawn_attacks': get_black_pawn_attacks(coord),
      'knight_attacks': get_knight_attacks(coord),
      'rook_attacks': get_rook_attacks(coord),
      'white_pawn_attacks': get_white_pawn_attacks(coord),
      'king_attacks': get_king_attacks(coord),
    }

    for name, moves in figure_moves.items():
      for move in moves:
        if move in available_coords:
          fact = place_figure_fact(name, [coord, move])

          if name not in facts:
            facts[name] = []

          facts[name].append(fact)

  return facts

# Generator execution:    

filename = '205006_26.pl'
test = generate_all_facts()

with open(filename, 'w') as outfile:
  for key, facts in test.items():
    for item in facts:
      outfile.write(item)
      outfile.write('\n')

    outfile.write('\n')

  outfile.write('queen_attacks(A, B, S) :- bishop_attacks(A, B, S) ; rook_attacks(A, B, S).')


  