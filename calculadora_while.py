# Calculadora com while

#a calculadora vai rodas até o usuário digital para sair
while True:

  numero_1 = input('Digite um número: ')
  numero_2 = input('Digite outro número: ')
  operador = input('Digite o operador (+ - / *): ')

  #Verificar se os números são válidos usando o try/except e vamos criar uma flag
  numeros_validos = None
  num_1_float = 0
  num_2_float = 0

  try:
    #vamos tentar converter os números para float
    num_1_float = float(numero_1)
    num_2_float = float(numero_2)
    #se chegar nessa linha quer dizer que os números são válidos
    numeros_validos = True
  except:
    print(' Um dos números é inválido, \n Digite os números novamente')
    # Volta ao topo do laço
    continue
    
  #Verificar o perador
  operadores_permitidos = '+-/*'

  if operador not in operadores_permitidos:
    print('Operador inválido \n Comece novamente')
    continue

  #verificar se recebeu somente 1 operador
  if len(operador) > 1:
    print('Digite somente um operador')
    continue

  #cálculos
  print('Realizando a conta, \n o resultado de: ')
  if operador == '+':
    print(f'{num_1_float} + {num_2_float} =',num_1_float + num_2_float)
  elif operador == '-':
    print(f'{num_1_float} - {num_2_float} =',num_1_float - num_2_float)
  elif operador == '/':
    print(f'{num_1_float} / {num_2_float} =',num_1_float / num_2_float)
  elif operador == '*':
    print(f'{num_1_float} * {num_2_float} =',num_1_float * num_2_float)
  #retonar um bool
  sair = input('Deseja sair? [s]im: ').lower().startswith('s')
  if sair:
    print('Você saiu')  
    break