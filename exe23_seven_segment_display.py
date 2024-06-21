""" A LED Display
You've surely seen a seven-segment display.

It's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit using a subset of seven segments. If you still don't know what it is, refer to the following Wikipedia article.

Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.

Each digit is constructed from 13 LEDs (some lit, some dark, of course) – that's how we imagine it:

  # ### ### # # ### ### ### ### ### ###
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###
Note: the number 8 shows all the LED lights on.

Your code has to display any non-negative integer number entered by the user.

Tip: using a list containing patterns of all ten digits may be very helpful. """



#verificando se o numero é positivo
while True:
  number_str = input('Digite um número inteiro positivo: ')

  try:
    number = int(number_str)
    if number > 0:
      break
    else:
      print('Digite um número maior que 0')

  except ValueError: 
    print('Número inválido, digite um número inteiro')


# Construindo numeros

zero = [
    " _ ",
    "| |",
    "|_|"
]

um = [
    "   ",
    "  |",
    "  |"
]

dois = [
    " _ ",
    " _|",
    "|_ "
]

tres = [
    " _ ",
    " _|",
    " _|"
]

quatro = [
    "   ",
    "|_|",
    "  |"
]

cinco = [
    " _ ",
    "|_ ",
    " _|"
]

seis = [
    " _ ",
    "|_ ",
    "|_|"
]

sete = [
    " _ ",
    "  |",
    "  |"
]

oito = [
    " _ ",
    "|_|",
    "|_|"
]

nove = [
    " _ ",
    "|_|",
    " _|"
]

""" # Função imprimir numero
def print_digit(digit):
  print('\n'.join(digit)) """


display = []
for number in number_str:
  if number == '0':
    display.append(zero)
  if number == '1':
    display.append(um)
  if number == '2':
    display.append(dois)
  if number == '3':
    display.append(tres)
  if number == '4':
    display.append(quatro)
  if number == '5':
    display.append(cinco)
  if number == '6':
    display.append(seis)
  if number == '7':
    display.append(sete)
  if number == '8':
    display.append(oito)
  if number == '9':
    display.append(nove)


# Função para imprimir os números na mesma linha(CHAT GPT)
def print_digits_in_line(digits):
  for i in range(3):  # número de linhas em cada dígito
    line = ""
    for digit in digits:
      line += digit[i] + " "
    print(line)

print_digits_in_line(display)



""" # SOLUÇÃO DO EXERCÍCIO
digits = [ '1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]


def print_number(num):
	global digits
	digs = str(num)
	lines = [ '' for lin in range(5) ]
	for d in digs:
		segs = [ [' ',' ',' '] for lin in range(5) ]
		ptrn = digits[ord(d) - ord('0')]
		if ptrn[0] == '1':
			segs[0][0] = segs[0][1] = segs[0][2] = '#'
		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '#'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '#'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '#'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '#'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '#'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '#'
		for lin in range(5):
			lines[lin] += ''.join(segs[lin]) + ' '
	for lin in lines:
		print(lin)


print_number(int(input("Enter the number you wish to display: "))) """
    