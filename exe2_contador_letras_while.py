# Exercício 2 > Contador de letras da frase

""" NÃO RESOLVE O PROBLEMA DE UMA LETRA COM A MESMA QUANTIDADE """


frase = input('Digite a sua frase: ').lower()

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

# precisamos somente checar se a letra atual é maior que a letra anterior
while i < len(frase):
  letra_atual = frase[i]

  #eliminando o espaço da contagem
  if letra_atual == ' ':
    i += 1
    continue

  qtd_apareceu_letra_atual = frase.count(letra_atual)

  if qtd_apareceu_mais_vezes < qtd_apareceu_letra_atual:
    qtd_apareceu_mais_vezes = qtd_apareceu_letra_atual
    letra_apareceu_mais_vezes = letra_atual

  i += 1

print(
  'A letra que apareceu mais vezes foi '
  f'"{letra_apareceu_mais_vezes}" que apareceu {qtd_apareceu_mais_vezes}x'
)