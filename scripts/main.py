from templates.base import BaseFactGenerationTemplate
from templates.full import FullFactGenerationTemplate
from templates.limited import LimitedFactGenerationTemplate

mode = 'full'
filename = f'prolog/facts_{"limited" if mode == "limited" else "full"}.pl'

def main():
  template = BaseFactGenerationTemplate()

  if mode == 'limited':
    template = LimitedFactGenerationTemplate()
  else:
    template = FullFactGenerationTemplate()

  with open(filename, 'w') as outfile:
    for fact in template.execute():
      outfile.write(fact + '\n')

if __name__ == "__main__":
  main()