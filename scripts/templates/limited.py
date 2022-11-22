from templates.base import BaseFactGenerationTemplate


class LimitedFactGenerationTemplate(BaseFactGenerationTemplate):
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
    return ['B5', 'C3', 'C6', 'D5', 'D6', 'E3', 'E4', 'E5', 'E7', 'F4', 'F5', 'F6', 'G4', 'G5', 'H5']

  def execute(self):
    standalone_positions = ['f4']
    result = super().execute()
    edge_pos = self.attack_generator.edge()

    for item in edge_pos:
      if item in self.get_positions():
        fact = self.prolog_parser.parse('edge', [item])
        result.append(fact)

    for pos in standalone_positions:
      fact = self.prolog_parser.parse(pos, [pos])
      result.append(fact)

    return result
    