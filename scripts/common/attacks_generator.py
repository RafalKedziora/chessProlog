from string import ascii_uppercase
from common.coords import CoordGenerator
from common.consts import BOARD_WIDTH, BOARD_HEIGHT

class AttackGenerator:
  def __init__(self) -> None:
    self.alphabet = ascii_uppercase
    self.generator = CoordGenerator()

  def black_pawn_attacks(self, pos):
    x, y = self.generator.convert_to_numeric(pos)
    attacks = []

    if y == 1:
      return attacks
    
    if x != BOARD_WIDTH:
      attacks.append((x + 1, y - 1))

    if x != 1:
      attacks.append((x - 1, y - 1))

    return list(map(self.generator.convert_to_coord, attacks))

  def white_pawn_attacks(self, pos):
    x, y = self.generator.convert_to_numeric(pos)
    attacks = []

    if y == BOARD_HEIGHT:
      return attacks
    
    if x != BOARD_WIDTH:
      attacks.append((x + 1, y + 1))

    if x != 1:
      attacks.append((x - 1, y + 1))

    return list(map(self.generator.convert_to_coord, attacks))

  def knight_attacks(self, pos):
    x, y = self.generator.convert_to_numeric(pos)
    potential = [(x + 2, y - 1), (x + 2, y + 1), (x - 2, y - 1), (x - 2, y + 1), (x + 1, y - 2), (x + 1, y + 2), (x - 1, y - 2), (x - 1, y + 2)]
    result = []

    for px, py in potential:
      if (px > 0 and px < BOARD_WIDTH) and (py > 0 and py < BOARD_HEIGHT):
        result.append((px, py))

    return list(map(self.generator.convert_to_coord, result))

  def rook_attacks(self, pos):
    x, y = self.generator.convert_to_numeric(pos)
    results = []

    for ry in range(1, BOARD_HEIGHT + 1):
      for rx in range(1, BOARD_WIDTH + 1):
        if (rx == x) != (ry == y):
          results.append((rx, ry))

    return list(map(self.generator.convert_to_coord, results))

  def bishop_attacks(self, pos):
    x, y = self.generator.convert_to_numeric(pos)
    results = []

    for ry in range(1, BOARD_HEIGHT + 1):
      for rx in range(1, BOARD_WIDTH + 1):
        if abs(rx - x) == abs(ry - y) and (rx != x and ry != y) :
          results.append((rx, ry))

    return list(map(self.generator.convert_to_coord, results))

  def king_attacks(self, pos):
    x, y = self.generator.convert_to_numeric(pos)
    results = []

    for ry in range(max(y - 1, 1), min(y + 2, BOARD_HEIGHT)):
      for rx in range(max(x - 1, 1), min(x + 2, BOARD_HEIGHT)):
        if rx != x or ry != y:
          results.append((rx, ry))

    return list(map(self.generator.convert_to_coord, results))

  def edge(self, dummy = None):
    results = []

    for ry in range(1, BOARD_HEIGHT + 1):
      for rx in range(1, BOARD_WIDTH + 1):
        if (rx == 1 or rx == BOARD_WIDTH) or (ry == 1 or ry == BOARD_HEIGHT):
          results.append((rx, ry))

    return list(map(self.generator.convert_to_coord, results))