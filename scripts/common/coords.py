from string import ascii_uppercase

class CoordGenerator:
  def __init__(self) -> None:
    self.alphabet = ascii_uppercase

  def convert_to_numeric(self, position):
    x_coord = (self.alphabet.find(position[0].upper())) + 1
    y_coord = int(position[1])

    return x_coord, y_coord

  def convert_to_coord(self, numeric):
    return f'{self.alphabet[numeric[0] - 1]}{numeric[1]}'

  