from templates.full import FullFactGenerationTemplate
from templates.limited import LimitedFactGenerationTemplate


def main():
  mode = ''
  filename = ''

  while mode not in ['1', '2']:
    print('GENERATOR FAKTÓW DO ZADANIA "SZACHY" - ZESTAW 26')
    print('==================================================\n')
    print('Czy chcesz pełny zestaw faktów (klawisz 1), czy ograniczony do zestawu 26 (klawisz 2)?')
    mode = input('Twoja odpowiedź: ')
    
    if mode == '1':
      template = FullFactGenerationTemplate()
      filename = 'prolog/facts_full.pl'
    if mode == '2':
      template = LimitedFactGenerationTemplate()
      filename = 'prolog/facts_limited.pl'
    

  with open(filename, 'w') as outfile:
    for fact in template.execute():
      outfile.write(fact + '\n')

  print(f'\nWygenerowano zestaw danych. Ścieżka: {filename}')

if __name__ == "__main__":
  main()