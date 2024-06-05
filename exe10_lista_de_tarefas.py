import os

def listar(tarefas):
  print()
  if not tarefas:
    print('Nenhuma tarefa a listar')
    print()
    #para parar a função
    return

  print('Tarefas:')
  for tarefa in tarefas:
    print(f'\t{tarefa}')
  print()
    

def desfazer(tarefas, tarefas_refazer):
  print()
  if not tarefas:
    print('Nenhuma tarefa a listar')
    #para parar a função
    return

  tarefa = tarefas.pop()
  print(f'{tarefa=} removida da lista de tarefas')
  tarefas_refazer.append(tarefa)
  print()


def refazer(tarefas, tarefas_refazer):
  print()
  if not tarefas_refazer:
    print('Nenhuma tarefa para refazer')
    return

  tarefa = tarefas_refazer.pop()
  print(f'{tarefa=} inserida novamente na lista de tarefas')
  tarefas.append(tarefa)
  print()


def adicionar(tarefa, tarefas):
  print()
  tarefa = tarefa.strip()
  if not tarefa:
    print('Você não digitou nenhuma tarefa')
    return
  
  print(f'{tarefa=} adicionada na lista de tarefas')
  tarefas.append(tarefa)
  print()



tarefas = []
tarefas_refazer =[]

while True:
  print('Comandos: listar, desfazer, refazer')
  tarefa = input('Digite uma tarefa ou comando: ')

  if tarefa == 'listar':
    listar(tarefas)
  elif tarefa == 'desfazer':
    print(2)
    desfazer(tarefas, tarefas_refazer)
    listar(tarefas)
    continue  

  elif tarefa == 'refazer':
    print(3)
    refazer(tarefas, tarefas_refazer)
    listar(tarefas)
    continue

  elif tarefa == 'clear':
    os.system('clear')
    continue

  else:
    adicionar(tarefa, tarefas)
    listar(tarefas)
