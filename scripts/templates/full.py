from string import ascii_uppercase
from common.consts import BOARD_WIDTH, BOARD_HEIGHT
from templates.limited import LimitedFactGenerationTemplate
from templates.base import BaseFactGenerationTemplate


class FullFactGenerationTemplate(BaseFactGenerationTemplate):
  def __init__(self) -> None:
    super().__init__()

  def get_methods(self):
    return [
      self.attack_generator.bishop_attacks,
      self.attack_generator.black_pawn_attacks,
      self.attack_generator.white_pawn_attacks,
      self.attack_generator.king_attacks,
      self.attack_generator.knight_attacks,
      self.attack_generator.rook_attacks
    ]

  def get_positions(self):
    array2d = [[f'{ascii_uppercase[w]}{h}' for h in range(1, BOARD_HEIGHT + 1)] for w in range(BOARD_WIDTH)]
    return [item for sublist in array2d for item in sublist]

  def execute(self):
    standalone_positions = ['f4']
    result = super().execute()
    limited_positions = LimitedFactGenerationTemplate().get_positions()
    edge_pos = self.attack_generator.edge()

    for item in edge_pos:
      if item in self.get_positions():
        fact = self.prolog_parser.parse('edge', [item])
        result.append(fact)

    mask = self.prolog_parser.mask(limited_positions)
    result.append(mask)

    for pos in standalone_positions:
      fact = self.prolog_parser.parse(pos, [pos])
      result.append(fact)

    return result
    