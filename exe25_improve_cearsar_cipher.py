""" Improving the Caesar cipher
You are already familiar with the Caesar cipher, and this is why we want you to improve the code we showed you recently.

The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.

Your task is to write a program which:

asks the user for one line of text to encrypt;
asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
prints out the encoded text.
Test your code using the data we've provided. """
from time import sleep

text = input('Enter your massage: ')
cipher = ''

while True:
  shift_value = input('Enter a shift value(1 - 25):')
  try:
    shift_value_int = int(shift_value)
    if 1 <= shift_value_int <= 25:
      print('Encrypting...')
      sleep(3)
      break
    else:
      print('Please enter a number between 1 and 25.')
  except ValueError:
    print('Invalid input. Please enter a number between 1 and 25.')
 
for char in text:
  if char.isalpha():
    code = ord(char) + shift_value_int
    first = ord('A') if char.isupper() else ord('a')
    code -= first
    code %= 26
    cipher += chr(first + code)
  else:
    cipher += char

print(cipher)
print()
print('*-*' * 20)
print()