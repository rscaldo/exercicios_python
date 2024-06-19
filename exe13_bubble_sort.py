my_list = [8, 10, 6, 2, 4]
swapped = True

while swapped:
  swapped = False
  for i in range(len(my_list) -1):
    if my_list[i] > my_list[i + 1]:
      swapped = True
      my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]


print(my_list)

my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)

my_list_2 = sorted(my_list)

print(my_list_2)