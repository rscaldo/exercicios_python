# Exercício - sistema de perguntas e respostas



perguntas = [

    {

        'Pergunta': 'Quanto é 2+2?',

        'Opções': ['1', '3', '4', '5'],

        'Resposta': '4',

    },

    {

        'Pergunta': 'Quanto é 5*5?',

        'Opções': ['25', '55', '10', '51'],

        'Resposta': '25',

    },

    {

        'Pergunta': 'Quanto é 10/2?',

        'Opções': ['4', '5', '2', '1'],

        'Resposta': '5',

    },
]

qtd_acertos = 0
for pergunta in perguntas:
  print('Pergunta: ', pergunta['Pergunta'])
  print()

  for i, opcao in enumerate(pergunta['Opções']):
    print(f'{i})', opcao)

  escolha = input('Escolha uma opção: ')

  # Queremos que a escolha da pessoa seja um número inteiro
  #flag
  escolha_int = None
  acertou = False

  # Verifica se temos somente números, exclui decimal tb por somente de 0 a 9
  if escolha.isdigit():
    escolha_int = int(escolha)
  
    if escolha_int >= 0 and escolha_int < len(pergunta['Opções']):
      if pergunta['Opções'][escolha_int] == pergunta['Resposta']:
        acertou = True
  
  if acertou:
    qtd_acertos += 1
    print('Acertou')
  else:
    print('Errou!')

  print()

print(f'Você acertou {qtd_acertos} de {len(perguntas)}, perguntas')