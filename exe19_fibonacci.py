def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
 
 
for n in range(1, 100): # testing
    print(n, "->", fib(n))


#With recursion
def fib_2(n):
    #base case
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib_2(n - 1) + fib_2(n - 2)


for n in range(1, 12):
    print(n, "->", fib_2(n))