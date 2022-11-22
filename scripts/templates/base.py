from string import ascii_uppercase

from common.coords import CoordGenerator
from common.consts import BOARD_WIDTH, BOARD_HEIGHT
from common.prolog import PrologParser
from common.attacks_generator import AttackGenerator

class BaseFactGenerationTemplate:
  def __init__(self) -> None:
    self.alphabet = ascii_uppercase
    self.coord_generator = CoordGenerator()
    self.prolog_parser = PrologParser()
    self.attack_generator = AttackGenerator()

  def get_methods(self):
    return []

  def get_positions(self):
    return []

  def execute(self):
    result = []

    for fn in self.get_methods():
      for coord in self.get_positions():
        attacks = fn(coord)
        method_name = fn.__name__

        for attack in attacks:
          arr = [coord, attack]

          if method_name == 'edge':
            arr = [coord]

          if attack in self.get_positions():
            predicate = self.prolog_parser.parse(method_name, arr)
            result.append(predicate)

    return result