""" The Digit of Life
Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple – you just need to sum all the digits of the date. If the result contains more than one digit, you have to repeat the addition until you get exactly one digit. For example:

1 January 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3
3 is the digit we searched for and found.

Your task is to write a program which:

asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY – actually, the order of the digits doesn't matter)
outputs the Digit of Life for the date. """

#MINHA RESOLUÇÃO
from time import sleep

while True:
    ano = input('Digite o ano de nascimento [YYYY] : ')
    try:
        ano_int = int(ano)
        if len(ano) != 4:
            print('O ano deve ter 4 dígitos')
            continue
        mes = input('Digite o mês de nascimento [MM] : ')
        try:
            mes_int = int(mes)
            if mes_int < 1 or mes_int > 12:
                print('O mês deve ser entre 1 e 12')
                continue
            dia = input('Digite o dia de nascimento [DD] : ')
            try:
                dia_int = int(dia)
                if dia_int < 1 or dia_int > 31:
                    print('O dia deve ser entre 1 e 31')
                    continue
                break  # Todos os valores são válidos, saímos do loop
            except ValueError:
                print('Formato de dia inválido')
        except ValueError:
            print('Formato de mês inválido')
    except ValueError:
        print('Formato de ano inválido')

print(f'Sua data de nascimento é: {ano_int}/{mes_int}/{dia_int}...Calculando...')
sleep(3)
digits = ano + mes + dia

soma_digits = 0
while True:
    for number in digits:
        number_int = int(number)
        soma_digits += number_int
    if soma_digits >= 10:
        digits = str(soma_digits)
        soma_digits = 0
        continue
    else:
        break

print(f'Seu dígito da vida é {soma_digits}')
    

