from string import ascii_uppercase
from common.coords import CoordGenerator
from common.consts import BOARD_WIDTH, BOARD_HEIGHT

class PrologParser:
  def __init__(self) -> None:
    self.alphabet = ascii_uppercase
    self.generator = CoordGenerator()

  def parse(self, fact_name, positions):
    data = map(self.generator.convert_to_numeric, positions)
    arr = [['_' for _ in range(BOARD_HEIGHT)] for _ in range(BOARD_WIDTH)]

    for idx, coord in enumerate(data):
      arr[BOARD_HEIGHT - coord[1]][coord[0] - 1] = self.alphabet[idx]

    content = ',\n'.join([', '.join(row) for row in arr])
    variables = ','.join(self.alphabet[0 : len(positions)])

    return f"{fact_name}({variables}, c(\n{content}))."

  def mask(self, positions):
    data = list(map(self.generator.convert_to_numeric, positions))
    arr = [['A' for _ in range(BOARD_HEIGHT)] for _ in range(BOARD_WIDTH)]

    for coord in data:
      arr[BOARD_HEIGHT - coord[1]][coord[0] - 1] = '_'

    content = ',\n'.join([', '.join(row) for row in arr])

    return f"valid(A, c(\n{content}))."