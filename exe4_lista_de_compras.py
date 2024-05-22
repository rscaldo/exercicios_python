"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

# MINHA SOLUÇÃO

import os
lista_compras = []

while True:

  opcao = input('Selecione uma opção\n[i]nserir [a]pagar [l]istar [s]sair: ').lower()


  if opcao[0] == 'i':
    os.system('cls')
    inserir = input('Digite o que deseja inserir: ')
    lista_compras.append(inserir)
    for indice, produto in enumerate(lista_compras):
      print(indice, produto)
  elif opcao[0] == 'a':
    apagar = input('Escolha o índice para apagar: ')
    try:
      apagar_int = int(apagar)
      if apagar_int > len(lista_compras):
        print('Indice inexiteste')
      else:
        del lista_compras[apagar_int]
        for indice, produto in enumerate(lista_compras):
          print(indice, produto)
    except:
      print('Opção inválida')
  elif opcao[0] == 'l':
    os.system('cls')
    if lista_compras == []:
      print('Nada para listar')
    else:
      for indice, produto in enumerate(lista_compras):
        print(indice, produto)
  elif opcao[0] == 's':
    print('Sair')
    break
  else:
    print('Por favor escolha i, a, l, ou s')