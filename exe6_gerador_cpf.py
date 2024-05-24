#GERADOR DE CPF

import random

nove_digitos = ''
for i in range(9):
  nove_digitos += str(random.randint(0, 9))

print(nove_digitos)

cpf_digitado = nove_digitos

contagem_1 = 10
soma_1 = 0
digito_1 = 0

for numero in cpf_digitado:
  soma_1 += int(numero) * contagem_1
  contagem_1 -= 1

digito_1 = (soma_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

contagem_2 = 11
soma_2 = 0
digito_2 = 0
cpf_dez_primeiros_numeros = str(nove_digitos) + str(digito_1)

for numero in cpf_dez_primeiros_numeros:
  soma_2 += int(numero) * contagem_2
  contagem_2 -= 1
digito_2 = (soma_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = str(cpf_digitado) + str(digito_1) + str(digito_2)

print(f'CPF gerado: {cpf_gerado}')