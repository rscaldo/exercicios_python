print()
import sys
 
sys.path.append('..∖∖modules')
for p in sys.path:
  print(p)

import exe21_modulo

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]

print()
print(exe21_modulo.suml(zeroes))
print(exe21_modulo.prodl(ones))