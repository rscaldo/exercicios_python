# Caesar cipher
#encrypting a message

text = input('Enter your massage: ')
cipher = ''
for char in text:
  #ignorar o que não é letra
  if not char.isalpha():
    continue
  char = char.upper()
  code = ord(char) + 1
  #exception no caso de Z
  if code > ord('Z'):
    code = ord('A')
  cipher += chr(code)

print(cipher)
print()
print('*-*' * 20)
print()




