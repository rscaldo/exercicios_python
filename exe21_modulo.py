""" print("I like to be a module.")
print(__name__)


#This is how you can make use of the __main__ variable in order to detect the context in which your code has been activated:
if __name__ == "__main__":
  print('Estou no script do modulo')
else:
  print('Estou sendo executado em outro script')
  #Each time you modify any of these functions, you can simply run the module to make sure that your amendments didn't spoil the code. These tests will be omitted when the code is imported as a module.
   """


__counter = 0

def suml(the_list):
  global __counter
  __counter += 1
  the_sum = 0
  for element in the_list:
    the_sum += element
  return the_sum


def prodl(the_list):
  global __counter
  __counter += 1
  prod = 1
  for element in the_list:
   prod *= element
  return prod


if __name__ == '__main__':
  print('I prefer to be a module, but i can do some tests for you.')
  my_list = [i+1 for i in range(5)]
  print(suml(my_list) == 15)
  print(prodl(my_list) == 120)